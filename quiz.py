"""개별 퀴즈 한 개를 표현하는 Quiz 클래스."""

CHOICE_COUNT = 4


class Quiz:
    """문제(question), 선택지 4개(choices), 정답 번호(answer, 1~4), 힌트(hint)를 가진 퀴즈."""

    def __init__(self, question, choices, answer, hint=""):
        if len(choices) != CHOICE_COUNT:
            raise ValueError(f"선택지는 {CHOICE_COUNT}개여야 합니다.")
        if not 1 <= answer <= CHOICE_COUNT:
            raise ValueError(f"정답은 1~{CHOICE_COUNT} 사이의 번호여야 합니다.")
        self.question = question
        self.choices = list(choices)
        self.answer = answer
        self.hint = hint

    def has_hint(self):
        return bool(self.hint)

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

    def to_dict(self):
        """JSON으로 저장할 수 있는 dict로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data):
        """state.json에서 읽은 dict를 Quiz로 변환한다. 형식이 틀리면 ValueError."""
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터가 객체(dict) 형식이 아닙니다.")
        question = data.get("question")
        choices = data.get("choices")
        answer = data.get("answer")

        if not isinstance(question, str) or not question.strip():
            raise ValueError("question이 올바르지 않습니다.")
        if not isinstance(choices, list) or not all(isinstance(c, str) for c in choices):
            raise ValueError("choices가 올바르지 않습니다.")
        # bool은 int의 하위 타입이라 True가 1로 통과하지 않도록 따로 막는다.
        if not isinstance(answer, int) or isinstance(answer, bool):
            raise ValueError("answer가 올바르지 않습니다.")
        hint = data.get("hint", "")  # 힌트는 선택 항목 (예전 파일에는 없을 수 있음)
        if not isinstance(hint, str):
            raise ValueError("hint가 문자열이 아닙니다.")
        return cls(question, choices, answer, hint)
