"""공통 입력 처리 함수.

- 입력 앞뒤 공백 제거
- 빈 입력 / 숫자 변환 실패 / 범위 밖 숫자 → 안내 후 재입력
- KeyboardInterrupt(Ctrl+C), EOFError는 여기서 잡지 않고 호출한 쪽(QuizGame.run)으로
  올려 보내서, 한 곳에서 '저장 후 안전 종료'를 처리한다.
"""


def read_text(prompt):
    """비어 있지 않은 문자열을 입력받는다."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠️ 빈 입력입니다. 내용을 입력하세요.")


def read_number(prompt, minimum, maximum):
    """minimum 이상 maximum 이하의 정수를 입력받는다."""
    guide = f"{minimum}-{maximum} 사이의 숫자를 입력하세요."
    while True:
        raw = input(prompt).strip()
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
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("⚠️ y 또는 n을 입력하세요.")
