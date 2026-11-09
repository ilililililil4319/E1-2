"""실습 스크립트용 도우미: QUIZ_SEED로 게임이 낼 문제 순서를 똑같이 계산해 입력값을 만든다.

사용법: python3 scripts/answers.py <판1> [<판2> ...]
  각 판 = "<문제 수>[모드]"
    7   → 7문제 모두 정답
    7w  → 첫 문제만 오답, 나머지 정답
    7x  → 모두 오답
출력: 판마다 한 줄, 답은 printf에 넣을 수 있게 \\n 으로 이어 붙인다. (예: 3\\n2\\n1)

게임(main.py)과 같은 방식(random.seed → random.sample)을 쓰므로 순서가 정확히 일치한다.
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.default_quizzes import create_default_quizzes  # noqa: E402
from app.storage import StateStorage  # noqa: E402


def load_quizzes():
    path = os.environ.get("QUIZ_STATE_PATH", "")
    if path and os.path.exists(path):
        return StateStorage(path).load()["quizzes"]
    return create_default_quizzes()


def wrong(answer):
    return answer % 4 + 1


def main():
    seed = os.environ.get("QUIZ_SEED")
    if seed is not None:
        random.seed(seed)
    quizzes = load_quizzes()
    for spec in sys.argv[1:]:
        mode = spec[-1] if spec[-1] in "wx" else ""
        count = int(spec.rstrip("wx"))
        selected = random.sample(quizzes, count)
        values = []
        for index, quiz in enumerate(selected):
            if mode == "x" or (mode == "w" and index == 0):
                values.append(wrong(quiz.answer))
            else:
                values.append(quiz.answer)
        print("\\n".join(str(v) for v in values))


if __name__ == "__main__":
    main()
