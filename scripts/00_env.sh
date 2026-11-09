#!/usr/bin/env bash
# 00. 실행 환경 기록: 어떤 OS·Python·Git에서 실행했는지 남긴다.
source "$(dirname "$0")/lib.sh"
start_log "00. 실행 환경"

section "운영체제"
run "uname -srm"
try "grep PRETTY_NAME /etc/os-release"

section "Python (요구: 3.10 이상, 외부 라이브러리 없음)"
run "$PY --version"
run "which $PY"
check "Python 3.10 이상" "$PY -c 'import sys; assert sys.version_info >= (3, 10)'"

section "Git"
run "git --version"
run "git config user.name"
run "git config user.email"
run "git config init.defaultBranch || echo '(설정 안 됨: 기본값 사용)'"

section "Docker (이번 미션에서는 필수 아님)"
try "docker --version"

section "작업 위치와 원격 저장소"
run "pwd"
run "git remote -v"
run "git status -sb | head -1"
finish
