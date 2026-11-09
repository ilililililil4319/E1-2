#!/usr/bin/env bash
# 09. 점수 확인: 최고 점수 확인·비교·갱신·저장, 아직 안 푼 경우 처리
source "$(dirname "$0")/lib.sh"
start_log "09. 점수 확인"
reset_demo

section "아직 퀴즈를 풀지 않은 경우"
play '4\n7\n'

section "1판 3문제 모두 정답(100점) → 2판 3문제 모두 오답(0점) → 점수 확인"
mapfile -t A < <(answers 3 3x)
play "1\n3\n${A[0]}\n1\n3\n${A[1]}\n4\n7\n"
check "최고 점수 100점 유지 (0점으로 덮어쓰지 않음)" "grep -q '\"best_score\": 100' .demo/state.json"

section "파일에 저장된 최고 점수"
run "grep -E 'best_(score|correct|total)' .demo/state.json"

section "다시 실행해도 최고 점수가 남아 있다"
play '4\n7\n'
finish
