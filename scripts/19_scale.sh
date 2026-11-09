#!/usr/bin/env bash
# 19. 대량 데이터(1000건 이상) 성능: 저장·불러오기·목록·검색·출제 시간과 메모리, 실제 게임 실행
source "$(dirname "$0")/lib.sh"
start_log "19. 대량 데이터 성능 (1,000 ~ 100,000건)"
note "질문: 퀴즈가 1,000개 이상으로 늘어나면 느려지거나 메모리가 부족해지지 않을까?"
note "방법: 실제 게임 코드(Quiz, StateStorage, QuizGame)로 퀴즈 N개짜리 파일을 만들어 시간을 잰다. (3번 재서 가장 빠른 값)"

section "측정 환경"
run "$PY --version"
run "nproc && free -h | head -2"

section "규모별 측정 (1,000 / 10,000 / 100,000건)"
run "$PY scripts/bench_scale.py 1000 10000 100000"

section "실제 게임으로 확인: 퀴즈 1,000개 파일을 불러와 목록 보기 → 10문제 풀기"
reset_demo
run "$PY - <<'PY'
import json
quizzes = [{'question': f'테스트 문제 {i}번', 'choices': ['가', '나', '다', '라'], 'answer': i % 4 + 1, 'hint': ''}
           for i in range(1000)]
json.dump({'quizzes': quizzes, 'best_score': None}, open('.demo/state.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('퀴즈', len(quizzes), '개 파일 생성')
PY"
run "ls -lh .demo/state.json"
run "time (printf '3\n1\n10\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n7\n' | $PY main.py > .demo/out.txt)"
run "grep -E '불러왔습니다|총 1000개|결과:' .demo/out.txt"
check "1,000개 파일을 불러와 목록에 총 1000개 표시" "grep -q '총 1000개' .demo/out.txt"
check "10문제 풀기 결과 출력" "grep -q '10문제 중' .demo/out.txt"
check "1,000개 불러오기가 1초 이내" "$PY -c \"
import time, sys; sys.path.insert(0, '.')
from app.storage import StateStorage
t = time.perf_counter(); StateStorage('.demo/state.json').load(); assert time.perf_counter() - t < 1
\""
finish
