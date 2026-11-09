#!/usr/bin/env bash
# 06. 퀴즈 풀기 (브랜치 활용): 출제 → 정답 입력 → 정답/오답 → 결과, 퀴즈 없음 처리
source "$(dirname "$0")/lib.sh"
start_log "06. 퀴즈 풀기 (브랜치 활용)"
reset_demo

section "7문제 풀기 (첫 문제는 일부러 오답)"
note "입력 순서: 1(퀴즈 풀기) → 7(문제 수) → 정답 7개 → 7(종료). QUIZ_SEED로 순서가 고정되어 있어 정답을 미리 계산해 넣는다."
A="$(answers 7w)"
play "1\n7\n$A\n7\n"
check "결과: 7문제 중 6문제 정답 (86점)" "grep -q '\"best_score\": 86' .demo/state.json"

section "퀴즈가 없는 경우"
put_state '{"quizzes": [], "best_score": null}'
play '1\n7\n'
check "퀴즈가 없으면 안내 메시지" "printf '1\n7\n' | $PY main.py | grep -q '등록된 퀴즈가 없습니다'"

section "브랜치 작업 기록 (feature/play-quiz → main 병합)"
run "git branch -a"
run "git log --oneline --merges"
run "git log --oneline --graph | grep -B1 -A2 'feature/play-quiz'"
check "feature/play-quiz 병합 커밋이 있다" "git log --oneline --merges | grep -q 'feature/play-quiz'"
finish
