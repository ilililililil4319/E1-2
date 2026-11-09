#!/usr/bin/env bash
# 18. Git 기록 확인: 커밋 10개 이상, 브랜치 생성·병합, 7종 명령 사용 흔적
source "$(dirname "$0")/lib.sh"
start_log "18. Git 기록 (git log --oneline --graph)"

section "git log --oneline --graph (제출 스크린샷과 같은 명령)"
run "git log --oneline --graph --all"

section "개수 확인"
run "git rev-list --count HEAD"
check "커밋 10개 이상" "test \$(git rev-list --count HEAD) -ge 10"
run "git log --oneline --merges"
check "브랜치 병합 1회 이상" "test \$(git log --merges --oneline | wc -l) -ge 1"
run "git branch -a"

section "커밋 메시지 접두어별 개수"
run "git log --format='%s' | grep -oE '^(Feat|Fix|Docs|Refactor|Chore|Test|Style|Merge)' | sort | uniq -c | sort -rn"

section "이 컴퓨터에서 실행한 Git 동작 (reflog: clone, pull, commit, checkout 등)"
run "git reflog --date=format:'%Y-%m-%d %H:%M' --format='%h %gd %gs' | head -n 15"

section "Git 7종 명령 사용 위치"
note "| 명령 | 사용한 곳 |"
note "| --- | --- |"
note "| init | 01_git_setup.md (임시 폴더 실습) |"
note "| add, commit | 커밋 기록 전체, 13_clone_pull.md |"
note "| push | 13_clone_pull.md (복제본에서 push) |"
note "| pull | 13_clone_pull.md (원래 폴더에서 pull) |"
note "| checkout | feature/play-quiz, feature/bonus 브랜치 작업 + 01_git_setup.md |"
note "| clone | 처음 내려받을 때 + 13_clone_pull.md |"
finish
