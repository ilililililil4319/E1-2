#!/usr/bin/env bash
# 11. 파일 저장/불러오기(state.json): 없음 → 기본 데이터, 저장·재실행, 손상 → 복구, UTF-8
source "$(dirname "$0")/lib.sh"
start_log "11. 파일 저장/불러오기 (state.json)"
reset_demo

section "파일이 없을 때 (첫 실행) → 기본 퀴즈 사용 + 파일 생성"
run "ls .demo"
play '7\n'
run "ls -l .demo"

section "저장된 파일 내용 (UTF-8, 한글 그대로)"
run "head -n 12 .demo/state.json"
try "file .demo/state.json"
check "UTF-8로 읽힌다" "$PY -c \"open('.demo/state.json', encoding='utf-8').read()\""
check "quizzes, best_score 키가 있다" "$PY -c \"import json;d=json.load(open('.demo/state.json',encoding='utf-8'));assert 'quizzes' in d and 'best_score' in d\""

section "다시 실행 → 저장된 데이터를 불러온다"
play '7\n'

section "파일이 손상된 경우 (JSON 문법 오류) → 백업 후 기본 데이터로 복구"
run "echo '{망가진 파일' > .demo/state.json && cat .demo/state.json"
play '7\n'
run "ls .demo && cat .demo/state.json.bak"
check "손상 파일이 .bak으로 백업됨" "test -f .demo/state.json.bak"
check "새 state.json은 정상 JSON" "$PY -m json.tool .demo/state.json"

section "구조가 틀린 경우 (선택지 1개) → 복구"
put_state '{"quizzes": [{"question": "x", "choices": ["a"], "answer": 1}], "best_score": 0}'
play '7\n'

section "예전 형식(hint, history 없음)도 읽을 수 있다"
put_state '{"quizzes": [{"question": "Python의 창시자는?", "choices": ["Guido", "Linus", "Bjarne", "James"], "answer": 1}], "best_score": 3}'
play '3\n4\n7\n'

section "기본 저장 위치: 프로젝트 루트의 state.json"
run "grep -n 'DEFAULT_STATE_PATH\|QUIZ_STATE_PATH' main.py"
note "실습 스크립트는 QUIZ_STATE_PATH로 .demo/state.json을 쓰고, 평소 python3 main.py 실행은 루트의 state.json을 쓴다."
finish
