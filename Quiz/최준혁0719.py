# 1
M = 0
for i in range(999, 99, -1):
    for k in range(999, i-1, -1):
        m = i * k
        if m <= M:
            break
        elif str(m) == str(m)[::-1]:
            M = m
print(M) # 906609

# 2
# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수!!
# chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
word = input("단어를 입력하세요 : ")
num_input = int(input("번호를 입력하세요 : "))
str_out = ''
for ch in word:
    if ch.islower():
       num = (ord(ch) + num_input - ord('a')) % 26 + ord('a')
    elif ch.isupper():
        num = (ord(ch) + num_input - ord('A')) % 26 + ord('A')
    else:
        num = ord(ch)
    str_out = str_out+chr(num)
print(str_out)

# 3
word, filename = input('찾고자 하는 문자열과 파일명을 입력하세요: ').split()
# range d:/Workspace/Python_Lecture/Day3/unit27_fileIO.py
lineNo = 1
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        if line.find(word) >= 0:
            print('%2d:' % lineNo, line, end='')
        lineNo += 1
# 4

# 5

# 6



