# 04. Quiz 클래스

> 이 파일은 `scripts/04_quiz_class.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:02:33 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

## 클래스 정의 확인

```console
$ grep -n 'class Quiz\|    def ' app/quiz.py
6:class Quiz:
9:    def __init__(self, question, choices, answer, hint=""):
19:    def has_hint(self):
22:    def display(self, number=None):
31:    def is_correct(self, user_answer):
35:    def answer_text(self):
39:    def to_dict(self):
49:    def from_dict(cls, data):
```

## Quiz 객체 만들어 보기

```console
$ python3 - <<'PY'
from app.quiz import Quiz

q = Quiz('Python의 창시자는?', ['Guido', 'Linus', 'Bjarne', 'James'], 1)
q.display(1)
print()
print('is_correct(1) →', q.is_correct(1))
print('is_correct(3) →', q.is_correct(3))
print('answer_text() →', q.answer_text())
print('to_dict() →', q.to_dict())
PY
[문제 1]
Python의 창시자는?

1. Guido
2. Linus
3. Bjarne
4. James

is_correct(1) → True
is_correct(3) → False
answer_text() → 1. Guido
to_dict() → {'question': 'Python의 창시자는?', 'choices': ['Guido', 'Linus', 'Bjarne', 'James'], 'answer': 1, 'hint': ''}
```

## 잘못된 Quiz는 만들 수 없다 (선택지 3개 → ValueError)

```console
$ python3 -c "from app.quiz import Quiz; Quiz('문제', ['a', 'b', 'c'], 1)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from app.quiz import Quiz; Quiz('문제', ['a', 'b', 'c'], 1)
                               ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~/codyssey/E1-2/app/quiz.py", line 11, in __init__
    raise ValueError(f"선택지는 {CHOICE_COUNT}개여야 합니다.")
ValueError: 선택지는 4개여야 합니다.
[종료 코드: 1]
```
- ✅ 선택지 3개면 ValueError

---

**결과: 모든 단계 통과 ✅**
