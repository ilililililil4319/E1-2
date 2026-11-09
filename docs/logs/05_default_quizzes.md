# 05. 기본 퀴즈 데이터

> 이 파일은 `scripts/05_default_quizzes.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:02:34 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

주제: 개발 입문 상식 (CLI · Git · Python · Docker)

## 기본 퀴즈 목록

```console
$ python3 - <<'PY'
from app.default_quizzes import create_default_quizzes
from app.quiz import Quiz

quizzes = create_default_quizzes()
print('개수:', len(quizzes))
print('모두 Quiz 인스턴스:', all(isinstance(q, Quiz) for q in quizzes))
for number, q in enumerate(quizzes, start=1):
    print(f'[{number}] {q.question} → 정답 {q.answer_text()}')
PY
개수: 7
모두 Quiz 인스턴스: True
[1] 현재 작업 중인 디렉터리의 절대 경로를 출력하는 명령어는? → 정답 3. pwd
[2] Git에서 변경된 파일을 스테이징 영역(Staging Area)에 올리는 명령어는? → 정답 2. git add
[3] 원격 저장소의 변경 사항을 가져와 현재 브랜치에 병합하는 명령어는? → 정답 1. git pull
[4] Python에서 클래스의 인스턴스가 생성될 때 자동으로 호출되는 메서드는? → 정답 4. __init__
[5] Python 표준 라이브러리 중 JSON 파일을 읽고 쓸 때 사용하는 모듈은? → 정답 3. json
[6] 실행 중인 Docker 컨테이너 목록을 확인하는 명령어는? → 정답 2. docker ps
[7] Git에서 새 브랜치를 만들고 동시에 그 브랜치로 이동하는 명령어는? → 정답 3. git checkout -b feat
```
- ✅ 기본 퀴즈 5개 이상

---

**결과: 모든 단계 통과 ✅**
