#__init__.py
#패키지가 로드할 때 실행되는 초기화 파일


#1. 패키지를 import 할 때 실행되어야 한ㄴ 초기화 코드(환경 확인, 설정값 로드)

print("__init__")

#2. 페키지 메타데이터 설정 
VERSION = "1.0.0"

#3. 패키지 re-export
from mypack.aa import add #절대 임퐅트
임포트