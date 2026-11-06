"""게임 전체(퀴즈 목록, 점수, 메뉴 흐름)를 관리하는 QuizGame 클래스."""

import os
import random

from default_quizzes import create_default_quizzes
from input_utils import read_number, read_text, read_yes_no
from quiz import CHOICE_COUNT, Quiz
from storage import StateFileError

LINE = "=" * 40
SUB_LINE = "-" * 40
HINT_CREDIT = 0.5  # 힌트를 보고 맞히면 해당 문제 점수의 50%만 인정


class QuizGame:
    """퀴즈 목록과 최고 점수를 가지고 메뉴를 진행하는 게임 관리자."""

    def __init__(self, storage):
        self.storage = storage
        self.quizzes = []
        self.best_score = None  # 아직 한 번도 풀지 않았으면 None
        self.best_correct = 0
        self.best_total = 0
        self.load_message = ""

        # (메뉴 이름, 실행할 메서드). 메서드가 None이면 종료
        self.menu_items = [
            ("퀴즈 풀기", self.play_quiz),
            ("퀴즈 추가", self.add_quiz),
            ("퀴즈 목록", self.list_quizzes),
            ("점수 확인", self.show_best_score),
            ("퀴즈 삭제", self.delete_quiz),
            ("종료", None),
        ]

    # ------------------------------------------------------------------ 메뉴
    def print_banner(self):
        print(LINE)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print(LINE)
        if self.load_message:
            print(self.load_message)
            print(LINE)

    def show_menu(self):
        print()
        for number, (label, _) in enumerate(self.menu_items, start=1):
            print(f"{number}. {label}")
        print(LINE)

    def run(self):
        """메인 루프: 메뉴 출력 → 선택 → 기능 실행을 종료할 때까지 반복."""
        self.print_banner()
        try:
            while True:
                self.show_menu()
                choice = read_number("선택: ", 1, len(self.menu_items))
                label, action = self.menu_items[choice - 1]
                if action is None:
                    break
                print()
                action()
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C 또는 입력 스트림 종료(Ctrl+D / 파이프 끝)
            # 진행 중이던 풀이·추가 입력은 버리고, 저장된 데이터는 지킨 채 종료한다.
            print("\n\n⚠️ 입력이 중단되었습니다. 데이터를 저장하고 안전하게 종료합니다.")
        self.save_state()
        print("👋 프로그램을 종료합니다. 다음에 또 만나요!")

    # ------------------------------------------------------------- 저장/불러오기
    def load_state(self):
        """state.json을 불러온다. 없거나 손상되면 기본 퀴즈로 시작한다."""
        try:
            data = self.storage.load()
        except FileNotFoundError:
            self._reset_to_default()
            self.load_message = "🆕 저장된 데이터가 없어 기본 퀴즈로 시작합니다."
            self.save_state()
            return
        except StateFileError as error:
            backup_path = self.storage.backup_broken_file()
            self._reset_to_default()
            self.load_message = f"⚠️ 데이터 파일이 손상되어 기본 퀴즈로 복구했습니다. ({error})"
            if backup_path:
                self.load_message += f"\n   손상된 파일은 {os.path.basename(backup_path)}로 백업했습니다."
            self.save_state()
            return

        self.quizzes = data["quizzes"]
        self.best_score = data["best_score"]
        self.best_correct = data["best_correct"]
        self.best_total = data["best_total"]
        best_text = "없음" if self.best_score is None else f"{self.best_score}점"
        self.load_message = (
            f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {best_text})"
        )

    def save_state(self):
        """현재 상태를 state.json에 저장한다. 실패해도 프로그램은 계속 동작한다."""
        try:
            self.storage.save(self.quizzes, self.best_score, self.best_correct, self.best_total)
            return True
        except OSError as error:
            print(f"⚠️ 데이터를 저장하지 못했습니다: {error}")
            return False

    def _reset_to_default(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.best_correct = 0
        self.best_total = 0

    # ------------------------------------------------------------------ 기능
    def play_quiz(self):
        """저장된 퀴즈를 순서대로 출제하고 결과를 보여준다."""
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다. 먼저 '퀴즈 추가'로 퀴즈를 만들어 주세요.")
            return

        total = read_number(
            f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ", 1, len(self.quizzes)
        )
        # random.sample: 원본 리스트는 그대로 두고, 겹치지 않게 total개를 무작위 순서로 뽑는다.
        selected = random.sample(self.quizzes, total)

        print()
        print(f"📝 퀴즈를 시작합니다! (총 {total}문제, 랜덤 출제)")

        print(f"💡 힌트가 있는 문제는 'h'를 입력하면 힌트를 볼 수 있습니다. "
              f"(힌트 사용 후 정답 시 {int(HINT_CREDIT * 100)}%만 인정)")

        correct = 0
        hints_used = 0
        earned = 0.0  # 문제당 1점, 힌트 사용 후 정답이면 HINT_CREDIT점
        for number, quiz in enumerate(selected, start=1):
            print()
            print(SUB_LINE)
            quiz.display(number)
            print()
            used_hint = False
            while True:
                user_answer = self.read_answer(quiz, allow_hint=not used_hint)
                if user_answer == "hint":
                    used_hint = True
                    hints_used += 1
                    print(f"💡 힌트: {quiz.hint}")
                    continue
                break

            if quiz.is_correct(user_answer):
                correct += 1
                earned += HINT_CREDIT if used_hint else 1
                print("✅ 정답입니다!" + (" (힌트 사용으로 부분 점수)" if used_hint else ""))
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer_text()} 입니다.")

        score = round(earned / total * 100)
        print()
        print(LINE)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        if hints_used:
            print(f"💡 힌트 {hints_used}회 사용 (힌트 없이 맞혔다면 {round(correct / total * 100)}점)")
        if self.update_best_score(score, correct, total):
            print("🎉 새로운 최고 점수입니다!")
            self.save_state()
        print(LINE)

    def read_answer(self, quiz, allow_hint):
        """정답 번호(1~4)를 입력받는다. 힌트를 쓸 수 있으면 'h'도 허용하고 'hint'를 돌려준다."""
        maximum = len(quiz.choices)
        can_hint = allow_hint and quiz.has_hint()
        prompt = f"정답 입력 (1-{maximum}{', 힌트: h' if can_hint else ''}): "
        guide = f"1-{maximum} 사이의 숫자를 입력하세요."
        while True:
            raw = input(prompt).strip()
            if raw.lower() == "h":
                if can_hint:
                    return "hint"
                if not quiz.has_hint():
                    print("⚠️ 이 문제에는 힌트가 없습니다.")
                else:
                    print("⚠️ 이미 힌트를 확인했습니다.")
                continue
            if not raw:
                print(f"⚠️ 빈 입력입니다. {guide}")
                continue
            try:
                number = int(raw)
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. {guide}")
                continue
            if not 1 <= number <= maximum:
                print(f"⚠️ 잘못된 입력입니다. {guide}")
                continue
            return number

    def update_best_score(self, score, correct, total):
        """이번 점수가 최고 점수보다 높으면 갱신하고 True를 돌려준다."""
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.best_correct = correct
            self.best_total = total
            return True
        return False

    def add_quiz(self):
        """문제, 선택지 4개, 정답 번호를 입력받아 새 퀴즈를 등록한다."""
        print("📌 새로운 퀴즈를 추가합니다.")
        print()
        question = read_text("문제를 입력하세요: ")
        choices = [read_text(f"선택지 {i}: ") for i in range(1, CHOICE_COUNT + 1)]
        answer = read_number(f"정답 번호 (1-{CHOICE_COUNT}): ", 1, CHOICE_COUNT)
        # 힌트는 선택 항목이라 빈 입력(Enter)을 허용한다.
        hint = input("힌트 (없으면 Enter): ").strip()

        self.quizzes.append(Quiz(question, choices, answer, hint))
        self.save_state()
        print()
        print("✅ 퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        """등록된 퀴즈의 문제 목록을 번호와 함께 출력한다."""
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다.")
            return

        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print()
        print(SUB_LINE)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print(SUB_LINE)

    def delete_quiz(self):
        """번호를 골라 퀴즈를 삭제하고 파일에 반영한다. 0을 입력하면 취소."""
        if not self.quizzes:
            print("📭 삭제할 퀴즈가 없습니다.")
            return

        self.list_quizzes()
        index = read_number(
            f"삭제할 퀴즈 번호 (1-{len(self.quizzes)}, 취소: 0): ", 0, len(self.quizzes)
        )
        if index == 0:
            print("↩️ 삭제를 취소했습니다.")
            return

        target = self.quizzes[index - 1]
        if not read_yes_no(f"'{target.question}' 퀴즈를 삭제할까요? (y/n): "):
            print("↩️ 삭제를 취소했습니다.")
            return

        del self.quizzes[index - 1]
        self.save_state()
        print(f"🗑️ 퀴즈가 삭제되었습니다. (남은 퀴즈 {len(self.quizzes)}개)")

    def show_best_score(self):
        """지금까지의 최고 점수를 보여준다."""
        if self.best_score is None:
            print("📭 아직 퀴즈를 풀지 않았습니다. '퀴즈 풀기'로 도전해 보세요!")
            return
        print(
            f"🏆 최고 점수: {self.best_score}점 "
            f"({self.best_total}문제 중 {self.best_correct}문제 정답)"
        )
