# 정규표현식 사용하기
import re
re.match('Hello', 'Hello, world!')   # 문자열이 있으므로 정규표현식 매치 객체가 반환됨
re.match('Python', 'Hello, world!')  # 문자열이 없으므로 아무것도 반환되지 않음

# 문자열이 있으면 매치(SRE_Match) 객체가 반환되고 없으면 아무것도 반환되지 않습니다.
# 여기서는 'Hello'가 있으므로 match='Hello'와 같이 패턴에 매칭된 문자열이 표시됩니다.
# 사실 이런 판단은 'Hello, world!'.find('Hello')처럼 문자열 메서드로도 충분히 가능합니다.
# 이제부터 문자열 메서드로 할 수 없는 판단을 해보겠습니다.

# 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기
# ^문자열 시작
# 문자열$ 끝
# re.search('패턴', '문자열')
# [^ ] not이라는 의미
re.search('^Hello', 'Hello, world!')  # Hello로 시작하므로 패턴에 매칭됨
re.search('world!$', 'Hello, world!')    # world!로 끝나므로 패턴에 매칭됨

# 지정된 문자열이 하나라도 포함되는지 판단하기
# |는 특정 문자열에서 지정된 문자열(문자)이 하나라도 포함되는지 판단합니다.
# 기본 개념은 OR 연산자와 같습니다.
# 문자열|문자열
# 문자열|문자열|문자열|문자열
re.match('hello|world', 'hello')    # hello 또는 world가 있으므로 패턴에 매칭됨

# 범위 판단하기
re.match('[0-9]*', '1234')    # 1234는 0부터 9까지 숫자가 0개 이상 있으므로 패턴에 매칭됨
re.match('[0-9]+', '1234')  # 1234는 0부터 9까지 숫자가 1개 이상 있으므로 패턴에 매칭됨
re.match('[0-9]+', 'abcd')    # abcd는 0부터 9까지 숫자가 1개 이상 없으므로 패턴에 매칭되지 않음
re.match('a*b', 'b')      # b에는 a가 0개 이상 있으므로 패턴에 매칭됨
re.match('a+b', 'b')      # b에는 a가 1개 이상 없으므로 패턴에 매칭되지 않음
re.match('a*b', 'aab')    # aab에는 a가 0개 이상 있으므로 패턴에 매칭됨
re.match('a+b', 'aab')    # aab에는 a가 1개 이상 있으므로 패턴에 매칭됨

# 문자가 한 개만 있는지 판단하기
re.match('H?', 'H')     # H 뒤에 문자가 0개 또는 1개이므로 패턴에 매칭됨
re.match('H?', 'Hi')    # H 뒤에 문자가 0개 또는 1개이므로 패턴에 매칭됨
re.match('H.', 'Hi')    # H 뒤에 문자가 1개 있으므로 패턴에 매칭됨

# 문자 개수 판단하기
re.match('h{3}', 'hhhello')
re.match('(hello){3}', 'hellohellohelloworld')

# 다음은 휴대전화의 번호 형식에 맞는지 판단합니다.
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000')    # 숫자 3개-4개-4개 패턴에 매칭됨
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100')  # 숫자 3개-4개-4개 패턴에 매칭되지 않음

# 다음은 일반전화의 번호 형식에 맞는지 판단합니다.
re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000')  # 2~3개-3~4개-4개 패턴에 매칭됨
re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000')  # 2~3개-3~4개-4개 패턴에 매칭되지 않음

# 숫자와 영문 문자를 조합해서 판단하기
re.match('[a-zA-Z0-9]+', 'Hello1234')    # a부터 z, A부터 Z, 0부터 9까지 1개 이상 있으므로
re.match('[A-Z0-9]+', 'hello')    # 대문자, 숫자는 없고 소문자만 있으므로 패턴에 매칭되지 않음

# 한글은?
re.match('[가-힣]+', '홍길동')    # 가부터 힣까지 1개 이상 있으므로 패턴에 매칭됨

# 특정 문자 범위에 포함되지 않는지 판단하기
re.match('[^A-Z]+', 'Hello')    # 대문자를 제외. 대문자가 있으므로 패턴에 매칭되지 않음
re.match('[^A-Z]+', 'hello')  # 대문자를 제외. 대문자가 없으므로 패턴에 매칭됨
re.search('^[A-Z]+', 'Hello')  # 대문자로 시작하므로 패턴에 매칭됨, '^[A-Z]+'는 영문 대문자로 시작하는지 판단합니다

# 특수 문자 판단하기
re.search('\*+', '1 ** 2')  # *이 들어있는지 판단
re.match('[$()a-zA-Z0-9]+', '$(document)')    # $, (, )와 문자, 숫자가 들어있는지 판단

re.match('\d+', '1234')          # 모든 숫자이므로 패턴에 매칭됨
re.match('\D+', 'Hello')         # 숫자를 제외한 모든 문자이므로 패턴에 매칭됨
re.match('\w+', 'Hello_1234')    # 영문 대소문자, 숫자, 밑줄 문자이므로 패턴에 매칭됨
re.match('\W+', '(:)')    # 영문 대소문자, 숫자, 밑줄문자를 제외한 모든 문자이므로 패턴에 매칭됨

# 공백 처리하기
re.match('[a-zA-Z0-9 ]+', 'Hello 1234')     # ' '로 공백 표현
re.match('[a-zA-Z0-9\s]+', 'Hello 1234')    # \s로 공백 표현

# 같은 정규표현식 패턴을 자주 사용할 때
p = re.compile('[0-9]+')    # 정규표현식 패턴을 객체로 만듦
p.match('1234')             # 정규표현식 패턴 객체에서 match 메서드 사용
p.search('hello')           # 정규표현식 패턴 객체에서 search 메서드 사용


# 그룹 사용하기
m = re.match('([0-9]+) ([0-9]+)', '10 295')
m.group(1)  # 첫 번째 그룹(그룹 1)에 매칭된 문자열을 반환
m.group(2)    # 두 번째 그룹(그룹 2)에 매칭된 문자열을 반환
m.group()     # 매칭된 문자열을 한꺼번에 반환
m.group(0)  # 매칭된 문자열을 한꺼번에 반환
m.groups()  # 각 그룹에 해당하는 문자열을 튜플 형태로 반환하는 메소드

m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
m.group('func')    # 그룹 이름으로 매칭된 문자열 출력
m.group('arg')  # 그룹 이름으로 매칭된 문자열 출력
# (?P<func>)와 (?P<arg>)처럼 각 그룹에 이름을 짓고 m.group('func'), m.group('arg')로
# 매칭된 문자열을 출력했습니다. 참고로 함수 이름은 문자로만 시작해야 하므로 첫글자는
# [a-zA-Z_]로 판단해줍니다. 또한, print 뒤에 붙은 (, )는 정규표현식에 사용하는 특수
# 문자이므로 앞에 \를 붙여줍니다.

# 패턴에 매칭되는 모든 문자열 가져오기
re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')

# 문자열 바꾸기, re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
re.sub('apple|orange', 'fruit', 'apple box orange tree')    # apple 또는 orange를 fruit로 바꿈
re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')    # 숫자만 찾아서 n으로 바꿈


def multiple10(m):        # 매개변수로 매치 객체를 받음
    n = int(m.group())    # 매칭된 문자열을 가져와서 정수로 변환
    return str(n * 10)    # 숫자에 10을 곱한 뒤 문자열로 변환해서 반환

re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8')

# 찾은 문자열을 결과에 다시 사용하기
re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234')    # 그룹 2, 1, 2, 1 순으로 바꿈
re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }')