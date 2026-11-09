# 환경 세팅 (Windows + WSL2 Ubuntu 기준)

이 문서는 "처음 받은 Windows PC에서 이 저장소를 실행할 수 있게 되기까지"를 순서대로 적은 것이다.
macOS/Linux라면 3번(WSL)을 건너뛰고 터미널에서 4번부터 하면 된다.

## 1. 준비물

| 도구 | 용도 | 확인 명령 |
| --- | --- | --- |
| WSL2 + Ubuntu | Windows 안에서 쓰는 진짜 리눅스 | `wsl -l -v` (PowerShell) |
| Python 3.10 이상 | 퀴즈 게임 실행 | `python3 --version` |
| Git | 버전 관리 | `git --version` |
| VSCode + WSL 확장 | 코드 편집, WSL 터미널 | VSCode 왼쪽 아래 `WSL: Ubuntu` 표시 |
| GitHub SSH 키 | 비밀번호 없이 push | `ssh -T git@github.com` |

Docker는 이번 미션(E1-2)에서는 필요 없다.

## 2. 터미널 구분하기

| 프롬프트 모양 | 어디인가 | 이 미션에서 |
| --- | --- | --- |
| `PS C:\...>` | Windows PowerShell | 쓰지 않는다 (멈추고 WSL 창으로) |
| `아이디@컴퓨터:~$` | WSL Ubuntu | 여기서 모든 명령 실행 |

## 3. WSL2 Ubuntu 설치 (처음 한 번)

PowerShell을 **관리자 권한**으로 열고:

```powershell
wsl --install -d Ubuntu
```

재부팅 후 Ubuntu가 열리면 사용자 이름과 비밀번호를 만든다. (비밀번호는 입력해도 화면에 안 보이는 것이 정상)

## 4. Python, Git 설치 확인 (Ubuntu 터미널)

```bash
sudo apt update
sudo apt install -y python3 git
python3 --version   # Python 3.10 이상이면 OK (Ubuntu 24.04는 3.12)
git --version
```

## 5. Git 사용자 설정 (처음 한 번)

```bash
git config --global user.name "ilililililil4319"
git config --global user.email "GitHub에 등록한 이메일"
git config --global init.defaultBranch main
git config --list
```

## 6. GitHub SSH 연결 (처음 한 번)

질문하는 명령이므로 **한 줄씩** 입력한다.

```bash
ssh-keygen -t ed25519 -C "GitHub에 등록한 이메일"
```

- 저장 위치를 물으면 그냥 Enter
- passphrase는 Enter 두 번(없음) 또는 원하는 암호

```bash
cat ~/.ssh/id_ed25519.pub
```

출력된 **공개키**(`.pub`)를 GitHub → Settings → SSH and GPG keys → New SSH key에 붙여 넣는다.
개인키(`id_ed25519`, `.pub` 없는 파일)는 절대 다른 곳에 올리지 않는다.

```bash
ssh -T git@github.com
```

`Hi ilililililil4319! You've successfully authenticated` 가 나오면 성공. (처음 접속 시 yes 입력)

## 7. 저장소 내려받기와 실행

Windows 폴더(`/mnt/c/...`)가 아니라 **Ubuntu 홈 폴더 아래**에 받는다. Windows 폴더에서는 `chmod` 등이 제대로 동작하지 않는다.

```bash
mkdir -p ~/codyssey && cd ~/codyssey
git clone git@github.com:ilililililil4319/E1-2.git
cd E1-2
code .                 # VSCode(WSL)로 열기
python3 main.py        # 게임 실행
```

## 8. 실습 스크립트로 증거 남기기

```bash
bash scripts/run_all.sh         # 00~18 전부 실행 → 마지막에 "완료!"
bash scripts/06_play.sh         # 하나만 다시 실행할 때
```

결과는 `docs/logs/NN_이름.md`에 자동 저장된다. 그다음:

```bash
git pull
git add .
git commit -m "Docs: 실행 로그 추가"
git push
```

## 9. 공용 PC를 떠날 때

```bash
git config --global --unset user.name
git config --global --unset user.email
```

VSCode와 브라우저의 GitHub 계정도 로그아웃한다.
