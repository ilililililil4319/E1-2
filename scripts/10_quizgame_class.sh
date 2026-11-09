#!/usr/bin/env bash
# 10. QuizGame 클래스: 속성(퀴즈 목록, 최고 점수), 기능별 메서드 분리
source "$(dirname "$0")/lib.sh"
start_log "10. QuizGame 클래스와 코드 구조"

section "클래스 목록 (요구: 2개 이상)"
run "grep -n '^class ' app/*.py"
check "클래스가 2개 이상" "test \$(grep -h '^class ' app/*.py | wc -l) -ge 2"

section "QuizGame 메서드 (기능별 분리)"
run "grep -n '    def ' app/quiz_game.py"

section "QuizGame 속성"
run "grep -n 'self\.[a-z_]* = ' app/quiz_game.py | head -12"

section "파일별 줄 수"
run "wc -l main.py app/*.py"
finish
