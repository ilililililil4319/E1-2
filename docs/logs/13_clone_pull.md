# 13. Git 저장소 복제 실습 (clone / pull)

> 이 파일은 `scripts/13_clone_pull.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:02:35 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

## 1) 다른 폴더로 clone

```console
$ rm -rf ../E1-2-copy
```

```console
$ git clone git@github.com:ilililililil4319/E1-2.git ../E1-2-copy
Cloning into '../E1-2-copy'...
```

```console
$ ls ../E1-2-copy
README.md
app
docs
main.py
scripts
```

## 2) 복제본에서 README에 한 줄 추가 → commit → push

```console
$ echo '- clone/pull 실습: 복제본(E1-2-copy)에서 이 줄을 추가하고 push → 원래 폴더에서 pull로 받음' >> ../E1-2-copy/README.md
```

```console
$ cd ../E1-2-copy && git status --short
 M README.md
```

```console
$ cd ../E1-2-copy && git add README.md && git commit -m 'Docs: clone/pull 실습으로 README에 한 줄 추가'
[main 7277d55] Docs: clone/pull 실습으로 README에 한 줄 추가
 1 file changed, 1 insertion(+)
```

```console
$ cd ../E1-2-copy && git push
To github.com:ilililililil4319/E1-2.git
   320f2b7..7277d55  main -> main
```

## 3) 원래 작업 폴더에서 pull

```console
$ git pull --no-rebase --no-edit
From github.com:ilililililil4319/E1-2
   dd2035e..7277d55  main       -> origin/main
Updating dd2035e..7277d55
Fast-forward
 README.md                         |   1 +
 docs/screenshots/git-check.png    | Bin 0 -> 18232 bytes
 docs/screenshots/python-check.png | Bin 0 -> 6154 bytes
 docs/screenshots/vscode.png       | Bin 0 -> 98781 bytes
 4 files changed, 1 insertion(+)
 create mode 100644 docs/screenshots/git-check.png
 create mode 100644 docs/screenshots/python-check.png
 create mode 100644 docs/screenshots/vscode.png
```

## 4) pull 받은 내용 확인

```console
$ tail -n 2 README.md
- Pro Git (한국어): https://git-scm.com/book/ko/v2
- clone/pull 실습: 복제본(E1-2-copy)에서 이 줄을 추가하고 push → 원래 폴더에서 pull로 받음
```
- ✅ 원래 폴더 README에 복제본에서 쓴 줄이 반영됨

```console
$ git log --oneline -3
7277d55 Docs: clone/pull 실습으로 README에 한 줄 추가
320f2b7 Docs: 환경 확인 스크린샷 추가 (VSCode, Python, Git 설정)
dd2035e Docs: 용어 설명을 분야별로 확장하고 읽는 법·띄어쓰기 표시 추가
```

```console
$ rm -rf ../E1-2-copy
```

---

**결과: 모든 단계 통과 ✅**
