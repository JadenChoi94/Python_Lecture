# import로 모듈 가져오기
import math
math.pi #static method

import math as m    # math 모듈을 가져오면서 이름을 m으로 지정
m.sqrt(4.0)

from math import pi
pi

from math import sqrt    # math 모듈에서 sqrt 함수만 가져옴
sqrt(4.0)                # sqrt 함수를 바로 사용
sqrt(2.0)                # sqrt 함수를 바로 사용
# 다 가져오기
from math import *
pi

# from import로 모듈의 일부를 가져온 뒤 이름 지정하기
from math import sqrt as s # math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정
s(4.0)

# 가져온 모듈 해제하기, 다시 가져오기
import math
del math
importlib.reload(math) # 모듈을 다시 가져오려면 importlib.reload를 사용합니다.

# import로 패키지 가져오기
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
response.status # urlopen 함수

# import as로 패키지 모듈 이름 지정하기
import urllib.request as r  # urllib 패키지의 request 모듈을 가져오면서 이름을 r로 지정
response = r.urlopen('http://www.google.co.kr')    # r로 urlopen 함수 사용
response.status

# from import로 패키지의 모듈에서 일부만 가져오기
from urllib.request import Request, urlopen    # urlopen 함수, Request 클래스를 가져옴
req = Request('http://www.google.co.kr')       # Request 클래스를 사용하여 req 생성
response = urlopen(req)                        # urlopen 함수 사용
response.status

#  from import로 패키지의 모듈의 일부를 가져온 뒤 이름 지정하기
from urllib.request import Request as r, urlopen as u
req = r('http://www.google.co.kr')    # r로 Request 클래스 사용
response = u(req)                     # u로 urlopen 함수 사용
response.status

# 파이썬 패키지 인덱스에서 패키지 설치하기
# pip 설치하기 (윈도우는 내장되있음)

# Windows에서는 명령 프롬프트를 실행(윈도우 키+R을 누른 뒤 cmd를 입력)하고, 리눅스와
# macOS에서는 콘솔(터미널)을 실행한 뒤 pip install requests 명령을 입력합니다(pip
# 명령은 파이썬 셸 >>>에 입력하면 안 됩니다. 반드시 명령 프롬프트, 콘솔, 터미널에
# 입력해주세요).
# 참고로 requests는 파이썬 표준 라이브러리의 urllib.request와 비슷한 역할을 하는
# 패키지인데 좀 더 기능이 많고 편리합니다.

# import로 패키지 가져오기
import requests                                # pip로 설치한 requests 패키지를 가져옴
r = requests.get('http://www.google.co.kr')    # requests.get 함수 사용
r.status_code

# 파이썬 3가 기본 설치된 경우에는 pip가 파이썬 3용 명령
$ sudo python3 -m pip install 패키지
$ sudo pip3 install 패키지

# pip search 패키지: 패키지 검색
# pip install 패키지==버전: 특정 버전의 패키지를 설치(예: pip install requests==2.9.0)
# pip list 또는 pip freeze: 패키지 목록 출력
# pip uninstall 패키지: 패키지 삭제

