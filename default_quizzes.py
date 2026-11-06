"""state.json이 없거나 손상되었을 때 사용하는 기본 퀴즈 데이터.

주제: 개발 입문 상식 (CLI · Git · Python)
"""

from quiz import Quiz


def create_default_quizzes():
    """기본 퀴즈 목록을 Quiz 인스턴스 리스트로 만들어 돌려준다.

    호출할 때마다 새 리스트를 만들어서, 게임 중 수정해도 원본이 오염되지 않는다.
    """
    return [
        Quiz(
            "현재 작업 중인 디렉터리의 절대 경로를 출력하는 명령어는?",
            ["ls", "cd", "pwd", "whoami"],
            3,
            "print working directory의 약자입니다.",
        ),
        Quiz(
            "Git에서 변경된 파일을 스테이징 영역(Staging Area)에 올리는 명령어는?",
            ["git commit", "git add", "git push", "git init"],
            2,
            "'더한다'는 뜻의 영어 단어입니다.",
        ),
        Quiz(
            "원격 저장소의 변경 사항을 가져와 현재 브랜치에 병합하는 명령어는?",
            ["git pull", "git clone", "git fetch", "git push"],
            1,
            "당겨 온다(pull)는 뜻입니다.",
        ),
        Quiz(
            "Python에서 클래스의 인스턴스가 생성될 때 자동으로 호출되는 메서드는?",
            ["__str__", "__main__", "__call__", "__init__"],
            4,
            "initialize(초기화)의 줄임말입니다.",
        ),
        Quiz(
            "Python 표준 라이브러리 중 JSON 파일을 읽고 쓸 때 사용하는 모듈은?",
            ["pickle", "csv", "json", "os"],
            3,
            "JavaScript Object Notation의 약자 그대로입니다.",
        ),
        Quiz(
            "실행 중인 Docker 컨테이너 목록을 확인하는 명령어는?",
            ["docker images", "docker ps", "docker run", "docker build"],
            2,
            "리눅스에서 프로세스 목록을 볼 때 쓰는 명령어 이름과 같습니다.",
        ),
        Quiz(
            "Git에서 새 브랜치를 만들고 동시에 그 브랜치로 이동하는 명령어는?",
            ["git branch -d feat", "git merge feat", "git checkout -b feat", "git switch feat"],
            3,
            "-b 옵션이 '만들기'를 담당합니다.",
        ),
    ]
