#!/usr/bin/env bash
# 02. 메뉴 기능: 메뉴 출력, 기능 선택, 종료, 잘못된 입력 처리
source "$(dirname "$0")/lib.sh"
start_log "02. 메뉴 기능"
reset_demo

section "메뉴 출력 후 종료 (7)"
play '7\n'
check "메뉴에 7개 항목과 종료가 있다" "printf '7\n' | $PY main.py | grep -q '7. 종료'"

section "기능 선택: 3(목록) → 4(점수) → 7(종료)"
play '3\n4\n7\n'

section "잘못된 입력: abc, 9 → 안내 후 다시 입력"
play 'abc\n9\n7\n'
check "abc 입력 시 안내 메시지" "printf 'abc\n7\n' | $PY main.py | grep -q '잘못된 입력입니다. 1-7 사이의 숫자'"
finish
