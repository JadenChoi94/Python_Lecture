import square2  # import로 square2 모듈을 가져옴

'''
print(square2.base)  # 모듈.변수 형식으로 모듈의 변수 사용
print(square2.square(10))  # 모듈.함수() 형식으로 모듈의 함수 사용


# from import로 변수, 함수 가져오기
from square2 import base, square
print(base)
square(10)

import person  # import로 person 모듈을 가져옴

# 모듈.클래스()로 person 모듈의 클래스 사용
maria = person.Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

# from import로 클래스 가져오기
from person import Person
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()



# 모듈과 시작점 알아보기
import hello  # hello 모듈을 가져옴
# 실행을 해보면 hello.py 파일과 main.py 파일의 __name__ 변수 값이 출력됩니다.
print('main.py __name__:', __name__)  # __name__ 변수 출력
# 파이썬에서 import로 모듈을 가져오면 해당 스크립트 파일이 한 번 실행됩니다. 따라서
# hello 모듈을 가져오면 hello.py 안의 코드가 실행됩니다. 따라서 hello.py의 __name__
# 변수에는 'hello'가 들어가고, main.py의 __name__ 변수에는 '__main__'이 들어갑니다.


# 스크립트 파일로 실행하거나 모듈로 사용하는 코드 만들기
import calc
calc.add(50, 60)
calc.mul(50, 60)


# 패키지 만들기
import calcpkg.operation  # calcpkg 패키지의 operation 모듈을 가져옴
import calcpkg.geometry  # calcpkg 패키지의 geometry 모듈을 가져옴

print(calcpkg.operation.add(10, 20))  # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))  # operation 모듈의 mul 함수 사용

print(calcpkg.geometry.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용


# from import로 패키지의 모듈에서 변수, 함수, 클래스 가져오기
from calcpkg.operation import add, mul
add(10, 20)
mul(10, 20)


import sys
sys.path

# 패키지에서 from import 응용하기
import calcpkg  # calcpkg 패키지만 가져옴

print(calcpkg.operation.add(10, 20))  # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))  # operation 모듈의 mul 함수 사용

print(calcpkg.geometry.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용



# from import로 패키지에 속한 모든 변수, 함수, 클래스 가져오기
from calcpkg import *  # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))  # operation 모듈의 add 함수 사용
print(mul(10, 20))  # operation 모듈의 mul 함수 사용
print(triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용
# 실행을 해보면 add가 정의되지 않았다면서 에러가 발생합니다. 왜냐하면 __init__.py
# 에서 모듈만 가져왔을 뿐 모듈 안의 함수는 가져오지 않았기 때문입니다.
# 이때는 __init__.py에서 모듈 안의 함수를 가져오게 만들어야 합니다. 특히 현재
# 패키지(calcpkg)라는 것을 명확하게 나타내기 위해 모듈 앞에 .(점)을 붙입니다.


import calcpkg  # calcpkg 패키지만 가져옴

print(calcpkg.add(10, 20))  # 패키지.함수 형식으로 operation 모듈의 add 함수 사용
print(calcpkg.mul(10, 20))  # 패키지.함수 형식으로 operation 모듈의 mul 함수 사용
print(calcpkg.triangle_area(30, 40))  # 패키지.함수 형식으로 geometry 모듈의 triangle_area 함수 사용
print(calcpkg.rectangle_area(30, 40))  # 패키지.함수 형식으로 geometry 모듈의 rectangle_area 함수 사용
'''

# __all__로 필요한 것만 공개하기
from calcpkg import *  # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))  # add 함수는 공개되어 있으므로 사용할 수 있음
print(mul(10, 20))  # 에러: mul 함수는 공개되어 있지 않으므로 사용할 수 없음

print(triangle_area(30, 40))  # triangle_area 함수는 공개되어 있으므로 사용할 수 있음
print(rectangle_area(30, 40))  # 에러: rectangle_area 함수는 공개되어 있으므로 사용할 수 있음
# main.py에서 from calcpkg import *로 패키지의 모든 변수, 함수, 클래스를 가져온다 #
# 하더라도 __all__에 지정된 add, triangle_area 함수만 사용할 수 있습니다. #