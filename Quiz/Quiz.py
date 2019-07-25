# 1
year = int(input('연도를 입력하세요: '))
if year % 4 == 0:
    if year % 400 == 0:
        print('윤년입니다.')
    elif year % 100 == 0:
        print("윤년이 아닙니다.")
    else:
        print("윤년입니다.")
else:
    print('윤년이 아닙니다.')
# 2
hour, minute = map(int, input('시, 분을 입력하세요: ').split())
if hour == 0:
    hour = 24
if minute >= 45:
    print(hour, minute-45)
else:
    print(hour-1, '시', (60+minute)-45, '분')

# 3
sample_list = list(map(int, input('세 숫자를 입력하세요: ').split()))
for i in range(len(sample_list)-1):
    for k in range(i+1, len(sample_list)):
        if sample_list[i] > sample_list[k]:
            sample_list[i], sample_list[k] = sample_list[k], sample_list[i]
print(sample_list[1])

# 4
for a in range(1, 333):
    for b in range(a+1, 500):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print(a, b, c, a+b+c)
'''
# a + b + c = 1000 인 피타고라스 수
# (단, a < b < c 이고 a + b > c)
outerBreak = False
for a in range(1, 333):
    if outerBreak:
        break
    for b in range(a+1, 500):
        c = 1000 - a - b
        if c < b:
            continue
        if a**2 + b**2 == c**2:
            print(a, b, c, a+b+c)
            print(a**2, b**2, c**2)
            outerBreak = True
            break;
'''

# 반복문
# 1
Case = int(input())
for i in range(Case):
    A, B = list(map(int, input().split()))
    print('Case #{}: {} + {} = {}'.format(i+1, A, B, A + B))

# 2
y = int(input('5이상 9이하의 홀수만 입력하세요 :'))
x = int(y/2)+1
for i in range(1, 2*x):
    if i <= x:
        for k in range(x-i):
            print(' ', end='')
        for k in range(2*i-1):
            print('*', end='')
        print()
    else:
        for k in range(i-x):
            print(' ', end='')
        for k in range((2*x-i)*2-1):
            print('*', end='')
        print()

# 3
sumSec=0    # 초의 총합을 저장할 변수
for hour in range(24) :     # 시간
    for minute in range(60) :   #분
        if '3' in str(hour) or '3' in str(minute) : # 시간이나 분에 3이 들어가면
            sumSec += 60            # 60초씩 더함
print(sumSec)

# 4
def dic(num1, num2):
    dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    temp_str=''
    for i in range(num1, num2+1):
        temp_str = temp_str+str(i)
    split_list = list(temp_str)
    for i in range(len(dict)):
        dict[i] = split_list.count(str(i))
    print(dict)
dic(1,1000)

# 5. 완벽수 perfect number
num = int(input("숫자를 입력하세요: "))
for x in range(1, num + 1):
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    if sum == x:
        print(sum)

# 6
foo = int(input("숫자를 입력하세요: "))
b = 0
c = 0
for a in range(foo+1):
    b = b + a * a # 제곱의합
    c = c + a # 합만 우선 계산
c = c * c # 합의제곱
print(c - b)

'''
n = int(input('자연수 입력: '))
sumOfSquare = 0
sum = 0
for i in range(1, n+1):
    sum += i
    sumOfSquare += i ** 2
squareOfSum = sum ** 2
print('합의 제곱 =', squareOfSum)
print('제곱의 합 =', sumOfSquare)
print('차이 =', squareOfSum - sumOfSquare)
'''