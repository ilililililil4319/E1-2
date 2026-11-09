# 19. 대량 데이터 성능 (1,000 ~ 100,000건)

> 이 파일은 `scripts/19_scale.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:43:43 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

질문: 퀴즈가 1,000개 이상으로 늘어나면 느려지거나 메모리가 부족해지지 않을까?

방법: 실제 게임 코드(Quiz, StateStorage, QuizGame)로 퀴즈 N개짜리 파일을 만들어 시간을 잰다. (3번 재서 가장 빠른 값)

## 측정 환경

```console
$ python3 --version
Python 3.14.4
```

```console
$ nproc && free -h | head -2
8
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       1.2Gi       6.3Gi       4.1Mi       343Mi       6.5Gi
```

## 규모별 측정 (1,000 / 10,000 / 100,000건)

```console
$ python3 scripts/bench_scale.py 1000 10000 100000
| 퀴즈 수 | 파일 크기 | 저장 | 불러오기 | 불러올 때 메모리 | 목록 출력 | 검색(전체 훑기) | 10문제 뽑기 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1,000 | 244 KB | 7.6 ms | 2.3 ms | 1.2 MB | 0.3 ms | 0.15 ms | 0.004 ms |
| 10,000 | 2.4 MB | 71.5 ms | 27.5 ms | 11.4 MB | 3.1 ms | 1.54 ms | 0.003 ms |
| 100,000 | 24.9 MB | 750.2 ms | 406.7 ms | 115.1 MB | 29.9 ms | 15.46 ms | 0.004 ms |
```

## 실제 게임으로 확인: 퀴즈 1,000개 파일을 불러와 목록 보기 → 10문제 풀기

```console
$ rm -rf .demo && mkdir -p .demo
```

```console
$ python3 - <<'PY'
import json
quizzes = [{'question': f'테스트 문제 {i}번', 'choices': ['가', '나', '다', '라'], 'answer': i % 4 + 1, 'hint': ''}
           for i in range(1000)]
json.dump({'quizzes': quizzes, 'best_score': None}, open('.demo/state.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('퀴즈', len(quizzes), '개 파일 생성')
PY
퀴즈 1000 개 파일 생성
```

```console
$ ls -lh .demo/state.json
-rw-r--r-- 1 ilililililil4319 ilililililil4319 105K Nov  9 23:43 .demo/state.json
```

```console
$ time (printf '3\n1\n10\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n7\n' | python3 main.py > .demo/out.txt)

real	0m0.047s
user	0m0.034s
sys	0m0.011s
```

```console
$ grep -E '불러왔습니다|총 1000개|결과:' .demo/out.txt
📂 저장된 데이터를 불러왔습니다. (퀴즈 1000개, 최고점수 없음)
📋 등록된 퀴즈 목록 (총 1000개)
🏆 결과: 10문제 중 5문제 정답! (50점)
```
- ✅ 1,000개 파일을 불러와 목록에 총 1000개 표시
- ✅ 10문제 풀기 결과 출력
- ✅ 1,000개 불러오기가 1초 이내

---

**결과: 모든 단계 통과 ✅**
