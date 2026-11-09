#!/usr/bin/env bash
# 14. 보너스: 랜덤 출제 + 문제 수 선택
source "$(dirname "$0")/lib.sh"
start_log "14. 보너스 - 랜덤 출제와 문제 수 선택"
reset_demo

section "문제 수 선택: 0, 99는 범위 밖 → 3 입력"
play '1\n0\n99\n3\n1\n1\n1\n7\n'

section "랜덤 출제: 같은 3문제 풀기를 시드만 바꿔 두 번 실행"
note "QUIZ_SEED를 바꾸면 순서가 달라진다. (평소에는 시드를 정하지 않으므로 실행할 때마다 달라진다)"
run "printf '1\n3\n1\n1\n1\n7\n' | QUIZ_SEED=1 $PY main.py | grep -A1 '^\[문제'"
run "printf '1\n3\n1\n1\n1\n7\n' | QUIZ_SEED=2 $PY main.py | grep -A1 '^\[문제'"
check "시드가 다르면 문제 순서가 다르다" "test \"\$(printf '1\n3\n1\n1\n1\n7\n' | QUIZ_SEED=1 $PY main.py | grep -A1 '^\[문제')\" != \"\$(printf '1\n3\n1\n1\n1\n7\n' | QUIZ_SEED=2 $PY main.py | grep -A1 '^\[문제')\""

section "원본 목록 순서는 그대로 (random.sample은 원본을 바꾸지 않음)"
play '3\n7\n'
run "grep -n 'random\.' app/quiz_game.py"
finish
