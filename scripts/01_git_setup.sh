#!/usr/bin/env bash
# 01. Git 저장소 설정: 원격 저장소 연결, .gitignore·README.md, 첫 커밋, init 실습
source "$(dirname "$0")/lib.sh"
start_log "01. Git 저장소 설정"
note "요구사항: GitHub 저장소 생성 → 로컬 저장소 설정 → .gitignore, README.md 생성 → 첫 commit과 push"

section "원격 저장소 연결 확인"
run "git remote -v"
run "git branch -vv"

section ".gitignore 와 README.md"
run "ls -a"
check ".gitignore 파일이 있다" "test -f .gitignore"
check "README.md 파일이 있다" "test -f README.md"
run "cat .gitignore"
note "state.json(개인 실행 데이터)과 .demo/(실습 데이터)는 Git에 올리지 않는다."
run "git check-ignore -v state.json .demo/state.json"

section "첫 번째 커밋"
run "git log --reverse --format='%h %ad %s' --date=short | head -3"

section "git init 실습 (임시 폴더에서 init → add → commit → checkout → merge)"
note "이 저장소는 GitHub에서 clone 했기 때문에 init을 따로 하지 않았다. init이 하는 일을 임시 폴더에서 직접 확인한다."
P=/tmp/e1-2-git-practice
run "rm -rf $P && mkdir -p $P"
run "cd $P && git init -b main"
run "ls -a $P"
run "cd $P && echo 'hello' > hello.txt && git add hello.txt && git status --short"
run "cd $P && git commit -q -m 'Feat: hello 파일 추가' && git log --oneline"
run "cd $P && git checkout -b feature/greet"
run "cd $P && echo 'bye' >> hello.txt && git commit -q -am 'Feat: 인사 추가' && git log --oneline"
run "cd $P && git checkout main && git merge --no-ff -q -m 'Merge branch feature/greet' feature/greet"
run "cd $P && git log --oneline --graph"
run "rm -rf $P"
finish
