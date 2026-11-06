"""개별 퀴즈 한 개를 표현하는 Quiz 클래스."""

CHOICE_COUNT = 4


class Quiz:
    """문제(question), 선택지 4개(choices), 정답 번호(answer, 1~4)를 가진 퀴즈."""

    def __init__(self, question, choices, answer):
        if len(choices) != CHOICE_COUNT:
            raise ValueError(f"선택지는 {CHOICE_COUNT}개여야 합니다.")
        if not 1 <= answer <= CHOICE_COUNT:
            raise ValueError(f"정답은 1~{CHOICE_COUNT} 사이의 번호여야 합니다.")
        self.question = question
        self.choices = list(choices)
        self.answer = answer

    def display(self, number=None):
        """문제와 선택지를 화면에 출력한다."""
        title = f"[문제 {number}]" if number is not None else "[문제]"
        print(title)
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답인지 확인한다."""
        return user_answer == self.answer

    def answer_text(self):
        """정답 번호와 내용을 문자열로 돌려준다. 예: '3. 6개'"""
        return f"{self.answer}. {self.choices[self.answer - 1]}"
