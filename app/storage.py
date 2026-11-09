"""state.json 파일 저장/불러오기를 담당하는 StateStorage 클래스."""

import json
import os

from .quiz import Quiz

ENCODING = "utf-8"


class StateFileError(Exception):
    """state.json이 손상되어 읽을 수 없을 때 발생시키는 예외."""


class StateStorage:
    """퀴즈 목록과 점수를 JSON 파일 하나(state.json)에 저장하고 불러온다."""

    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)

    def load(self):
        """파일을 읽어 dict로 돌려준다.

        - 파일이 없으면 FileNotFoundError
        - JSON 문법 오류이거나 구조가 틀리면 StateFileError
        """
        try:
            with open(self.path, "r", encoding=ENCODING) as file:
                data = json.load(file)
        except FileNotFoundError:
            raise
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            raise StateFileError(f"JSON 형식 오류: {error}") from error
        except OSError as error:
            raise StateFileError(f"파일 읽기 오류: {error}") from error

        try:
            return self._parse(data)
        except (ValueError, TypeError) as error:
            raise StateFileError(f"데이터 구조 오류: {error}") from error

    def _parse(self, data):
        if not isinstance(data, dict):
            raise ValueError("최상위 데이터가 객체(dict)가 아닙니다.")

        raw_quizzes = data.get("quizzes")
        if not isinstance(raw_quizzes, list):
            raise ValueError("quizzes가 리스트가 아닙니다.")
        quizzes = [Quiz.from_dict(item) for item in raw_quizzes]

        best_score = data.get("best_score")
        if best_score is not None and (
            not isinstance(best_score, int) or isinstance(best_score, bool)
        ):
            raise ValueError("best_score가 정수가 아닙니다.")

        history = data.get("history", [])  # 예전 파일에는 없을 수 있음
        if not isinstance(history, list):
            raise ValueError("history가 리스트가 아닙니다.")
        history = [record for record in history if self._is_valid_record(record)]

        return {
            "quizzes": quizzes,
            "best_score": best_score,
            "best_correct": int(data.get("best_correct", 0)),
            "best_total": int(data.get("best_total", 0)),
            "history": history,
        }

    @staticmethod
    def _is_valid_record(record):
        """기록 1건이 필요한 키를 모두 가지고 있는지 확인한다. (잘못된 기록은 건너뜀)"""
        required = ("played_at", "total", "correct", "hints_used", "score")
        return isinstance(record, dict) and all(key in record for key in required)

    def save(self, quizzes, best_score, best_correct, best_total, history):
        """데이터를 UTF-8 JSON으로 저장한다.

        임시 파일에 먼저 쓴 뒤 os.replace로 바꿔치기해서, 저장 도중
        프로그램이 끊겨도 기존 state.json이 깨지지 않게 한다.
        """
        data = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_score": best_score,
            "best_correct": best_correct,
            "best_total": best_total,
            "history": history,
        }
        temp_path = self.path + ".tmp"
        with open(temp_path, "w", encoding=ENCODING) as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        os.replace(temp_path, self.path)

    def backup_broken_file(self):
        """손상된 파일을 state.json.bak으로 옮겨 두고 백업 경로를 돌려준다."""
        backup_path = self.path + ".bak"
        try:
            os.replace(self.path, backup_path)
            return backup_path
        except OSError:
            return None
