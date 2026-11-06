"""게임 전체(퀴즈 목록, 점수, 메뉴 흐름)를 관리하는 QuizGame 클래스."""

from default_quizzes import create_default_quizzes
from input_utils import read_number, read_text
from quiz import CHOICE_COUNT, Quiz

LINE = "=" * 40
SUB_LINE = "-" * 40


class QuizGame:
    """퀴즈 목록과 최고 점수를 가지고 메뉴를 진행하는 게임 관리자."""

    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None  # 아직 한 번도 풀지 않았으면 None

        # (메뉴 이름, 실행할 메서드). 메서드가 None이면 종료
        self.menu_items = [
            ("퀴즈 풀기", self.play_quiz),
            ("퀴즈 추가", self.add_quiz),
            ("퀴즈 목록", self.list_quizzes),
            ("점수 확인", self.show_best_score),
            ("종료", None),
        ]

    # ------------------------------------------------------------------ 메뉴
    def print_banner(self):
        print(LINE)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print(LINE)

    def show_menu(self):
        print()
        for number, (label, _) in enumerate(self.menu_items, start=1):
            print(f"{number}. {label}")
        print(LINE)

    def run(self):
        """메인 루프: 메뉴 출력 → 선택 → 기능 실행을 종료할 때까지 반복."""
        self.print_banner()
        while True:
            self.show_menu()
            choice = read_number("선택: ", 1, len(self.menu_items))
            label, action = self.menu_items[choice - 1]
            if action is None:
                break
            print()
            action()
        print("👋 프로그램을 종료합니다. 다음에 또 만나요!")

    # ------------------------------------------------------------------ 기능
    def play_quiz(self):
        """저장된 퀴즈를 순서대로 출제하고 결과를 보여준다."""
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다. 먼저 '퀴즈 추가'로 퀴즈를 만들어 주세요.")
            return

        total = len(self.quizzes)
        print(f"📝 퀴즈를 시작합니다! (총 {total}문제)")

        correct = 0
        for number, quiz in enumerate(self.quizzes, start=1):
            print()
            print(SUB_LINE)
            quiz.display(number)
            print()
            user_answer = read_number("정답 입력: ", 1, len(quiz.choices))
            if quiz.is_correct(user_answer):
                correct += 1
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer_text()} 입니다.")

        score = round(correct / total * 100)
        print()
        print(LINE)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        print(LINE)

    def add_quiz(self):
        """문제, 선택지 4개, 정답 번호를 입력받아 새 퀴즈를 등록한다."""
        print("📌 새로운 퀴즈를 추가합니다.")
        print()
        question = read_text("문제를 입력하세요: ")
        choices = [read_text(f"선택지 {i}: ") for i in range(1, CHOICE_COUNT + 1)]
        answer = read_number(f"정답 번호 (1-{CHOICE_COUNT}): ", 1, CHOICE_COUNT)

        self.quizzes.append(Quiz(question, choices, answer))
        print()
        print("✅ 퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        print("🚧 준비 중인 기능입니다.")

    def show_best_score(self):
        print("🚧 준비 중인 기능입니다.")
