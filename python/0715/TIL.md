# Git 기본기

1.readme.md

- 프로젝트에 대한 설명 문서
- github 프로젝트에서 가장먼저 보는 문서
- sw와 함께 배포
- 형식 따로 없음

2.Repository

- 저장소
- **git init** 명령어로 로컬 *저장소*를 생성

3.readme.md 생성

- 특정버전으로 남긴다 = "커밋(Commit)"한다.
  - working directory = 내가 작업하고 있는 실제 디렉토리
  - staging Area = 커밋으로 남기고 싶은, 특정버전으로 관리하고 싶은 파일이 있는곳
  - Repository = 커밋들이 저장되는 곳

---

git add -> git commit ->  커밋된 이후에 변경사항 알아서 관리해줌.

git status - 관리되는 파일들의 상태를 알 수 있음.



# 터미널을 사용할때(CLI) 현재 작업경로가 내가 원하는 경로와 맞는지를 꼭 확인하세요!!

git config --global user.name "깃허브 username"

git config --global user.email "깃허브 email"



readme.md

git add. : 현재 작업영역의 모든 파일 staging area에 올리기

git commit -m " 커밋메세지" : staging area 에 있는 관리 대상 파일 모두comit, -m은 메세지를 남길수 있는 옵션입니다. 

git remote add origin "깃허브 레포지토리 url" : 어떤 원격 저장소에 깃 작업을 할 건지 등록

git push origin master : 내가 지금까지 커밋한 내용(파일들) 원격 저장소에 업데이트

토큰 알아서 받고, 토큰 다시보기 불가능 영구 저장해놓기

expiration date : 토큰의 만료 기간

권한 설정 :  repo 부분만 체크(저장소 관련 권한)

__git clone "깃허브 레포지토리 url" : 해당 원격 저장소에 있는 파일들 현재 작업 영역으로 복사.__

## __star__

## commit 하기전에 꼭 pull 을 통해서 원격 레포지토리와 로컬 레포지토리의 정보를 최신화

1일 1commit

commit 하고 push 하면 업데이트 된다.







