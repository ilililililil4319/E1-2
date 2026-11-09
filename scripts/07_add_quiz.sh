#!/usr/bin/env bash
# 07. 퀴즈 추가: 문제·선택지 4개·정답 번호 입력, 잘못된 입력 처리, 파일 저장
source "$(dirname "$0")/lib.sh"
start_log "07. 퀴즈 추가"
reset_demo

section "새 퀴즈 추가 (빈 문제, 정답 0, abc 입력을 섞어서)"
note "입력 순서: 2(추가) → Enter(빈 문제) → 문제 → 선택지 4개 → 0 → abc → 2(정답) → 힌트 → 7(종료)"
play '2\n\n영화 기생충의 감독은?\n박찬욱\n봉준호\n김기덕\n이창동\n0\nabc\n2\n칸 영화제 황금종려상 수상자\n7\n'

section "파일에 저장되었는지 확인"
run "$PY -c \"import json; d=json.load(open('.demo/state.json', encoding='utf-8')); print(len(d['quizzes']), '개'); print(json.dumps(d['quizzes'][-1], ensure_ascii=False, indent=2))\""
check "8번째 퀴즈로 저장됨" "$PY -c \"import json;d=json.load(open('.demo/state.json',encoding='utf-8'));assert len(d['quizzes'])==8 and d['quizzes'][-1]['answer']==2\""

section "프로그램을 다시 실행해도 남아 있다"
play '3\n7\n'
finish
