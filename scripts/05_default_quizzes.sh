#!/usr/bin/env bash
# 05. 기본 퀴즈 데이터: 선택한 주제로 5개 이상, Quiz 인스턴스로 생성
source "$(dirname "$0")/lib.sh"
start_log "05. 기본 퀴즈 데이터"
note "주제: 개발 입문 상식 (CLI · Git · Python · Docker)"

section "기본 퀴즈 목록"
run "$PY - <<'PY'
from app.default_quizzes import create_default_quizzes
from app.quiz import Quiz

quizzes = create_default_quizzes()
print('개수:', len(quizzes))
print('모두 Quiz 인스턴스:', all(isinstance(q, Quiz) for q in quizzes))
for number, q in enumerate(quizzes, start=1):
    print(f'[{number}] {q.question} → 정답 {q.answer_text()}')
PY"
check "기본 퀴즈 5개 이상" "$PY -c 'from app.default_quizzes import create_default_quizzes as c; assert len(c()) >= 5'"
finish
