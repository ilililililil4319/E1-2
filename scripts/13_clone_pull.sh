#!/usr/bin/env bash
# 13. Git 저장소 복제 실습: clone → 복제본에서 수정·commit·push → 원래 폴더에서 pull → 반영 확인
# 다시 실행해도 안전하다: README에 이미 실습 줄이 있으면 커밋·push는 건너뛰고 clone/pull만 한다.
source "$(dirname "$0")/lib.sh"
start_log "13. Git 저장소 복제 실습 (clone / pull)"

URL="${CLONE_URL:-$(git remote get-url origin)}"
COPY="../E1-2-copy"
MARK="- clone/pull 실습: 복제본(E1-2-copy)에서 이 줄을 추가하고 push → 원래 폴더에서 pull로 받음"

section "1) 다른 폴더로 clone"
run "rm -rf $COPY"
run "git clone $URL $COPY"
run "ls $COPY"

section "2) 복제본에서 README에 한 줄 추가 → commit → push"
if grep -qF -- "$MARK" "$COPY/README.md"; then
    note "README에 실습 줄이 이미 있다(이전 실행에서 push 완료). 커밋·push는 건너뛴다."
    run "grep -nF 'clone/pull 실습' $COPY/README.md"
else
    run "echo '$MARK' >> $COPY/README.md"
    run "cd $COPY && git status --short"
    run "cd $COPY && git add README.md && git commit -m 'Docs: clone/pull 실습으로 README에 한 줄 추가'"
    run "cd $COPY && git push"
fi

section "3) 원래 작업 폴더에서 pull"
run "git pull --no-rebase --no-edit"

section "4) pull 받은 내용 확인"
run "tail -n 2 README.md"
check "원래 폴더 README에 복제본에서 쓴 줄이 반영됨" "grep -qF -- '$MARK' README.md"
run "git log --oneline -3"
run "rm -rf $COPY"
finish
