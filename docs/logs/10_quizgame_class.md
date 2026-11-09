# 10. QuizGame 클래스와 코드 구조

> 이 파일은 `scripts/10_quizgame_class.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:02:34 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

## 클래스 목록 (요구: 2개 이상)

```console
$ grep -n '^class ' app/*.py
app/quiz.py:6:class Quiz:
app/quiz_game.py:17:class QuizGame:
app/storage.py:11:class StateFileError(Exception):
app/storage.py:15:class StateStorage:
```
- ✅ 클래스가 2개 이상

## QuizGame 메서드 (기능별 분리)

```console
$ grep -n '    def ' app/quiz_game.py
20:    def __init__(self, storage):
41:    def print_banner(self):
49:    def show_menu(self):
55:    def run(self):
75:    def load_state(self):
103:    def save_state(self):
114:    def _reset_to_default(self):
122:    def play_quiz(self):
177:    def read_answer(self, quiz, allow_hint):
206:    def record_history(self, total, correct, hints_used, score):
216:    def update_best_score(self, score, correct, total):
225:    def add_quiz(self):
240:    def list_quizzes(self):
253:    def delete_quiz(self):
276:    def show_best_score(self):
286:    def show_history(self, limit=10):
```

## QuizGame 속성

```console
$ grep -n 'self\.[a-z_]* = ' app/quiz_game.py | head -12
21:        self.storage = storage
22:        self.quizzes = []
23:        self.best_score = None  # 아직 한 번도 풀지 않았으면 None
24:        self.best_correct = 0
25:        self.best_total = 0
26:        self.history = []  # 모든 게임 기록 (보너스)
27:        self.load_message = ""
30:        self.menu_items = [
81:            self.load_message = "🆕 저장된 데이터가 없어 기본 퀴즈로 시작합니다."
87:            self.load_message = f"⚠️ 데이터 파일이 손상되어 기본 퀴즈로 복구했습니다. ({error})"
93:        self.quizzes = data["quizzes"]
94:        self.best_score = data["best_score"]
```

## 파일별 줄 수

```console
$ wc -l main.py app/*.py
   33 main.py
    8 app/__init__.py
   57 app/default_quizzes.py
   58 app/input_utils.py
   67 app/quiz.py
  305 app/quiz_game.py
  104 app/storage.py
  632 total
```

---

**결과: 모든 단계 통과 ✅**
