"""프로그램 시작점. 실행: python main.py"""

import os

from quiz_game import QuizGame
from storage import StateStorage

# 실행 위치(cwd)와 상관없이 항상 프로젝트 루트의 state.json을 사용한다.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(PROJECT_ROOT, "state.json")


def main():
    game = QuizGame(StateStorage(STATE_PATH))
    game.load_state()
    game.run()


if __name__ == "__main__":
    main()
