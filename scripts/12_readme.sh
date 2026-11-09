#!/usr/bin/env bash
# 12. README.md 필수 항목 확인
source "$(dirname "$0")/lib.sh"
start_log "12. README.md 필수 항목"

section "목차(## 제목) 목록"
run "grep -n '^## ' README.md"

section "미션 필수 항목 확인"
check "프로젝트 개요" "grep -q '프로젝트 개요' README.md"
check "퀴즈 주제와 선정 이유" "grep -q '선정 이유' README.md"
check "실행 방법" "grep -q '실행 방법' README.md"
check "기능 목록" "grep -q '기능 목록' README.md"
check "파일 구조" "grep -q '파일 구조' README.md"
check "데이터 파일 설명 (state.json 경로/역할/스키마)" "grep -q 'state.json' README.md && grep -q '스키마' README.md"
finish
