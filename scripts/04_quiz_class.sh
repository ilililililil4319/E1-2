#!/usr/bin/env bash
# 04. Quiz 클래스: 속성(question, choices, answer), 메서드(출력, 정답 확인)
source "$(dirname "$0")/lib.sh"
start_log "04. Quiz 클래스"

section "클래스 정의 확인"
run "grep -n 'class Quiz\|    def ' app/quiz.py"

section "Quiz 객체 만들어 보기"
run "$PY - <<'PY'
from app.quiz import Quiz

q = Quiz('Python의 창시자는?', ['Guido', 'Linus', 'Bjarne', 'James'], 1)
q.display(1)
print()
print('is_correct(1) →', q.is_correct(1))
print('is_correct(3) →', q.is_correct(3))
print('answer_text() →', q.answer_text())
print('to_dict() →', q.to_dict())
PY"

section "잘못된 Quiz는 만들 수 없다 (선택지 3개 → ValueError)"
try "$PY -c \"from app.quiz import Quiz; Quiz('문제', ['a', 'b', 'c'], 1)\""
check "선택지 3개면 ValueError" "! $PY -c \"from app.quiz import Quiz; Quiz('q', ['a','b','c'], 1)\""
finish
