# 지금까지 calcpkg 패키지의 모듈을 가져올 때 import calcpkg.operation처럼 import
# 패키지.모듈 형식으로 가져왔습니다. 그러면 import calcpkg처럼 import 패키지 형식으로
# 패키지만 가져와서 모듈을 사용할 수는 없을까요?
# 이때는 calcpkg 패키지의 __init__.py 파일을 다음과 같이 수정합니다.


from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

# 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
from .operation import add, mul
from .geometry import triangle_area, rectangle_area

from .operation import *    # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
from .geometry import *     # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴

__all__ = ['add', 'triangle_area']  # calcpkg 패키지에서 add, triangle_area 함수만 공개

from .operation import *  # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
from .geometry import *  # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴

