"""프로그램 시작점. 실행: python3 main.py

게임 코드는 app/ 폴더에 있고, 이 파일은 저장 경로를 정한 뒤 게임을 시작하는 역할만 한다.
"""

import os
import random

from app.quiz_game import QuizGame
from app.storage import StateStorage

# 실행 위치(cwd)와 상관없이 항상 프로젝트 루트(이 파일이 있는 폴더)의 state.json을 사용한다.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_STATE_PATH = os.path.join(PROJECT_ROOT, "state.json")


def main():
    # QUIZ_STATE_PATH: 실습 스크립트가 내 실제 기록(state.json)을 건드리지 않도록 다른 파일을 쓰게 할 때 사용
    state_path = os.environ.get("QUIZ_STATE_PATH") or DEFAULT_STATE_PATH

    # QUIZ_SEED: 랜덤 출제 순서를 고정한다. 실습 스크립트를 다시 돌려도 같은 문제 순서가 나와서
    # 정해 둔 답을 넣을 수 있다(재현성). 평소에는 설정하지 않으므로 매번 순서가 바뀐다.
    seed = os.environ.get("QUIZ_SEED")
    if seed is not None:
        random.seed(seed)

    game = QuizGame(StateStorage(state_path))
    game.load_state()
    game.run()


if __name__ == "__main__":
    main()
