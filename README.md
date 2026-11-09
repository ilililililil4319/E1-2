# 🎯 나만의 퀴즈 게임 (E1-2)

터미널에서 동작하는 4지선다 퀴즈 게임을 Python 클래스로 만들고, `state.json`으로 데이터를 유지하며, Git 브랜치·병합·clone·pull로 이력을 관리한 미션 결과물입니다.

- GitHub: https://github.com/ilililililil4319/E1-2
- 미션: 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기 — 올인원 1기 입학 연수 E1-2
- 실행 로그: [docs/logs/](docs/logs/)
- 스크린샷: [docs/screenshots/](docs/screenshots/)
- 환경 세팅: [docs/SETUP.md](docs/SETUP.md)

![메뉴 화면](docs/screenshots/menu.png)

## 목차

1. [프로젝트 소개](#1-프로젝트-소개)
2. [핵심 질문](#2-핵심-질문)
3. [프로젝트 개요 및 산출물 구성](#3-프로젝트-개요-및-산출물-구성)
4. [폴더 구조 (파일 구조)](#4-폴더-구조-파일-구조)
5. [용어 설명 (초보자를 위한 참고)](#5-용어-설명-초보자를-위한-참고)
6. [기술 스택 및 실행 환경](#6-기술-스택-및-실행-환경)
7. [사용 자료·이미지 및 출처](#7-사용-자료이미지-및-출처)
8. [검증 방법 및 핵심 개념 요약](#8-검증-방법-및-핵심-개념-요약)
9. [전체 작업 순서 (STEP)](#9-전체-작업-순서-step)
10. [작업 흐름도](#10-작업-흐름도)
11. [구조도](#11-구조도)
12. [핵심 실습 결과](#12-핵심-실습-결과)
13. [보너스 과제](#13-보너스-과제)
14. [로컬 실행 방법](#14-로컬-실행-방법)
15. [환경 변수 및 설정 (데이터 파일 설명)](#15-환경-변수-및-설정-데이터-파일-설명)
16. [실습 중 발생한 오류와 해결](#16-실습-중-발생한-오류와-해결)
17. [AI(Claude) 사용 로그 요약](#17-aiclaude-사용-로그-요약)
18. [기능요구사항 대비 결과](#18-기능요구사항-대비-결과)
19. [결론 및 한계점](#19-결론-및-한계점)
20. [보안 유의사항](#20-보안-유의사항)
21. [출처 및 라이선스 유의사항](#21-출처-및-라이선스-유의사항)
22. [기타](#22-기타)

---

## 1. 프로젝트 소개

| 항목 | 내용 |
| --- | --- |
| 미션 목표 | 문법을 "아는 것"을 넘어,<br>입력→처리→출력→저장이 이어진 프로그램 하나를 끝까지 완성한다 |
| 핵심 도구 | Python 3 (표준 라이브러리만), Git, GitHub |
| 핵심 가치 | 역할별 클래스 분리, 어떤 입력에도 죽지 않는 프로그램,<br>껐다 켜도 남는 데이터, 기능 단위로 남긴 Git 이력 |

### 퀴즈 주제와 선정 이유

**주제: 개발 입문 상식 (CLI · Git · Python · Docker)**

입학 연수에서 처음 배우는 터미널 명령어, Git 명령어, Python 문법은 여러 번 직접 써 봐야 손에 익습니다.
퀴즈 게임을 만드는 과정 자체가 Python 복습이고, 완성된 게임으로 Git/CLI 명령어를 반복 학습할 수 있어서
"만들면서 공부하고, 만든 것으로 또 공부하는" 주제로 골랐습니다.

### 기능 목록

| 메뉴 | 기능 |
| --- | --- |
| 1. 퀴즈 풀기 | 문제 수 선택 → 랜덤 출제 → 정답 번호 입력(`h`로 힌트)<br>→ 정답/오답 표시 → 최종 점수(100점 만점), 최고 점수 갱신 |
| 2. 퀴즈 추가 | 문제, 선택지 4개, 정답 번호(1~4), 힌트(선택) 입력 → 즉시 저장 |
| 3. 퀴즈 목록 | 등록된 퀴즈의 문제 목록 |
| 4. 점수 확인 | 최고 점수와 그때의 정답 수 (아직 안 풀었으면 안내) |
| 5. 퀴즈 삭제 | 번호 선택 → y/n 확인 → 삭제 후 즉시 저장 (0은 취소) |
| 6. 게임 기록 | 최근 10회 기록(날짜/시간, 문제 수, 정답 수, 힌트, 점수)과 평균 점수 |
| 7. 종료 | 저장 후 종료 |

## 2. 핵심 질문

미션의 "스스로 설명할 수 있어야 한다" 항목과 한 줄 답입니다.

**Python 기초**

- 변수가 무엇이고 왜 쓰는가?
  → 값에 이름표를 붙여 두는 상자. 같은 값을 여러 곳에서 쓰고 바꿀 때 이름으로 부르기 위해 쓴다 (`correct += 1`).
- `int`, `str`, `bool`, `list`, `dict`의 차이는?
  → 정수 / 글자 / 참·거짓 / 순서 있는 목록 / 이름표(key)로 찾는 묶음. 퀴즈 1개는 `dict`, 선택지는 `list`, 정답 번호는 `int`로 저장했다.
- `if/elif/else`로 조건에 따라 다르게 동작하려면?
  → 정답이면 "정답", 아니면 "오답"을 출력하는 `if quiz.is_correct(...) / else` 구조로 썼다.
- `for`와 `while`의 차이와 선택 기준은?
  → `for`는 횟수가 정해진 반복(문제 목록 돌기), `while`은 조건이 만족될 때까지 반복(올바른 입력이 올 때까지 다시 묻기).
- 함수의 매개변수와 반환값은?
  → `read_number(prompt, minimum, maximum)`처럼 필요한 값을 받아(매개변수) 검증된 숫자를 돌려준다(반환값).

**클래스와 객체**

- 클래스가 무엇이고 왜 쓰는가?
  → 데이터(속성)와 그 데이터를 다루는 기능(메서드)을 한 묶음으로 만드는 설계도. 퀴즈·게임·저장의 책임을 나누려고 썼다.
- `__init__`과 `self`의 역할은?
  → `__init__`은 객체가 만들어질 때 자동 실행되어 속성을 채우고, `self`는 "지금 만들어지는(사용 중인) 그 객체 자신"을 가리킨다.
- 속성과 메서드는?
  → `Quiz.question/choices/answer`가 속성, `display()/is_correct()`가 메서드.

**파일 입출력**

- 파일을 열고, 읽고, 쓰는 과정은?
  → `with open(경로, 모드, encoding="utf-8") as f:`로 열고 `json.load(f)` / `json.dump(data, f)`로 읽고 쓴다. `with`가 끝나면 자동으로 닫힌다.
- JSON이 무엇이고 왜 쓰는가?
  → `{"키": 값}` 형태의 글자 파일. 사람이 읽을 수 있고 Python `dict/list`와 1:1로 바뀌어 저장에 편하다.
- `try/except`로 오류 처리는?
  → `int("abc")`의 `ValueError`, 손상된 파일의 `JSONDecodeError`, `Ctrl+C`의 `KeyboardInterrupt`를 잡아 안내 후 계속/안전 종료한다.

**Git 기초**

- Git이 무엇이고 왜 필요한가?
  → 파일의 변경 이력을 저장하는 도구. 언제 무엇을 왜 바꿨는지 남기고, 되돌리고, 나눠서 작업한 뒤 합칠 수 있다.
- `init/add/commit/push/pull/checkout/clone`은?
  → 저장소 만들기 / 커밋할 파일 담기 / 이력 저장 / 원격에 올리기 / 원격에서 받아 합치기 / 브랜치 이동 / 원격 저장소 통째로 복제.
- 브랜치 생성과 병합은?
  → `git checkout -b feature/play-quiz`로 갈래를 만들어 작업하고 `git checkout main` → `git merge --no-ff feature/play-quiz`로 합쳤다.
- clone 하고 pull로 변경을 가져오기는?
  → 복제본(`E1-2-copy`)에서 README를 고쳐 push하고, 원래 폴더에서 `git pull`로 받아 반영을 확인했다 ([13_clone_pull.md](docs/logs/13_clone_pull.md)).

## 3. 프로젝트 개요 및 산출물 구성

| 최종 결과물 | 저장소 위치 |
| --- | --- |
| 퀴즈 게임 실행 파일 | [main.py](main.py) |
| 게임 코드 (클래스 3개) | [app/](app/) |
| 데이터 파일 | `state.json` (실행 시 루트에 자동 생성, Git 제외) |
| 실습 스크립트 | [scripts/](scripts/) |
| 실행 로그 (명령 + 출력) | [docs/logs/](docs/logs/) |
| 스크린샷 | [docs/screenshots/](docs/screenshots/) |
| 환경 세팅 문서 | [docs/SETUP.md](docs/SETUP.md) |

## 4. 폴더 구조 (파일 구조)

```
E1-2/
├── README.md              # 기술 문서 (이 파일)
├── .gitignore             # state.json, .demo/, .env, 키 파일, 캐시 제외
├── main.py                # 시작점: 저장 경로 결정 → 게임 시작
├── app/                   # 게임 코드
│   ├── __init__.py
│   ├── quiz.py            # Quiz: 퀴즈 1개 (출력, 정답 확인, 힌트, dict 변환)
│   ├── quiz_game.py       # QuizGame: 메뉴, 풀기/추가/목록/점수/삭제/기록
│   ├── storage.py         # StateStorage: state.json 읽기/쓰기, 손상 처리
│   ├── input_utils.py     # 공통 입력 함수 (공백·빈 입력·숫자·범위 검증)
│   └── default_quizzes.py # 기본 퀴즈 7개
├── scripts/
│   ├── lib.sh             # run/try/check/note/section, 마스킹, 실패 시 [중단]
│   ├── answers.py         # 고정 시드 기준 정답 입력값 계산 (스크립트용)
│   ├── 00_env.sh          # 실행 환경
│   ├── 01_git_setup.sh ~ 18_git_history.sh   # 요구사항 하나당 스크립트 하나
│   └── run_all.sh         # 전부 순서대로 실행
└── docs/
    ├── SETUP.md           # 환경 세팅 (Windows WSL2 기준)
    ├── logs/              # 스크립트 출력 (자동)
    └── screenshots/       # 캡처
```

## 5. 용어 설명 (초보자를 위한 참고)

이 미션에서 새로 쓴 용어와 명령을 정리했습니다. E1-1에서 설명한 기본 명령(`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `cp`, `mv`, `rm`, `chmod`, `git` $`\color{red}{\vee}`$ `add`, `git` $`\color{red}{\vee}`$ `commit`, `git` $`\color{red}{\vee}`$ `push`, `git` $`\color{red}{\vee}`$ `clone` 등)은 [E1-1 README 5장](https://github.com/ilililililil4319/E1-1#5-용어-설명-초보자를-위한-참고)에 있습니다.

> **읽는 법**: `[` $`\color{red}{\vee}`$ `]` 안은 소리 내어 읽는 방법
> **띄어쓰기 표시**: 명령 사이의 붉은 $`\color{red}{\vee}`$ 는 **띄어쓰기 한 칸**입니다. 예) `git` $`\color{red}{\vee}`$ `add` $`\color{red}{\vee}`$ `.` = 깃 / 띄어쓰기 / 애드 / 띄어쓰기 / 점

### 5-1. Python

| 용어 / 코드 [읽는 법] | 뜻 |
| --- | --- |
| 클래스 / 객체<br>[클래스 / 오브젝트] | 설계도 / 설계도로 만든 실제 물건 |
| 속성 / 메서드<br>[애트리뷰트 / 메서드] | 객체가 가진 값 / 객체가 할 수 있는 일 |
| `__init__`<br>[던더 이닛] | 객체가 만들어질 때 자동으로 실행되는 준비 함수 |
| `self`<br>[셀프] | 객체 자기 자신 |
| 예외 (Exception)<br>[익셉션] | 실행 중 생긴 문제 |
| `try` / `except`<br>[트라이 / 익셉트] | 예외를 잡아서 처리하는 안전망 |
| `ValueError`<br>[밸류 에러] | 값이 잘못됨 (`int("abc")`) |
| `KeyboardInterrupt`<br>[키보드 인터럽트] | Ctrl+C로 중단함 |
| `EOFError`<br>[이오에프 에러] | 입력이 끝남 (Ctrl+D, 파이프 입력 끝) |
| JSON<br>[제이슨] | 사람이 읽을 수 있는 데이터 저장 형식 (`{"키":` $`\color{red}{\vee}`$ `값}`) |
| `json.load` / `json.dump`<br>[제이슨 점 로드 / 덤프] | 파일에서 읽기 / 파일에 쓰기 |
| UTF-8<br>[유티에프 팔] | 한글을 포함한 전 세계 글자를 저장하는 방식 |
| 영속성 | 프로그램을 껐다 켜도 데이터가 남는 것 |
| `random.sample`<br>[랜덤 점 샘플] | 원본은 그대로 두고 겹치지 않게 n개 뽑기 |
| `input().strip()`<br>[인풋 점 스트립] | 입력받은 글자의 앞뒤 공백 지우기 |
| `if` $`\color{red}{\vee}`$ `__name__` $`\color{red}{\vee}`$ `==` $`\color{red}{\vee}`$ `"__main__":`<br>[이프 던더 네임 … 던더 메인] | 이 파일을 직접 실행할 때만 아래 코드 실행 |

### 5-2. 터미널 (E1-1에 없던 명령)

| 명령 [읽는 법] | 뜻 |
| --- | --- |
| `head` $`\color{red}{\vee}`$ `-n` $`\color{red}{\vee}`$ `5` $`\color{red}{\vee}`$ `state.json`<br>[헤드 대시 엔] | 파일 앞부분만 보기 (기본 10줄) |
| `tail` $`\color{red}{\vee}`$ `-f` $`\color{red}{\vee}`$ `app.log`<br>[테일 대시 에프] | 파일 뒷부분 보기<br>`-f`는 새로 추가되는 줄을 계속 보여 줌 |
| `grep` $`\color{red}{\vee}`$ `-n` $`\color{red}{\vee}`$ `"def"` $`\color{red}{\vee}`$ `app/quiz_game.py`<br>[그렙 대시 엔] | 파일에서 글자가 있는 줄 찾기<br>`-n`은 줄 번호 표시 |
| `find` $`\color{red}{\vee}`$ `.` $`\color{red}{\vee}`$ `-name` $`\color{red}{\vee}`$ `"*.py"`<br>[파인드 점 대시 네임] | 이름 조건으로 파일 찾기 |
| `wc` $`\color{red}{\vee}`$ `-l` $`\color{red}{\vee}`$ `main.py`<br>[더블유씨(워드 카운트) 대시 엘] | 줄 수 세기 |
| `echo` $`\color{red}{\vee}`$ `"state.json"` $`\color{red}{\vee}`$ `>>` $`\color{red}{\vee}`$ `.gitignore`<br>[에코 … 어펜드] | 글자를 파일 끝에 이어 쓰기 |
| `printf` $`\color{red}{\vee}`$ `'1\n7\n'`<br>[프린트에프] | 줄바꿈(`\n`)이 섞인 글자 만들기<br>파이프로 입력을 보낼 때 사용 |
| `echo` $`\color{red}{\vee}`$ `$?`<br>[에코 달러 물음표] | 바로 앞 명령의 종료 코드 (0 = 성공) |
| `which` $`\color{red}{\vee}`$ `python3`<br>[위치 파이썬쓰리] | 명령 실행 파일이 있는 위치 |
| `python3` $`\color{red}{\vee}`$ `main.py`<br>[파이썬쓰리 메인 점 파이] | 파이썬 파일 실행 |
| `python3` $`\color{red}{\vee}`$ `-m` $`\color{red}{\vee}`$ `json.tool` $`\color{red}{\vee}`$ `state.json`<br>[파이썬쓰리 대시 엠 제이슨 점 툴] | JSON을 보기 좋게 출력하고 문법 검사 |
| `python3` $`\color{red}{\vee}`$ `-m` $`\color{red}{\vee}`$ `venv` $`\color{red}{\vee}`$ `.venv`<br>[파이썬쓰리 대시 엠 벤브] | 가상환경 만들기 |
| `source` $`\color{red}{\vee}`$ `.venv/bin/activate`<br>[소스 … 액티베이트] | 가상환경 켜기 (끄기: `deactivate`) |
| `export` $`\color{red}{\vee}`$ `QUIZ_SEED=42`<br>[익스포트] | 환경 변수 설정<br>(이 터미널을 닫을 때까지) |
| `bash` $`\color{red}{\vee}`$ `scripts/run_all.sh`<br>[배시] | 셸 스크립트 실행 |
| `timeout` $`\color{red}{\vee}`$ `-s` $`\color{red}{\vee}`$ `INT` $`\color{red}{\vee}`$ `1` $`\color{red}{\vee}`$ `python3` $`\color{red}{\vee}`$ `main.py`<br>[타임아웃 대시 에스 인트] | 1초 뒤 Ctrl+C와 같은 신호 보내기 |
| `rm` $`\color{red}{\vee}`$ `-rf` $`\color{red}{\vee}`$ `.demo`<br>[알엠 대시 알에프] | 폴더를 확인 없이 통째로 삭제 |
| `code` $`\color{red}{\vee}`$ `.`<br>[코드 점] | VSCode로 현재 폴더 열기 |
| `clear`<br>[클리어] | 터미널 화면 지우기 |
| 종료 코드<br>[엑시트 코드] | 명령의 성적표. 0이면 성공, 0이 아니면 실패 |

### 5-3. Git (E1-1에 없던 명령)

| 명령 [읽는 법] | 뜻 |
| --- | --- |
| `git` $`\color{red}{\vee}`$ `diff`<br>[깃 디프] | 스테이징 전 변경 내용 보기 |
| `git` $`\color{red}{\vee}`$ `diff` $`\color{red}{\vee}`$ `--staged`<br>[깃 디프 대시대시 스테이지드] | 스테이징한(커밋할) 변경 내용 보기 |
| `git` $`\color{red}{\vee}`$ `commit` $`\color{red}{\vee}`$ `-am` $`\color{red}{\vee}`$ `"메시지"`<br>[깃 커밋 대시 에이엠] | 추적 중인 파일을 add + commit 한 번에 |
| `git` $`\color{red}{\vee}`$ `commit` $`\color{red}{\vee}`$ `--amend`<br>[깃 커밋 대시대시 어멘드] | 직전 커밋 고치기 |
| `git` $`\color{red}{\vee}`$ `restore` $`\color{red}{\vee}`$ `quiz.py`<br>[깃 리스토어] | 수정 내용 버리고 마지막 커밋으로 |
| `git` $`\color{red}{\vee}`$ `restore` $`\color{red}{\vee}`$ `--staged` $`\color{red}{\vee}`$ `state.json`<br>[깃 리스토어 대시대시 스테이지드] | 스테이징만 취소 (파일 내용은 그대로) |
| `git` $`\color{red}{\vee}`$ `rm` $`\color{red}{\vee}`$ `--cached` $`\color{red}{\vee}`$ `state.json`<br>[깃 알엠 대시대시 캐시드] | 파일은 두고 Git 추적만 중지 |
| `git` $`\color{red}{\vee}`$ `log` $`\color{red}{\vee}`$ `--oneline` $`\color{red}{\vee}`$ `--graph`<br>[깃 로그 대시대시 원라인 대시대시 그래프] | 커밋을 한 줄씩 + 브랜치 갈래 그림 |
| `git` $`\color{red}{\vee}`$ `show` $`\color{red}{\vee}`$ `HEAD`<br>[깃 쇼 헤드] | 커밋 하나의 변경 내용 |
| `git` $`\color{red}{\vee}`$ `reflog`<br>[깃 리플로그] | 내 PC에서 한 Git 동작 기록 (clone, pull, checkout) |
| `git` $`\color{red}{\vee}`$ `rev-list` $`\color{red}{\vee}`$ `--count` $`\color{red}{\vee}`$ `HEAD`<br>[깃 레브리스트 대시대시 카운트 헤드] | 커밋 개수 |
| `git` $`\color{red}{\vee}`$ `branch` $`\color{red}{\vee}`$ `-a`<br>[깃 브랜치 대시 에이] | 원격까지 모든 브랜치 목록 |
| `git` $`\color{red}{\vee}`$ `checkout` $`\color{red}{\vee}`$ `-b` $`\color{red}{\vee}`$ `feature/x`<br>[깃 체크아웃 대시 비] | 브랜치를 만들고 바로 이동 |
| `git` $`\color{red}{\vee}`$ `switch` $`\color{red}{\vee}`$ `-c` $`\color{red}{\vee}`$ `feature/x`<br>[깃 스위치 대시 씨] | 위와 같음 (새 문법) |
| `git` $`\color{red}{\vee}`$ `merge` $`\color{red}{\vee}`$ `--no-ff` $`\color{red}{\vee}`$ `feature/x`<br>[깃 머지 대시대시 노 에프에프] | 병합 커밋을 꼭 남기며 병합 |
| `git` $`\color{red}{\vee}`$ `merge` $`\color{red}{\vee}`$ `--abort`<br>[깃 머지 대시대시 어보트] | 충돌 난 병합 취소 |
| `git` $`\color{red}{\vee}`$ `branch` $`\color{red}{\vee}`$ `-d` / `git` $`\color{red}{\vee}`$ `branch` $`\color{red}{\vee}`$ `-D`<br>[대시 디 / 대시 대문자 디] | 병합된 브랜치 삭제 / 강제 삭제 |
| `git` $`\color{red}{\vee}`$ `push` $`\color{red}{\vee}`$ `-u` $`\color{red}{\vee}`$ `origin` $`\color{red}{\vee}`$ `main`<br>[깃 푸시 대시 유 오리진 메인] | 처음 올리면서 추적 관계 설정 |
| `git` $`\color{red}{\vee}`$ `fetch`<br>[깃 페치] | 원격 변경을 가져오기만 (합치지 않음) |
| `git` $`\color{red}{\vee}`$ `remote` $`\color{red}{\vee}`$ `add` $`\color{red}{\vee}`$ `origin` $`\color{red}{\vee}`$ `URL`<br>[깃 리모트 애드 오리진 유알엘] | 원격 저장소 연결 |
| `git` $`\color{red}{\vee}`$ `revert` $`\color{red}{\vee}`$ `a1b2c3d`<br>[깃 리버트] | 커밋을 되돌리는 새 커밋 만들기 |
| `git` $`\color{red}{\vee}`$ `stash` / `git` $`\color{red}{\vee}`$ `stash` $`\color{red}{\vee}`$ `pop`<br>[깃 스태시 / 스태시 팝] | 작업 임시 보관 / 다시 꺼내기 |
| `ssh-keygen` $`\color{red}{\vee}`$ `-t` $`\color{red}{\vee}`$ `ed25519`<br>[에스에스에이치 키젠 대시 티] | SSH 키 만들기 |
| `ssh` $`\color{red}{\vee}`$ `-T` $`\color{red}{\vee}`$ `git@github.com`<br>[에스에스에이치 대시 대문자 티 깃 앳 깃허브 닷컴] | GitHub SSH 연결 확인 |

### 5-4. 헷갈리기 쉬운 명령

| 비교 | 차이 |
| --- | --- |
| `cd`<br>`mv` | `cd`: **내가** 그 폴더로 이동 (파일은 그대로)<br>`mv`: **파일을** 다른 곳으로 옮기거나 이름 바꾸기 |
| `mv`<br>`cp` | `mv`: 옮기기, 원본이 사라짐<br>`cp`: 복사하기, 원본이 남음 |
| `git` $`\color{red}{\vee}`$ `clone`<br>`git` $`\color{red}{\vee}`$ `pull` | clone: GitHub 저장소를 **처음 한 번** 통째로 복사<br>pull: 이미 받은 저장소를 **최신으로** 맞춤 |
| `git` $`\color{red}{\vee}`$ `clone`<br>`cp` $`\color{red}{\vee}`$ `-r` | clone: GitHub → 내 PC (변경 이력까지)<br>`cp` $`\color{red}{\vee}`$ `-r`: 내 PC 안에서 폴더 복사 (이력 없음) |
| `git` $`\color{red}{\vee}`$ `fetch`<br>`git` $`\color{red}{\vee}`$ `pull` | fetch: 받기만 / pull: 받기 + 합치기 |
| GitHub **Code** 버튼<br>HTTPS 주소<br>SSH 주소 | `https://github.com/아이디/E1-2.git`<br>→ 로그인·토큰 필요<br>`git@github.com:아이디/E1-2.git`<br>→ SSH 키를 등록하면 비밀번호 없이 |
| `>`<br>`>>` | 덮어쓰기 / 이어 쓰기 |
| `head`<br>`tail` | 앞부분 / 뒷부분 |
| `cat`<br>`echo` | 파일 **내용** 출력 / 내가 쓴 **글자** 출력 |
| `rm`<br>`rmdir`<br>`rm` $`\color{red}{\vee}`$ `-rf` | 파일 삭제 / 빈 폴더만 삭제 / 폴더를 통째로 확인 없이 |
| `git` $`\color{red}{\vee}`$ `add`<br>`git` $`\color{red}{\vee}`$ `commit` | 담기 / 기록 확정 |
| `git` $`\color{red}{\vee}`$ `restore`<br>`git` $`\color{red}{\vee}`$ `restore` $`\color{red}{\vee}`$ `--staged` | 수정 내용 버리기 / 스테이징만 취소 |
| `git` $`\color{red}{\vee}`$ `reset`<br>`git` $`\color{red}{\vee}`$ `revert` | 기록 되감기 / 되돌리는 새 커밋 |
| `git` $`\color{red}{\vee}`$ `branch` $`\color{red}{\vee}`$ `X`<br>`git` $`\color{red}{\vee}`$ `checkout` $`\color{red}{\vee}`$ `-b` $`\color{red}{\vee}`$ `X` | 만들기만 / 만들고 이동까지 |
| `python`<br>`python3` | Windows는 보통 `python`, 리눅스(WSL)는 `python3` |
| `bash` $`\color{red}{\vee}`$ `a.sh`<br>`source` $`\color{red}{\vee}`$ `a.sh` | 새 셸에서 실행 / 지금 셸에서 실행 (설정이 남음) |
| `json.load`<br>`json.loads` | 파일에서 읽기 / 문자열에서 읽기 |
| `random.shuffle`<br>`random.sample` | 원본을 섞음 / 원본은 두고 n개 뽑기 |

## 6. 기술 스택 및 실행 환경

| 도구 | 버전 | 용도 |
| --- | --- | --- |
| OS | Windows + WSL2<br>Ubuntu 26.04.1 LTS | 실행 환경 |
| Python | 3.14.4<br>(요구: 3.10 이상) | 게임 실행 |
| Git | 2.53.0 | 버전 관리 |
| VSCode (WSL 확장) | - | 편집, 터미널 |
| 외부 라이브러리 | 없음 | 표준 라이브러리만 사용<br>`json`, `os`, `random`,<br>`datetime`, `sys` |

버전 출처: [00_env.md](docs/logs/00_env.md) (집 PC에서 실행)

| VSCode (WSL 연결) | Python 버전 | Git 설정 |
| --- | --- | --- |
| ![VSCode](docs/screenshots/vscode.png) | ![Python](docs/screenshots/python-check.png) | ![Git 설정](docs/screenshots/git-check.png) |

## 7. 사용 자료·이미지 및 출처

| 자료 | 출처 | 비고 |
| --- | --- | --- |
| 퀴즈 문제 7개 | 직접 작성 | CLI·Git·Python·Docker 기초 |
| Python 표준 라이브러리 | [docs.python.org](https://docs.python.org/3/library/) | `json`, `random` 등<br>별도 설치 없음 |
| 스크린샷 | 직접 캡처 | 아이디, 컴퓨터 이름 가림 |

외부 패키지를 쓰지 않으므로 고정할 버전이 없고, Python 3.10 이상이면 같은 결과가 나옵니다.

## 8. 검증 방법 및 핵심 개념 요약

**검증 원칙**

1. 요구사항 하나당 스크립트 하나: `scripts/NN_*.sh`가 명령을 실행하고 명령+출력을 `docs/logs/NN_*.md`에 그대로 남긴다.
2. 결과를 눈으로만 보지 않는다: `check`가 파일 내용·출력 문구를 조건으로 확인해 ✅/❌를 남기고, 실패하면 [중단]한다.
3. 다시 실행해도 같은 결과: 실습 데이터는 `.demo/`에서 매번 새로 만들고, `QUIZ_SEED`로 랜덤 순서를 고정한다.
4. 사람만 할 수 있는 확인(대화형 실행 화면, VSCode, GitHub 화면)은 스크린샷으로 남긴다.

| 핵심 질문 | 확인 결과 | 증거 |
| --- | --- | --- |
| 잘못된 입력에도<br>죽지 않는가 | 공백, abc, 범위 밖, 빈 입력은 재입력<br>Ctrl+C, EOF는 저장 후 종료 코드 0 | [03_input_errors.md](docs/logs/03_input_errors.md) |
| 껐다 켜도<br>데이터가 남는가 | 추가한 퀴즈와 최고 점수가<br>재실행 후에도 유지 | [07_add_quiz.md](docs/logs/07_add_quiz.md)<br>[09_score.md](docs/logs/09_score.md) |
| 파일이 망가지면? | `.bak`으로 백업 후<br>기본 퀴즈로 복구 | [11_state_json.md](docs/logs/11_state_json.md) |
| 클래스로 역할을<br>나눴는가 | `Quiz`, `QuizGame`,<br>`StateStorage` 3개 | [10_quizgame_class.md](docs/logs/10_quizgame_class.md) |
| 브랜치 병합과<br>clone, pull을 했는가 | 브랜치 2개 병합<br>복제본 push → pull 반영 | [13_clone_pull.md](docs/logs/13_clone_pull.md)<br>[18_git_history.md](docs/logs/18_git_history.md) |

## 9. 전체 작업 순서 (STEP)

| STEP | 작업 | 증빙 |
| --- | --- | --- |
| 1 | GitHub 저장소 생성<br>`.gitignore`, README 첫 커밋 | [01_git_setup.md](docs/logs/01_git_setup.md) |
| 2 | `Quiz` 클래스 → 기본 퀴즈 데이터<br>→ 메뉴, 입력 처리 | [04](docs/logs/04_quiz_class.md), [05](docs/logs/05_default_quizzes.md),<br>[02](docs/logs/02_menu.md), [03](docs/logs/03_input_errors.md) |
| 3 | `feature/play-quiz` 브랜치에서<br>퀴즈 풀기 → main 병합 | [06_play.md](docs/logs/06_play.md) |
| 4 | 퀴즈 추가 → 목록 → 점수 | [07](docs/logs/07_add_quiz.md), [08](docs/logs/08_list.md), [09](docs/logs/09_score.md) |
| 5 | `state.json` 저장/불러오기, 손상 복구<br>Ctrl+C, EOF 처리 | [11_state_json.md](docs/logs/11_state_json.md) |
| 6 | `feature/bonus` 브랜치에서<br>보너스 5종 → main 병합 | [14](docs/logs/14_bonus_random_count.md)~[17](docs/logs/17_bonus_history.md) |
| 7 | 코드를 `app/`로 분리, 실습 스크립트 추가 | [10_quizgame_class.md](docs/logs/10_quizgame_class.md) |
| 8 | README 작성, clone/pull 실습 | [12_readme.md](docs/logs/12_readme.md)<br>[13_clone_pull.md](docs/logs/13_clone_pull.md) |
| 9 | 전체 Git 이력 확인 | [18_git_history.md](docs/logs/18_git_history.md) |

## 10. 작업 흐름도

```mermaid
%%{init: {'flowchart': {'htmlLabels': false, 'padding': 24}}}%%
flowchart TB
    subgraph R1["① 시작과 기본 구조 (main)"]
        direction LR
        A["저장소 생성<br/>첫 커밋"] --> B["Quiz 클래스<br/>기본 퀴즈 7개"] --> C["메뉴와<br/>입력 처리"]
    end
    subgraph R2["② 핵심 기능 (feature/play-quiz)"]
        direction LR
        D["퀴즈 풀기<br/>브랜치 병합"] --> E["추가, 목록<br/>점수 확인"] --> F["state.json<br/>저장과 복구"]
    end
    subgraph R3["③ 보너스와 마무리 (feature/bonus)"]
        direction LR
        G["보너스 5종<br/>브랜치 병합"] --> H["app/ 분리<br/>실습 스크립트"] --> I["README<br/>clone과 pull"]
    end
    R1 --> R2 --> R3
```

## 11. 구조도

```mermaid
%%{init: {'flowchart': {'htmlLabels': false, 'padding': 24}}}%%
flowchart TB
    U["사용자 키보드<br/>입력"] --> M["main.py<br/>저장 경로 결정"]
    M --> G["QuizGame<br/>메뉴와<br/>게임 흐름"]
    G -->|입력 검증| I["input_utils<br/>ask, read_number"]
    G -->|퀴즈 보유| Q["Quiz<br/>문제, 선택지<br/>정답, 힌트"]
    G -->|"저장<br/>불러오기"| S["StateStorage<br/>JSON 읽기, 쓰기"]
    S <--> F[("state.json<br/>UTF-8")]
    D["default_quizzes<br/>기본 퀴즈"] -->|"파일 없음<br/>또는 손상"| G
```

**설계 노트**

- `QuizGame`은 "무엇을 할지"만 알고, 파일을 어떻게 읽고 쓰는지는 `StateStorage`가 맡는다. 저장 방식을 바꿔도 게임 코드는 그대로다.
- 모든 입력은 `input_utils.ask()`를 지나간다. 공백 제거·재입력 규칙이 한 곳에 있어 메뉴·정답·추가 화면이 같은 방식으로 동작한다.
- `Ctrl+C`/EOF는 각 입력 함수가 아니라 `QuizGame.run()` 한 곳에서 잡아 "저장 후 종료"를 보장한다.
- 저장은 임시 파일에 먼저 쓰고 `os.replace`로 바꿔치기한다. 저장 도중 꺼져도 기존 `state.json`이 반쯤 쓰인 채 남지 않는다.

## 12. 핵심 실습 결과

항목마다 두 가지 증거를 함께 붙였습니다. **숫자가 서로 다른 것은 정상**입니다.

| 구분 | 어떻게 만들었나 | 사용한 데이터 |
| --- | --- | --- |
| 🤖 **자동 실행 로그** | `scripts/` 스크립트가 정해진 입력을 넣어 실행<br>(문제 순서 고정 `QUIZ_SEED=42`) | 실습용 `.demo/state.json`<br>매번 새로 만듦 |
| 📸 **직접 실행 화면** | 집 PC에서 내가 키보드로 입력 | 내 기록 `state.json` |

예) 퀴즈 풀기: 자동 로그는 **7문제 중 6문제(86점)**, 직접 실행은 **2문제 중 2문제(100점)**.
점수 확인: 자동 로그는 **3문제 중 3문제**, 직접 실행은 **2문제 중 2문제**.
전체 명령과 출력은 각 로그 링크에 있습니다.

### 12-1. 메뉴와 잘못된 입력 — [02_menu.md](docs/logs/02_menu.md), [03_input_errors.md](docs/logs/03_input_errors.md)

🤖 **자동 실행 로그**

```console
$ printf 'abc\n9\n7\n' | python3 main.py
...
선택: abc
⚠️ 잘못된 입력입니다. 1-7 사이의 숫자를 입력하세요.
선택: 9
⚠️ 잘못된 입력입니다. 1-7 사이의 숫자를 입력하세요.
선택: 7
👋 프로그램을 종료합니다. 다음에 또 만나요!
```

```console
$ sleep 3 | timeout --preserve-status -s INT 1 python3 main.py | tail -n 3; echo "종료 코드: ${PIPESTATUS[1]}"

⚠️ 입력이 중단되었습니다. 데이터를 저장하고 안전하게 종료합니다.
👋 프로그램을 종료합니다. 다음에 또 만나요!
종료 코드: 0
```

📸 **직접 실행 화면**

| 메뉴 | 잘못된 입력 |
| --- | --- |
| ![메뉴](docs/screenshots/menu.png) | ![잘못된 입력](docs/screenshots/invalid-input.png) |

### 12-2. 퀴즈 풀기 — [06_play.md](docs/logs/06_play.md)

🤖 **자동 실행 로그**

```console
[문제 7]
Git에서 변경된 파일을 스테이징 영역(Staging Area)에 올리는 명령어는?
...
정답 입력 (1-4, 힌트: h): 2
✅ 정답입니다!

========================================
🏆 결과: 7문제 중 6문제 정답! (86점)
🎉 새로운 최고 점수입니다!
========================================
```

📸 **직접 실행 화면**

![퀴즈 풀기](docs/screenshots/play.png)

### 12-3. 퀴즈 추가·목록 — [07_add_quiz.md](docs/logs/07_add_quiz.md), [08_list.md](docs/logs/08_list.md)

🤖 **자동 실행 로그**

```console
문제를 입력하세요:
⚠️ 빈 입력입니다. 내용을 입력하세요.
...
정답 번호 (1-4): 0
⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.
정답 번호 (1-4): abc
⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.
정답 번호 (1-4): 2
✅ 퀴즈가 추가되었습니다!
```

📸 **직접 실행 화면**

| 퀴즈 추가 | 퀴즈 목록 |
| --- | --- |
| ![퀴즈 추가](docs/screenshots/add_quiz.png) | ![퀴즈 목록](docs/screenshots/list.png) |

### 12-4. 점수 확인 — [09_score.md](docs/logs/09_score.md)

🤖 **자동 실행 로그**

```console
📭 아직 퀴즈를 풀지 않았습니다. '퀴즈 풀기'로 도전해 보세요!
...
🏆 최고 점수: 100점 (3문제 중 3문제 정답)
```

📸 **직접 실행 화면**

![점수 확인](docs/screenshots/score.png)

### 12-5. state.json 저장·복구 — [11_state_json.md](docs/logs/11_state_json.md)

🤖 **자동 실행 로그**

```console
⚠️ 데이터 파일이 손상되어 기본 퀴즈로 복구했습니다. (JSON 형식 오류: ...)
   손상된 파일은 state.json.bak로 백업했습니다.
```

📸 **직접 실행 화면**: 껐다 켜도 데이터가 남는다 (퀴즈 7개, 최고 점수 100점을 그대로 불러옴)

![재실행](docs/screenshots/restart.png)

### 12-6. Git 이력 — [18_git_history.md](docs/logs/18_git_history.md)

📸 **직접 실행 화면**

| `git log --oneline --graph --all` | GitHub 저장소 |
| --- | --- |
| ![Git 이력](docs/screenshots/git-log-graph.png) | ![GitHub 저장소](docs/screenshots/github-repo.png) |

## 13. 보너스 과제

| 과제 | 수행 내용 | 확인 결과 | 달성 |
| --- | --- | --- | --- |
| 랜덤 출제 | `random.sample(퀴즈목록, n)`<br>원본 순서는 두고 중복 없이 추출 | 시드 1, 2의<br>문제 순서가 다름 | ✅ [로그](docs/logs/14_bonus_random_count.md) |
| 문제 수 선택 | 풀기 전에 1~전체 개수 입력<br>범위 밖은 재입력 | 0, 99 거부 후<br>3문제 출제 | ✅ [로그](docs/logs/14_bonus_random_count.md) |
| 힌트 | `Quiz.hint` 추가<br>풀이 중 `h` 입력 시 출력 (문제당 1회) | 힌트 없는 문제,<br>중복 요청 안내 | ✅ [로그](docs/logs/15_bonus_hint.md) |
| 힌트 감점 | 힌트 본 문제는 맞혀도 50%<br>`HINT_CREDIT = 0.5` | 2문제 중 1개 힌트<br>→ 75점 | ✅ [로그](docs/logs/15_bonus_hint.md) |
| 퀴즈 삭제 | 번호 선택 → y/n 확인<br>→ 삭제 후 즉시 저장 | 7개 → 6개<br>재실행 후에도 6개 | ✅ [로그](docs/logs/16_bonus_delete.md) |
| 점수 히스토리 | 판마다 `played_at`, `total`, `correct`,<br>`hints_used`, `score` 저장 | 3판 기록,<br>평균 점수 | ✅ [로그](docs/logs/17_bonus_history.md) |

점수 계산식: `점수 = round((힌트 없이 맞힌 수 × 1 + 힌트 쓰고 맞힌 수 × 0.5) ÷ 푼 문제 수 × 100)`

| 퀴즈 삭제 | 게임 기록 |
| --- | --- |
| ![퀴즈 삭제](docs/screenshots/delete.png) | ![게임 기록](docs/screenshots/history.png) |

## 14. 로컬 실행 방법

```bash
git clone git@github.com:ilililililil4319/E1-2.git
cd E1-2
python3 --version          # 3.10 이상
python3 main.py            # 게임 실행 (Windows: python main.py)
bash scripts/run_all.sh    # 실습 스크립트 전체 실행 → docs/logs/ 갱신
```

- 처음 실행하면 `state.json`이 없으므로 기본 퀴즈 7개로 시작하고 파일이 자동 생성됩니다.
- 실습 스크립트는 bash가 필요합니다(macOS/Linux/WSL). Windows PowerShell에서는 `python main.py`만 실행할 수 있습니다.
- `13_clone_pull.sh`는 실제로 GitHub에 push합니다(처음 한 번만 커밋하고, 다시 실행하면 건너뜀).

## 15. 환경 변수 및 설정 (데이터 파일 설명)

| 이름 | 기본값 | 설명 |
| --- | --- | --- |
| `QUIZ_STATE_PATH` | 루트의 `state.json` | 데이터 파일 경로<br>스크립트는 `.demo/state.json` 사용<br>(실제 기록 보호) |
| `QUIZ_SEED` | 없음 (매번 랜덤) | 랜덤 출제 순서 고정<br>스크립트는 `42` |
| `PYTHON` | `python3` | 스크립트가 사용할<br>Python 명령 |
| `CLONE_URL` | `origin` 주소 | 13번 스크립트가<br>clone 할 주소 |

### 데이터 파일 설명 (state.json)

- **경로**: 프로젝트 루트 (`main.py`와 같은 폴더). 어느 위치에서 실행해도 이 경로를 사용합니다.
- **역할**: 퀴즈 목록, 최고 점수, 게임 기록을 저장해 다시 실행해도 유지합니다.
- **인코딩**: UTF-8 (`ensure_ascii=False`로 한글을 그대로 저장)
- **Git**: 개인 실행 데이터이므로 `.gitignore`로 제외합니다.

**스키마**

```json
{
  "quizzes": [
    {
      "question": "현재 작업 중인 디렉터리의 절대 경로를 출력하는 명령어는?",
      "choices": ["ls", "cd", "pwd", "whoami"],
      "answer": 3,
      "hint": "print working directory의 약자입니다."
    }
  ],
  "best_score": 86,
  "best_correct": 6,
  "best_total": 7,
  "history": [
    {"played_at": "2026-11-09 13:00:00", "total": 7, "correct": 6, "hints_used": 0, "score": 86}
  ]
}
```

| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list[str] | 선택지 4개 |
| `quizzes[].answer` | int | 정답 번호 (1~4) |
| `quizzes[].hint` | str | 힌트 (없으면 `""`) |
| `best_score` | int \| null | 최고 점수(0~100)<br>아직 안 풀었으면 `null` |
| `best_correct`<br>`best_total` | int | 최고 점수 때<br>맞힌 수 / 푼 수 |
| `history[]` | list | 판마다 날짜/시간, 푼 문제 수,<br>정답 수, 힌트 수, 점수 |

`hint`, `history`가 없는 예전 형식 파일도 읽을 수 있습니다. (기본값 `""`, `[]`)

## 16. 실습 중 발생한 오류와 해결

**① `| head` 를 붙인 명령이 [중단]됨 (종료 코드 141)**

- 문제: `git log ... | head -3`이 정상 출력 후에도 실패로 처리되어 스크립트가 멈췄다.
- 원인 가설: `head`가 3줄만 읽고 파이프를 닫자 `git`이 SIGPIPE(128+13=141)로 끝났고, `pipefail`이 이를 실패로 봤다.
- 확인: 같은 명령을 `echo ${PIPESTATUS[@]}`로 보니 `141 0`이었다.
- 해결: `lib.sh`에서 141은 정상으로 처리했다.

**② 출력에 문구가 있는데도 `check`가 실패**

- 문제: `printf '7\n' | python3 main.py | grep -q '7. 종료'`가 실패했다.
- 원인 가설: `grep -q`는 찾자마자 끝나서, 아직 출력 중이던 Python이 BrokenPipe로 실패했고 `pipefail`이 그 실패를 가져왔다.
- 확인: `pipefail`을 끄면 성공, 켜면 실패.
- 해결: 확인용 `check`는 파이프 마지막 명령(grep)의 결과로만 판단하도록 바꿨다.

**③ 메뉴를 늘린 뒤 테스트 입력이 엉뚱하게 종료됨**

- 문제: 기록 메뉴를 추가한 뒤 "7(기록 보기)"을 입력했는데 프로그램이 종료됐다.
- 원인 가설: 메뉴가 5개 → 7개로 늘면서 번호가 밀려 7이 "종료"가 되었다.
- 확인: 메뉴를 출력해 보니 6이 게임 기록, 7이 종료였다.
- 해결: 테스트 입력 번호를 고치고, 메뉴는 리스트(`menu_items`) 하나로 관리해 번호와 범위 안내가 자동으로 맞춰지게 했다.

**④ 퀴즈 추가 화면에서 메뉴 번호를 입력함 (집 PC 실습 중)**

- 문제: 메뉴로 돌아간 줄 알고 `2`, `7`, `7`을 입력했더니 문제·선택지로 들어갔고, 선택지 3에서 빈 입력 안내가 반복됐다.
- 원인 가설: `2`(퀴즈 추가)를 고른 뒤라 프로그램은 이미 "문제 입력" 단계였다. 화면 맨 위 `📌 새로운 퀴즈를 추가합니다.`를 놓쳤다.
- 확인: 화면을 위로 올려 보니 `문제를 입력하세요: 2`, `선택지 1: 7`로 기록되어 있었다.
- 해결: `Ctrl+C`로 중단 → "데이터를 저장하고 안전하게 종료" 후 다시 실행. 만들던 퀴즈는 저장되지 않았고(목록 7개 유지), 처음부터 다시 추가했다. 입력 중 Ctrl+C 처리가 실제로 쓸모 있음을 확인했다.

## 17. AI(Claude) 사용 로그 요약

| 사용 작업 | 이유 | 검증 방법 |
| --- | --- | --- |
| 코드, 스크립트 초안 | 구조를 빠르게 잡고<br>요구사항을 빠짐없이 매핑 | 스크립트 결과(✅/❌)와<br>직접 실행으로 확인 |
| 오류 원인 분석 (16장) | 종료 코드 141처럼<br>처음 보는 오류의 원인 찾기 | 원인 가설을 명령으로<br>다시 확인한 뒤 수정 |
| README, SETUP 초안 | 22개 목차 형식 맞추기 | 실행 로그의 실제 값과 대조 |
| 학습 정리 | 용어와 명령을<br>초보자 눈높이로 이해 | 핵심 질문(2장)을<br>내 말로 설명해 보기 |

설치, 스크립트 실행, 화면 캡처, 커밋·push는 직접 했습니다.

## 18. 기능요구사항 대비 결과

| 요구사항 | 구현 위치 | 달성 |
| --- | --- | --- |
| 1. Git 저장소 설정<br>(.gitignore, README, 첫 commit, push) | `.gitignore`, `README.md`<br>첫 커밋 | ✅ |
| 2. 메뉴<br>(출력, 선택, 종료, 잘못된 입력) | `QuizGame.run`, `show_menu`<br>`menu_items` | ✅ |
| 3. 공통 입력/예외<br>(공백, abc, 범위 밖, 빈 입력,<br>Ctrl+C, EOF, 파일 없음/손상) | `input_utils.py`<br>`QuizGame.run`, `load_state` | ✅ |
| 4. Quiz 클래스<br>(question, choices 4개, answer 1~4,<br>출력, 정답 확인) | `app/quiz.py` | ✅ |
| 5. 기본 퀴즈 5개 이상<br>(Quiz 인스턴스) | `app/default_quizzes.py` (7개) | ✅ |
| 6. 퀴즈 풀기 + 브랜치<br>(`feature/play-quiz` → main) | `QuizGame.play_quiz` | ✅ |
| 7. 퀴즈 추가 + 파일 저장 | `QuizGame.add_quiz` | ✅ |
| 8. 퀴즈 목록 + 없음 처리 | `QuizGame.list_quizzes` | ✅ |
| 9. 점수 확인, 갱신, 저장<br>+ 미풀이 처리 | `QuizGame.update_best_score`<br>`QuizGame.show_best_score` | ✅ |
| 10. QuizGame 클래스<br>(목록, 최고 점수, 기능별 메서드) | `app/quiz_game.py` | ✅ |
| 11. state.json 저장/불러오기<br>(UTF-8, try/except) | `app/storage.py` | ✅ |
| 12. README 필수 항목 | 이 문서 1·3·4·14·15장 | ✅ |
| 13. clone/pull 실습 | `scripts/13_clone_pull.sh` | ✅ |
| 커밋 10개 이상<br>Git 7종 명령 | [18_git_history.md](docs/logs/18_git_history.md) | ✅ |

## 19. 결론 및 한계점

`Quiz`(데이터) · `QuizGame`(흐름) · `StateStorage`(저장)로 책임을 나눠, 기능을 추가할 때마다 고칠 곳이 한 군데로 모였습니다.
보너스 기능(힌트·삭제·기록)을 넣을 때도 저장 형식만 `to_dict/from_dict`에 추가하면 되었습니다.

**한계점**

- 퀴즈를 수정하는 메뉴가 없다 (삭제 후 다시 추가해야 함).
- 데이터가 파일 하나라서 여러 사람이 동시에 쓰면 마지막 저장이 이긴다.
- 자동 테스트가 셸 스크립트 기반이라 Windows PowerShell에서는 바로 실행되지 않는다.

**설계 결정과 다른 선택지**

| 결정 | 이유 | 검토한 대안 |
| --- | --- | --- |
| 클래스 3개로 분리 | 저장 방식이 바뀌어도<br>게임 코드는 그대로 | 2개(QuizGame이 저장까지)<br>→ 한 클래스가 너무 커짐 |
| 정답을 번호(1~4)로 저장 | 미션 권장,<br>입력과 비교가 단순 | 정답 문자열 저장<br>→ 선택지를 고치면 정답이 깨짐 |
| JSON 파일 1개 | 미션 요구,<br>사람이 읽고 고칠 수 있음 | SQLite<br>→ 학습 범위를 넘음 |
| 임시 파일에 쓴 뒤<br>`os.replace` | 저장 중 꺼져도<br>기존 파일 보존 | 바로 덮어쓰기<br>→ 중간에 끊기면 파일 손상 |
| 손상 파일은 `.bak`으로<br>백업 후 초기화 | 데이터를 버리지 않고<br>원인 확인 가능 | 바로 삭제<br>→ 복구 불가 |
| `random.sample` | 원본 순서를 지키면서<br>n개만 한 번에 뽑기 | `random.shuffle` 후 자르기<br>→ 원본 순서가 바뀜 |
| 힌트 감점 50% | 힌트를 쓰면 손해지만<br>0점은 아니게 | 고정 감점(-10점)<br>→ 문제 수에 따라 비중이 달라짐 |
| 실습 스크립트 + `.md` 로그 | 명령과 출력을 빠짐없이,<br>다시 실행 가능 | 손으로 실행 후 캡처<br>→ 빠지는 명령, 재현 어려움 |
| `QUIZ_SEED`<br>`QUIZ_STATE_PATH` | 같은 결과 재현,<br>실제 기록 보호 | 코드 안에 테스트용 분기<br>→ 실제 동작과 달라짐 |

## 20. 보안 유의사항

- `state.json`(개인 기록), `.demo/`, `.env`, 키 파일(`*.pem`, `id_ed25519*` 등)은 `.gitignore`로 제외했습니다.
- 실행 로그는 `lib.sh`가 이메일·GitHub 토큰을 `****`, 홈 경로를 `~`로 바꿔 저장합니다.
- 스크린샷의 터미널 아이디·컴퓨터 이름, 계정 메뉴의 이메일은 가렸습니다.
- GitHub에는 SSH **공개키**만 등록했습니다. 개인키는 PC 밖으로 내보내지 않습니다.

## 21. 출처 및 라이선스 유의사항

- 코드와 퀴즈 문제는 직접 작성했으며 외부 코드를 복사하지 않았습니다.
- Python 표준 라이브러리 문서: https://docs.python.org/3/ (PSF License)
- Git 문서: https://git-scm.com/docs
- 미션 원문(코디세이 E1-2)은 저장소에 포함하지 않았습니다.

## 22. 기타

- 환경 세팅: [docs/SETUP.md](docs/SETUP.md)
- 커밋 메시지 규칙: `Feat:` 기능, `Fix:` 버그 수정, `Docs:` 문서, `Refactor:` 구조 개선, `Chore:` 설정
- Python 튜토리얼: https://docs.python.org/ko/3/tutorial/
- Pro Git (한국어): https://git-scm.com/book/ko/v2
- clone/pull 실습: 복제본(E1-2-copy)에서 이 줄을 추가하고 push → 원래 폴더에서 pull로 받음
