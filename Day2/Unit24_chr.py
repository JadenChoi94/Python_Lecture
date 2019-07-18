# replace('바꿀문자열', '새문자열')
'Hello, world!'.replace('world', 'Python')

# translate는 문자열 안의 문자를 다른 문자로 바꿉니다. 먼저 str.maketrans('바꿀문자', '새문자')로
# 변환 테이블을 만듭니다.
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)

# split('기준문자열')
'apple, pear, grape, pineapple, orange'.split(', ') #리스트 형태로 변환

# 구분자 문자열과 문자열 리스트 연결하기
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])

# 소문자 혹은 대문자로 바꾸기
'python'.upper()

# 왼쪽, 오른쪽, 양쪽공백 삭제하기
'   Python   '.lstrip()
'   Python   '.rstrip()
'   Python   '.strip()

# 왼쪽, 오른쪽, 양쪽 특정문자 삭제하기
', python.'.lstrip(',.')
', python.'.rstrip(',.')
', python.'.strip(',.')

# 구두점을 간단하게 삭제하기
# string 모듈의 punctuation에는 모든 구두점이 들어있습니다.
# 다음과 같이 strip 메서드에 string.punctuation을 넣으면 문자열 양쪽의 모든 구두점을 간단하게 삭제할 수 있습니다.
import string
', python.'.strip(string.punctuation)
string.punctuation
', python.'.strip(string.punctuation + ' ') # 공백까지 삭제할 때
', python.'.strip(string.punctuation).strip().upper() # 메서드체이닝

# 문자열을 왼쪽 가운데 양쪽 정렬하기
'python'.ljust(10)
'python'.rjust(10)
'python'.center(10)

# 문자열 왼쪽에 0 채우기
'35'.zfill(4)
'3.5'.zfill(6)
'hello'.zfill(10)

# 문자열 위치 찾기
'apple pineapple'.find('pl')
'apple pineapple'.find('xy') # 해당 문자열이 없으면 -1을 반환

# 오른쪽에서부터 문자열 위치 찾기
'apple pineapple'.rfind('pl') #해당 문자열 인덱스 반환
'apple pineapple'.rfind('xy')

# 문자열 위치 찾기, find, rfind 이외에도 index, rindex로 문자열의 위치를 찾을 수 있습니다.
'apple pineapple'.index('pl')
'apple pineapple'.rindex('pl') #오른쪽에서부터 문자열 위치 찾기

# 문자열 개수 세기
'apple pineapple'.count('pl')

# 서식 지정자로 문자열 넣기
'I am %s.' % 'james' # %d, %f
'%.2f' % 2.3
'%10s' % 'python' #  왼쪽 공간을 공백 4칸으로 채웁니다.

# 자릿수가 다른 숫자 출력하기
'%10d' % 150
'%10d' % 15000
'%10.2f' % 2.3
'%10.2f' % 2000.3
'%-10s' % 'python' # 왼쪽 정렬은 문자열 길이에 -를 붙여주면 됩니다

# 서식 지정자로 문자열 안에 값 여러 개 넣기
'Today is %d%s.' % (3, 'April')
'Hello, {0}'.format('world!')

# 인덱스의 순서와 format에 지정된 값의 순서를 주목해주세요.
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'{0} {0} {1} {1}'.format('Python', 'Script')
'Hello, {} {} {}'.format('Python', 'Script', 3.7)

# { } 중괄호 자체를 출력할 때는 {{, }}처럼 중괄호를 두 번 사용하면 됩니다.
'{{ {0} }}'.format('Python')

# format 메서드로 문자열 정렬하기
'{0:<10}'.format('python')
'{0:>10}'.format('python')
'{:>10}'.format('python')

# 금액에서 천단위로 콤마 넣기
format(1493500, ',')
'%20s' % format(1493500, ',')    # 길이 20, 오른쪽으로 정렬
'{0:,}'.format(1493500)
'{0:0>20,}'.format(1493500)    # 길이 20, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
