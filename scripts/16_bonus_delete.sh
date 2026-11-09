#!/usr/bin/env bash
# 16. 보너스: 퀴즈 삭제 + 파일 반영
source "$(dirname "$0")/lib.sh"
start_log "16. 보너스 - 퀴즈 삭제"
reset_demo

section "삭제 취소(0) → 범위 밖(99) → 1번 선택 후 n(취소) → 1번 선택 후 y(삭제)"
play '5\n0\n5\n99\n1\nx\nn\n5\n1\ny\n3\n7\n'

section "파일에 반영되었는지 확인"
check "퀴즈가 6개로 줄었다" "$PY -c \"import json;assert len(json.load(open('.demo/state.json',encoding='utf-8'))['quizzes'])==6\""
run "grep -c '\"question\"' .demo/state.json"

section "다시 실행해도 6개"
play '7\n'
finish
