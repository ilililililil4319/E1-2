# 01. Git 저장소 설정

> 이 파일은 `scripts/01_git_setup.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:02:27 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

요구사항: GitHub 저장소 생성 → 로컬 저장소 설정 → .gitignore, README.md 생성 → 첫 commit과 push

## 원격 저장소 연결 확인

```console
$ git remote -v
origin	git@github.com:ilililililil4319/E1-2.git (fetch)
origin	git@github.com:ilililililil4319/E1-2.git (push)
```

```console
$ git branch -vv
* main dd2035e [origin/main] Docs: 용어 설명을 분야별로 확장하고 읽는 법·띄어쓰기 표시 추가
```

## .gitignore 와 README.md

```console
$ ls -a
.
..
.git
.gitignore
README.md
app
docs
main.py
scripts
```
- ✅ .gitignore 파일이 있다
- ✅ README.md 파일이 있다

```console
$ cat .gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/

# 실행 중 생성되는 데이터 파일 (개인 퀴즈/점수 기록)
state.json
state.json.tmp
state.json.bak

# 실습 스크립트가 쓰는 임시 데이터 (scripts/lib.sh → .demo/state.json)
.demo/

# 비밀 정보 (토큰·비밀번호·개인 키는 절대 올리지 않는다)
.env
.env.*
*.pem
*.key
id_rsa*
id_ed25519*

# OS / Editor
.DS_Store
Thumbs.db
Zone.Identifier
*:Zone.Identifier
.vscode/
.idea/
```

state.json(개인 실행 데이터)과 .demo/(실습 데이터)는 Git에 올리지 않는다.

```console
$ git check-ignore -v state.json .demo/state.json
.gitignore:9:state.json	state.json
.gitignore:14:.demo/	.demo/state.json
```

## 첫 번째 커밋

```console
$ git log --reverse --format='%h %ad %s' --date=short | head -3
79c5ff4 2026-11-06 Chore: 프로젝트 초기 설정 (.gitignore, README 생성)
14ea985 2026-11-06 Feat: Quiz 클래스 구현
af589a3 2026-11-06 Feat: 기본 퀴즈 데이터 7개 작성 (개발 입문 상식)
```

## git init 실습 (임시 폴더에서 init → add → commit → checkout → merge)

이 저장소는 GitHub에서 clone 했기 때문에 init을 따로 하지 않았다. init이 하는 일을 임시 폴더에서 직접 확인한다.

```console
$ rm -rf /tmp/e1-2-git-practice && mkdir -p /tmp/e1-2-git-practice
```

```console
$ cd /tmp/e1-2-git-practice && git init -b main
Initialized empty Git repository in /tmp/e1-2-git-practice/.git/
```

```console
$ ls -a /tmp/e1-2-git-practice
.
..
.git
```

```console
$ cd /tmp/e1-2-git-practice && echo 'hello' > hello.txt && git add hello.txt && git status --short
A  hello.txt
```

```console
$ cd /tmp/e1-2-git-practice && git commit -q -m 'Feat: hello 파일 추가' && git log --oneline
79b9ee7 Feat: hello 파일 추가
```

```console
$ cd /tmp/e1-2-git-practice && git checkout -b feature/greet
Switched to a new branch 'feature/greet'
```

```console
$ cd /tmp/e1-2-git-practice && echo 'bye' >> hello.txt && git commit -q -am 'Feat: 인사 추가' && git log --oneline
f539505 Feat: 인사 추가
79b9ee7 Feat: hello 파일 추가
```

```console
$ cd /tmp/e1-2-git-practice && git checkout main && git merge --no-ff -q -m 'Merge branch feature/greet' feature/greet
Switched to branch 'main'
```

```console
$ cd /tmp/e1-2-git-practice && git log --oneline --graph
*   4ea3399 Merge branch feature/greet
|\  
| * f539505 Feat: 인사 추가
|/  
* 79b9ee7 Feat: hello 파일 추가
```

```console
$ rm -rf /tmp/e1-2-git-practice
```

---

**결과: 모든 단계 통과 ✅**
