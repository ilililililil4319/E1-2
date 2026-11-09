#!/usr/bin/env bash
# 17. 보너스: 점수 기록 히스토리 (날짜/시간, 푼 문제 수, 점수)
source "$(dirname "$0")/lib.sh"
start_log "17. 보너스 - 점수 기록 히스토리"
reset_demo

section "기록이 없을 때"
play '6\n7\n'

section "3판 플레이 후 기록 보기"
mapfile -t A < <(answers 3 2x 7)
play "1\n3\n${A[0]}\n1\n2\n${A[1]}\n1\n7\n${A[2]}\n6\n7\n"
check "기록 3건 저장" "$PY -c \"import json;assert len(json.load(open('.demo/state.json',encoding='utf-8'))['history'])==3\""

section "state.json의 history"
run "$PY -c \"import json; print(json.dumps(json.load(open('.demo/state.json', encoding='utf-8'))['history'], ensure_ascii=False, indent=2))\""
finish
