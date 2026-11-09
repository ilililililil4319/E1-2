"""대량 데이터 성능 측정: 퀴즈 N개짜리 state.json을 만들어 저장·불러오기·목록·검색·출제 시간과 메모리를 잰다.

사용: python3 scripts/bench_scale.py 1000 10000 100000
- 실제 게임 코드(Quiz, StateStorage, QuizGame)를 그대로 사용한다
- 측정 파일은 .demo/scale_<N>.json (실제 기록 state.json은 건드리지 않음)
- 시간은 3번 재서 가장 빠른 값(다른 프로그램 영향 최소화)
"""

import contextlib
import io
import os
import random
import sys
import time
import tracemalloc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from app.quiz import Quiz  # noqa: E402
from app.quiz_game import QuizGame  # noqa: E402
from app.storage import StateStorage  # noqa: E402

DEMO = os.path.join(ROOT, ".demo")


def best_ms(func, repeat=3):
    best = None
    for _ in range(repeat):
        start = time.perf_counter()
        func()
        elapsed = (time.perf_counter() - start) * 1000
        best = elapsed if best is None else min(best, elapsed)
    return best


def make_quizzes(n):
    return [
        Quiz(f"테스트 문제 {i}번: 다음 중 정답은?", [f"보기 {i}-{k}" for k in range(1, 5)], i % 4 + 1, f"힌트 {i}")
        for i in range(n)
    ]


def measure(n):
    path = os.path.join(DEMO, f"scale_{n}.json")
    storage = StateStorage(path)
    quizzes = make_quizzes(n)

    save_ms = best_ms(lambda: storage.save(quizzes, None, 0, 0, []))
    size_kb = os.path.getsize(path) / 1024
    load_ms = best_ms(storage.load)

    tracemalloc.start()
    loaded = storage.load()["quizzes"]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    game = QuizGame(storage)
    game.quizzes = loaded
    with contextlib.redirect_stdout(io.StringIO()):
        list_ms = best_ms(game.list_quizzes)
    search_ms = best_ms(lambda: [q for q in loaded if f"{n - 1}번" in q.question])
    sample_ms = best_ms(lambda: random.sample(loaded, 10))

    os.remove(path)
    return n, size_kb, save_ms, load_ms, peak / 1024 / 1024, list_ms, search_ms, sample_ms


def main():
    os.makedirs(DEMO, exist_ok=True)
    random.seed(42)
    sizes = [int(x) for x in sys.argv[1:]] or [1000, 10000]
    print("| 퀴즈 수 | 파일 크기 | 저장 | 불러오기 | 불러올 때 메모리 | 목록 출력 | 검색(전체 훑기) | 10문제 뽑기 |")
    print("| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for n in sizes:
        n, size_kb, save_ms, load_ms, mem_mb, list_ms, search_ms, sample_ms = measure(n)
        size = f"{size_kb:,.0f} KB" if size_kb < 1024 else f"{size_kb / 1024:,.1f} MB"
        print(
            f"| {n:,} | {size} | {save_ms:,.1f} ms | {load_ms:,.1f} ms | {mem_mb:,.1f} MB "
            f"| {list_ms:,.1f} ms | {search_ms:,.2f} ms | {sample_ms:,.3f} ms |"
        )


if __name__ == "__main__":
    main()
