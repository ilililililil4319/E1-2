# 00. 실행 환경

> 이 파일은 `scripts/00_env.sh`가 자동으로 만든 실행 기록입니다. `$` 뒤가 입력한 명령, 그 아래가 실제 출력입니다.
>
> - 실행 시각: 2026-11-09 23:02:27 KST
> - 실습 데이터: `.demo/state.json` (QUIZ_STATE_PATH), 랜덤 고정값 QUIZ_SEED=42
> - 개인정보 마스킹: 이메일·토큰은 `****`, 홈 경로는 `~`

## 운영체제

```console
$ uname -srm
Linux 6.18.54.1-microsoft-standard-WSL2 x86_64
```

```console
$ grep PRETTY_NAME /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
```

## Python (요구: 3.10 이상, 외부 라이브러리 없음)

```console
$ python3 --version
Python 3.14.4
```

```console
$ which python3
/usr/bin/python3
```
- ✅ Python 3.10 이상

## Git

```console
$ git --version
git version 2.53.0
```

```console
$ git config user.name
ilililililil4319
```

```console
$ git config user.email
****@****
```

```console
$ git config init.defaultBranch || echo '(설정 안 됨: 기본값 사용)'
main
```

## Docker (이번 미션에서는 필수 아님)

```console
$ docker --version
Docker version 29.9.2, build a82e528
```

## 작업 위치와 원격 저장소

```console
$ pwd
~/codyssey/E1-2
```

```console
$ git remote -v
origin	git@github.com:ilililililil4319/E1-2.git (fetch)
origin	git@github.com:ilililililil4319/E1-2.git (push)
```

```console
$ git status -sb | head -1
## main...origin/main
```

---

**결과: 모든 단계 통과 ✅**
