#!/usr/bin/env bash
# 15. 보너스: 힌트 기능 + 힌트 사용 시 점수 차감
source "$(dirname "$0")/lib.sh"
start_log "15. 보너스 - 힌트와 점수 차감"
reset_demo
note "규칙: 풀이 중 h 입력 → 힌트 출력(문제당 1번). 힌트를 본 문제는 맞혀도 50%만 인정."

section "2문제: 1번은 힌트 보고 정답, 2번은 그냥 정답 → (0.5 + 1) / 2 = 75점"
mapfile -t A < <(answers 2)
A1="${A[0]%%\\n*}"
A2="${A[0]##*\\n}"
play "1\n2\nh\nh\n$A1\n$A2\n7\n"
check "75점으로 계산됨" "grep -q '\"best_score\": 75' .demo/state.json"

section "힌트가 없는 퀴즈에서 h 입력"
put_state '{"quizzes": [{"question": "Python의 창시자는?", "choices": ["Guido", "Linus", "Bjarne", "James"], "answer": 1, "hint": ""}], "best_score": null}'
play '1\n1\nh\n1\n7\n'

section "저장된 힌트 필드"
run "grep -n 'hint' app/quiz.py"
finish
