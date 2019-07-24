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

# 2 =====================================================================================================
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

# 3 =====================================================================================================
word, filename = input('찾고자 하는 문자열과 파일명을 입력하세요: ').split()
# range d:/Workspace/Python_Lecture/Day3/unit27_fileIO.py
lineNo = 1
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        if line.find(word) >= 0:
            print('%2d:' % lineNo, line, end='')
        lineNo += 1

# 4 =====================================================================================================
filename = input('파일이름:')
wordsDict = dict()
with open(filename, 'r') as file:
    for line in file :
    linewords = line.replace('(', ' ').replace(')', ' ').replace('.', ' ')\
        .replace(',',' ').split()
    for word in linewords:
        count = wordsDict.get(word, 0)
        if count == 0:
            wordsDict.setdefault(word, 1)
        else:
            wordsDict.update(dict([(word, count+1)]))
import operator
wordsList = sorted(wordsDict.items(), key = operator.itemgetter(1), reverse=True)
# operator.itemgetter(1) 정렬의 키값을 1번째 인덱스 기준으로 하겠다는 것이다.
# 내림차순으로 정렬이 가능하다.
for i in range(10):
    print(wordsList[i])

# 5 =====================================================================================================
import os
import shutil #shutil은 파일을 복사해 주는 파이썬 모듈.
import random as rd
'''
PATH = 'C:/Windows/Temp/Ex04'
os.mkdir(PATH)
os.chdir(PATH)
for dirname in ('low', 'mid', 'high'):
    os.mkdir(PATH + '/' + dirname)
    for num in ('1', '2', '3'):
        os.mkdir(PATH + '/' + dirname + '/' + num)
for i in range(100):
    filenumber = rd.randint(0, 9999)
    content = str(rd.randint(1, 3))
    filename = '%04d.txt' % filenumber #txt 이름
    file = open(filename, 'w')
    file.write(content) #txt 내용
    file.close() # 저장
fileList = os.listdir(PATH)

for filename in fileList:
    # 디렉토리면 처리하지 않고 Loop을 반복
    if os.path.isdir(filename):
        continue
    # 일반 파일이면
    # 파일이름에서 숫자를 구하고, 파일을 읽어서 콘텐츠를 가져온다.
    filenumber = int(filename[0:4]) # 슬라이싱,'1234.txt'로 부터 1234를 구함
    file = open(filename, 'r')
    content = file.read(1)
    file.close()
    # 원하는 위치에 파일을 이동, shutil
    if filenumber <= 3333:
        dirname = 'low'
    elif filenumber <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'
    dst = dirname + '/' + content + '/' + filename
    shutil.move(filename, dst)
'''

os.chdir("C:/Windows/Temp/Ex04")
count = 0
if os.path.isdir('low') == True:
    shutil.rmtree('low')
if os.path.isdir('mid') == True:
    shutil.rmtree('mid')
if os.path.isdir('high') == True:
    shutil.rmtree('high')

os.mkdir('low')
os.mkdir('mid')
os.mkdir('high')
for i in range(1,4):
    os.mkdir('low' + '/' + str(i))
    os.mkdir('mid' + '/'  + str(i))
    os.mkdir('high' + '/' + str(i))

while count < 100:
    filename = ''
    for i in range(0,4):
        filename = filename+str(rd.randint(0,9))
    text = str(rd.randint(1,3))
    if (int(filename) < 3334):
        with open('low\\' + text + '\\' + filename + '.txt', 'w') as w:
            w.write(text)
    elif (int(filename) > 3333 and int(filename) < 6667):
        with open('mid\\' + text + '\\' + filename + '.txt', 'w') as w:
            w.write(text)
    else:
        with open('high\\' + text + '\\' + filename + '.txt', 'w') as w:
            w.write(text)
    count += 1


# 6 =====================================================================================================
import os
def showHexa(addr, buf, size):
    if addr % 1024 == 0 and addr != 0:
        print()
    print('%08X: ' % addr, end = ' ')

    if size != 16:
        for i in range(size):
            if i == 8:
                print(end=' ')
            print('%02X' % buf[i], end=' ')
        for i in range(size, 16):
            if i == 8:
                print(end=' ')
            print('  ', end=' ')

    else:
        for i in range(size):
            if i == 8:
                print(end=' ')
            print('%02X' % buf[i], end=' ')
    print('  ', end='')

    for i in range(size):
        if i == 8:
            print(end=' ')
        if buf[i] < 0x20 or buf[i] > 0x7e:
            print('.', end='')
        else:
            print(chr(buf[i]), end='')
    print()

filename = input('파일 이름을 입력하세요: ')# C:/Windows/Temp/james.p
fileLength = os.path.getsize(filename)
with open(filename, 'rb') as file:
    count = 0
    for i in range(0, fileLength, 16):
        buf = file.read(16)
        if fileLength - i < 16:
            size = fileLength - i
        else:
            size = 16
        showHexa(i, buf, size)










