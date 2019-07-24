# 추상 클래스 사용하기
# StudentBase를 상속받은 Student에서는 study 메서드만 구현하고, go_to_school
# 메서드는 구현하지 않았으므로 에러가 발생합니다.
# 따라서 추상 클래스를 상속받았다면 @abstractmethod가 붙은 추상 메서드를 모두
# 구현해야 합니다.
from abc import *
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()
james.go_to_school()

# 추상 메서드를 빈 메서드로 만드는 이유
# 한 가지 중요한 점이 있는데 추상 클래스는 인스턴스로 만들 수가 없다는 점입니다.
# 다음과 같이 추상 클래스 StudentBase로 인스턴스를 만들면 에러가 발생합니다.
james = StudentBase()
# 그래서 지금까지 추상 메서드를 만들 때 pass만 넣어서 빈 메서드로 만든 것입니다.
# 왜냐하면 추상 클래스는 인스턴스를 만들 수 없으니 추상 메서드도 호출할 일이 없기 때문이죠.