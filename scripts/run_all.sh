#!/usr/bin/env bash
# 모든 실습 스크립트를 번호 순서대로 실행한다. 하나라도 실패하면 [중단]하고 멈춘다.
# 사용: bash scripts/run_all.sh
cd "$(dirname "$0")/.." || exit 1

for script in scripts/[0-9][0-9]_*.sh; do
    if ! bash "$script"; then
        printf '\n\033[31m[중단]\033[0m %s 에서 멈췄습니다. 위 오류 화면을 캡처해 주세요.\n' "$script"
        exit 1
    fi
done

rm -rf .demo
printf '\n\033[1;32m완료!\033[0m 로그: docs/logs/ (%s개)\n' "$(ls docs/logs/*.md | wc -l)"
echo "다음 단계: git pull → git add . → git commit -m \"Docs: 실행 로그 추가\" → git push"
