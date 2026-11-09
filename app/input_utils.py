"""공통 입력 처리 함수.

- 입력 앞뒤 공백 제거
- 빈 입력 / 숫자 변환 실패 / 범위 밖 숫자 → 안내 후 재입력
- KeyboardInterrupt(Ctrl+C), EOFError는 여기서 잡지 않고 호출한 쪽(QuizGame.run)으로
  올려 보내서, 한 곳에서 '저장 후 안전 종료'를 처리한다.
- 키보드가 아닌 파이프/파일로 입력이 들어오면(실습 스크립트) 입력한 값을 화면에 다시
  보여 줘서, 로그만 읽어도 "무엇을 입력했는지" 알 수 있게 한다.
"""

import sys


def ask(prompt):
    """input()을 감싼 함수. 모든 입력은 이 함수를 거친다."""
    value = input(prompt)
    if not sys.stdin.isatty():
        print(value)  # 파이프 입력은 화면에 안 보이므로 직접 보여 준다
    return value


def read_text(prompt):
    """비어 있지 않은 문자열을 입력받는다."""
    while True:
        value = ask(prompt).strip()
        if value:
            return value
        print("⚠️ 빈 입력입니다. 내용을 입력하세요.")


def read_number(prompt, minimum, maximum):
    """minimum 이상 maximum 이하의 정수를 입력받는다."""
    guide = f"{minimum}-{maximum} 사이의 숫자를 입력하세요."
    while True:
        raw = ask(prompt).strip()
        if not raw:
            print(f"⚠️ 빈 입력입니다. {guide}")
            continue
        try:
            number = int(raw)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {guide}")
            continue
        if not minimum <= number <= maximum:
            print(f"⚠️ 잘못된 입력입니다. {guide}")
            continue
        return number


def read_yes_no(prompt):
    """y/n을 입력받아 True/False로 돌려준다."""
    while True:
        raw = ask(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("⚠️ y 또는 n을 입력하세요.")
