#!/usr/bin/env bash
# 08. 퀴즈 목록: 저장된 목록 확인, 퀴즈 없음 처리
source "$(dirname "$0")/lib.sh"
start_log "08. 퀴즈 목록"
reset_demo

section "퀴즈 목록 보기"
play '3\n7\n'
check "목록에 7개가 보인다" "printf '3\n7\n' | $PY main.py | grep -q '총 7개'"

section "퀴즈가 없는 경우"
put_state '{"quizzes": [], "best_score": null}'
play '3\n7\n'
check "퀴즈 없음 안내" "printf '3\n7\n' | $PY main.py | grep -q '등록된 퀴즈가 없습니다.'"
finish
