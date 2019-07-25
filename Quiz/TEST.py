
# 3번
num = list(map(int, input().split()))
numbers = sorted(num)
oddSum = 0
for i in range(numbers[0], numbers[1]+1):
    if i % 2 == 1:
        oddSum += i
    else:
        print()
print(oddSum)

# 4번
# principal 초기 금액
# rate      이자율
principal, rate = map(float, input().split())
year = 0
while True:
    year += 1
    principal = principal * ((1 + rate)**year)
    if principal == 2*principal:
        break
print(year)

# 5번
bts = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']
print(bts[-2])
print(bts[:1])
print(bts[5:7])
print(bts[2:5])
print(bts[:1]+bts[2:3]+bts[4:5]+bts[6:7])

# 6번
import operator
vegetables = {'가지': 800, '오이': 600, '수박': 15000, '호박': 1000, '깻잎': 500}
svegi = sorted(vegetables.items(), key = operator.itemgetter(1), reverse=True)
svegi
for key, value in svegi:
   print(key,':','%7s' % format(value, ','))

# 7번
M = 0
for i in range(999, 99, -1):
    for k in range(999, i-1, -1):
        m = i * k
        if m <= M:
            break
        elif str(m) == str(m)[::-1]:
            M = m
print(M)

# 8번
import random
tile = random.randrange(1, 5)
for i in range(1,5):
    for j in range(1,5):
        print(tile)
        if board[i][j] != 0:
            if j<3 and (board[i][j] == board[i][j+1] == board[i][j+2]):
                bul =1
                k = j
                while (k<5 and (board[i][j] == board[i][k])):
                    k+=1
            if i<3 and (board[i][j] == board[i+1][j] == board[i+2][j]):
                bul = 1
                k = i
                while (k<5 and (board[i][j] == board[k][j]) ):
                    k+=1


# 9번
a = [1, 3, 5, 7, 9]
b = list(map(lambda a: a**2, a))
print(b)