# 🎯 나만의 퀴즈 게임

터미널(콘솔)에서 동작하는 4지선다 퀴즈 게임입니다.
메뉴에서 번호를 골라 퀴즈를 풀고, 직접 퀴즈를 추가하고, 최고 점수를 확인할 수 있습니다.
퀴즈와 점수는 `state.json`에 저장되어 프로그램을 껐다 켜도 그대로 유지됩니다.

## 1. 프로젝트 개요

| 항목 | 내용 |
| --- | --- |
| 언어 | Python 3.10 이상 (외부 라이브러리 없음, 표준 라이브러리만 사용) |
| 형태 | 콘솔 프로그램 (`input()` / `print()` 기반) |
| 구조 | `Quiz`, `QuizGame`, `StateStorage` 3개 클래스로 역할 분리 |
| 데이터 | 프로젝트 루트의 `state.json` (UTF-8) |

## 2. 퀴즈 주제와 선정 이유

**주제: 개발 입문 상식 (CLI · Git · Python · Docker)**

입학 연수에서 처음 배우는 터미널 명령어, Git 명령어, Python 문법은 직접 여러 번 써 봐야 손에 익습니다.
퀴즈 게임을 만드는 과정 자체가 Python 복습이고, 완성된 게임으로 Git/CLI 명령어를 반복 학습할 수 있어
"만들면서 공부하고, 만든 걸로 또 공부하는" 주제로 골랐습니다. 단답형 시험 대비에도 그대로 쓸 수 있습니다.

## 3. 실행 방법

```bash
# 1) 저장소 복제
git clone https://github.com/ilililililil4319/E1-2.git
cd E1-2

# 2) Python 버전 확인 (3.10 이상)
python --version        # macOS/Linux에서는 python3 --version

# 3) 실행
python main.py          # 또는 python3 main.py
```

- 처음 실행하면 `state.json`이 없으므로 기본 퀴즈 7개로 시작하고, 파일이 자동 생성됩니다.
- 종료는 메뉴의 `종료`를 선택하거나 `Ctrl+C`를 눌러도 저장 후 안전하게 종료됩니다.

## 4. 기능 목록

| 메뉴 | 기능 |
| --- | --- |
| 1. 퀴즈 풀기 | 등록된 퀴즈를 출제 → 정답 번호 입력 → 정답/오답 표시 → 최종 점수(100점 만점) 표시 |
| 2. 퀴즈 추가 | 문제, 선택지 4개, 정답 번호(1~4)를 입력해 새 퀴즈 등록 후 즉시 저장 |
| 3. 퀴즈 목록 | 등록된 퀴즈의 문제 목록 출력 |
| 4. 점수 확인 | 최고 점수와 그때의 정답 수 출력 (풀이 기록이 없으면 안내) |
| 5. 종료 | 데이터 저장 후 종료 |

### 입력/예외 처리

- 입력 앞뒤 공백 제거 (`" 1 "` → `1`)
- 빈 입력, 숫자가 아닌 입력(`abc`), 범위 밖 숫자(메뉴 `9`, 정답 `0`) → 안내 후 다시 입력
- `Ctrl+C`(KeyboardInterrupt), 입력 끝(EOFError) → 안내 메시지 출력 후 저장하고 정상 종료
- `state.json`이 없으면 기본 퀴즈 사용
- `state.json`이 손상되면 `state.json.bak`으로 백업하고 기본 퀴즈로 복구

## 5. 파일 구조

```
E1-2/
├── main.py              # 프로그램 시작점, state.json 경로 결정
├── quiz.py              # Quiz 클래스: 퀴즈 1개 (출력, 정답 확인, dict 변환)
├── quiz_game.py         # QuizGame 클래스: 메뉴, 풀기/추가/목록/점수, 저장 호출
├── storage.py           # StateStorage 클래스: state.json 읽기/쓰기, 손상 처리
├── input_utils.py       # 공통 입력 함수 (숫자/문자열/y·n 입력 검증)
├── default_quizzes.py   # 기본 퀴즈 데이터
├── docs/screenshots/    # 실행 화면 캡처
├── .gitignore
└── README.md
```

## 6. 데이터 파일 설명 (`state.json`)

- **경로**: 프로젝트 루트 (`main.py`와 같은 폴더). 어느 위치에서 실행해도 이 경로를 사용합니다.
- **역할**: 퀴즈 목록과 최고 점수를 저장해 프로그램을 다시 실행해도 데이터를 유지합니다.
- **인코딩**: UTF-8 (`ensure_ascii=False`로 한글을 그대로 저장)
- **Git 관리**: 개인 실행 데이터이므로 `.gitignore`로 제외합니다.

```json
{
  "quizzes": [
    {
      "question": "현재 작업 중인 디렉터리의 절대 경로를 출력하는 명령어는?",
      "choices": ["ls", "cd", "pwd", "whoami"],
      "answer": 3
    }
  ],
  "best_score": 86,
  "best_correct": 6,
  "best_total": 7
}
```

| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `quizzes` | list | 퀴즈 목록 |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list[str] | 선택지 4개 |
| `quizzes[].answer` | int | 정답 번호 (1~4) |
| `best_score` | int \| null | 최고 점수(0~100). 아직 안 풀었으면 `null` |
| `best_correct` | int | 최고 점수 때 맞힌 문제 수 |
| `best_total` | int | 최고 점수 때 푼 문제 수 |
