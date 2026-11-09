# 18. Git 기록 (git log --oneline --graph)

> 이 파일은 `scripts/18_git_history.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:02:45 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

## git log --oneline --graph (제출 스크린샷과 같은 명령)

```console
$ git log --oneline --graph --all
* 7277d55 Docs: clone/pull 실습으로 README에 한 줄 추가
* 320f2b7 Docs: 환경 확인 스크린샷 추가 (VSCode, Python, Git 설정)
* dd2035e Docs: 용어 설명을 분야별로 확장하고 읽는 법·띄어쓰기 표시 추가
* ce32b39 Docs: 구조도 상자 글자가 잘리지 않도록 줄 나누기와 여백 추가
* 4233cfe Docs: 흐름도·구조도 글자가 GitHub에서 글자 단위로 끊기지 않도록 수정
* c3096ae Docs: 표 안 단어가 글자 단위로 끊기지 않도록 README·SETUP 표 정리
* 6fc13ad Docs: README 목차에 '용어 설명'을 5장으로 번호 부여 (전체 22장)
* 7dbebef Docs: 작업 흐름도를 3줄로 재배치하고 도표 글자 깨짐 방지
* 6b4d604 Fix: clone/pull 실습 스크립트에서 '-'로 시작하는 문장 검색 오류 수정
* f29bf7d Docs: README를 21개 목차 기술 문서로 재구성
* c73f0c4 Docs: SETUP.md 환경 세팅 문서 추가 (Windows WSL2 기준)
* 80dc148 Feat: 요구사항별 실습 스크립트와 자동 실행 로그 기록 추가
* 2881e13 Chore: .gitignore에 실습 데이터(.demo)와 비밀 정보(.env, 키 파일) 제외 추가
* 9f5e1c7 Feat: 파이프 입력 에코와 QUIZ_SEED 랜덤 고정 옵션 추가
* 69f8866 Refactor: 게임 코드를 app/ 패키지로 분리
* b8ddc90 Docs: README에 보너스 기능, 점수 계산식, history 스키마, Git 작업 흐름 추가
*   7ee051f Merge branch 'feature/bonus' into main
|\  
| * 68fff99 Feat: 점수 기록 히스토리 추가 (보너스)
| * 303bf18 Feat: 퀴즈 삭제 기능 추가 (보너스)
| * eb9c1c5 Feat: 힌트 기능 및 힌트 사용 시 점수 차감 추가 (보너스)
| * 8043c4c Feat: 랜덤 출제 및 문제 수 선택 기능 추가 (보너스)
|/  
* 8d04f7f Docs: README 작성 (개요, 주제 선정 이유, 실행 방법, 기능, 파일 구조, state.json)
* cce966d Fix: Ctrl+C / EOF 입력 시 비정상 종료 대신 저장 후 안전 종료
* e70cdbb Feat: state.json 저장/불러오기 및 손상 파일 복구 구현
* 7d15369 Feat: 최고 점수 확인 및 갱신 기능 구현
* b69e500 Feat: 퀴즈 목록 기능 구현
* 51bc304 Feat: 퀴즈 추가 기능 구현
*   31e0616 Merge branch 'feature/play-quiz' into main
|\  
| * cf9b744 Feat: 퀴즈 풀기 기능 구현
|/  
* 4e6df43 Feat: 메뉴 기능 및 공통 입력 예외 처리 구현
* af589a3 Feat: 기본 퀴즈 데이터 7개 작성 (개발 입문 상식)
* 14ea985 Feat: Quiz 클래스 구현
* 79c5ff4 Chore: 프로젝트 초기 설정 (.gitignore, README 생성)
```

## 개수 확인

```console
$ git rev-list --count HEAD
33
```
- ✅ 커밋 10개 이상

```console
$ git log --oneline --merges
7ee051f Merge branch 'feature/bonus' into main
31e0616 Merge branch 'feature/play-quiz' into main
```
- ✅ 브랜치 병합 1회 이상

```console
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/feature/bonus
  remotes/origin/feature/play-quiz
  remotes/origin/main
```

## 커밋 메시지 접두어별 개수

```console
$ git log --format='%s' | grep -oE '^(Feat|Fix|Docs|Refactor|Chore|Test|Style|Merge)' | sort | uniq -c | sort -rn
     14 Feat
     12 Docs
      2 Merge
      2 Fix
      2 Chore
      1 Refactor
```

## 이 컴퓨터에서 실행한 Git 동작 (reflog: clone, pull, commit, checkout 등)

```console
$ git reflog --date=format:'%Y-%m-%d %H:%M' --format='%h %gd %gs' | head -n 15
7277d55 HEAD@{2026-11-09 23:02} pull --no-rebase --no-edit: Fast-forward
dd2035e HEAD@{2026-11-09 22:54} clone: from github.com:ilililililil4319/E1-2.git
```

## Git 7종 명령 사용 위치

| 명령 | 사용한 곳 |

| --- | --- |

| init | 01_git_setup.md (임시 폴더 실습) |

| add, commit | 커밋 기록 전체, 13_clone_pull.md |

| push | 13_clone_pull.md (복제본에서 push) |

| pull | 13_clone_pull.md (원래 폴더에서 pull) |

| checkout | feature/play-quiz, feature/bonus 브랜치 작업 + 01_git_setup.md |

| clone | 처음 내려받을 때 + 13_clone_pull.md |

---

**결과: 모든 단계 통과 ✅**
