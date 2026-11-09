#!/usr/bin/env bash
# 03. 공통 입력/예외 처리: 공백, 숫자 변환 실패, 범위 밖, 빈 입력, Ctrl+C, EOF
source "$(dirname "$0")/lib.sh"
start_log "03. 공통 입력/예외 처리"
reset_demo

section "입력 앞뒤 공백 제거: ' 3 ' → 3"
play ' 3 \n 7 \n'
check "' 3 '이 목록 메뉴로 처리된다" "printf ' 3 \n7\n' | $PY main.py | grep -q '등록된 퀴즈 목록'"

section "숫자 변환 실패(abc), 범위 밖(메뉴 9 / 정답 0), 빈 입력(Enter)"
play 'abc\n9\n\n1\n1\n0\n\nabc\n1\n7\n'
check "빈 입력 안내" "printf '\n7\n' | $PY main.py | grep -q '빈 입력입니다'"
check "정답 0 입력 시 범위 안내" "printf '1\n1\n0\n1\n7\n' | $PY main.py | grep -q '1-4 사이의 숫자'"

section "입력 스트림 종료(EOFError): 퀴즈 추가 도중 입력이 끊김"
note "printf가 보낸 입력이 '선택지 1' 까지만 있고 끝난다. (키보드에서 Ctrl+D와 같은 상황)"
play '2\n중간에 끊긴 문제\n선택지A\n'
check "추가 도중 끊긴 퀴즈는 저장되지 않았다(7개 유지)" "$PY -c \"import json;assert len(json.load(open('.demo/state.json',encoding='utf-8'))['quizzes'])==7\""

section "Ctrl+C(KeyboardInterrupt): 메뉴에서 입력을 기다리는 중 SIGINT 보내기"
note "timeout -s INT 1 은 1초 뒤 Ctrl+C와 같은 신호(SIGINT)를 보낸다. --preserve-status 는 프로그램의 실제 종료 코드를 그대로 돌려준다."
run "sleep 3 | timeout --preserve-status -s INT 1 $PY main.py | tail -n 3; echo \"종료 코드: \${PIPESTATUS[1]}\""
check "Ctrl+C 후에도 종료 코드 0 (정상 종료)" "sleep 2 | timeout --preserve-status -s INT 1 $PY main.py"
finish
