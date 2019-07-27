class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person): # 부모이름을 ()안에 써줌
    def study(self):
        print('공부하기')

james = Student()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Student에 추가한 study 메서드

james = Student()
james.greeting()    # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드

# 상속 관계 확인하기
class Person:
     pass
class Student(Person):
     pass
issubclass(Student, Person)

# 상속관계
class Person:
    def greeting(self):
        print('안녕하세요.')
class Student(Person):
    def study(self):
        print('공부하기')

# 포함관계
class Person:
    def greeting(self):
        print('안녕하세요.')
class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리
    def append_person(self, person):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

# 여기서는 상속을 사용하지 않고 속성에 인스턴스를 넣어서 관리하므로 PersonList가
# Person을 포함하고 있습니다. 이러면 사람 목록 PersonList와 사람 Person은 동등한
# 관계가 아니라 포함 관계입니다. 즉, "사람 목록은 사람을 가지고 있다."라고 말할 수
# 있습니다. 그래서 포함 관계를 영어로 has-a 관계라고 부릅니다(PersonList has a Person).

# super()로 기반 클래스 초기화하기
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello) #이젠됨, 원래 기반 클래스의 속성을 출력하려고 하면 에러가 발생함

# 기반 클래스를 초기화하지 않아도 되는 경우
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
class Student(Person):
    pass
james = Student()
print(james.hello)

# 좀 더 명확하게 super 사용하기
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()# super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'


# 메서드 오버라이딩 사용하기
# class Person:
#     def greeting(self):
#         print('안녕하세요.')
#
# class Student(Person):
#     def greeting(self):
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
#
# james = Student()
# james.greeting()

class Person:
    def greeting(self):
        print('안녕하세요.')
class Student(Person):
    def greeting(self):
        super().greeting()  # 기반 클래스의 메서드 호출하여(super) 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')
james = Student()
james.greeting()


# 다중 상속 사용하기
class Person:
    def greeting(self):
        print('안녕하세요.')
class University:
    def manage_credit(self):
        print('학점 관리')
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()  # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드

# 다이아몬드 상속는 안됨!!!!
