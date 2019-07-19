import os
os.chdir("c:\windows\Temp") # 디렉토리 바꾸기
os.getcwd() #현재 디렉토리 확인

# 파일에 문자열 쓰기, 읽기
file = open('hello.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!')      # 파일에 문자열 저장/read/update
file.close()                     # 파일 객체 닫기

file = open('hello.txt', 'r')    # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()                     # 파일 객체 닫기

# 자동으로 파일 객체 닫기
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)                            # Hello, world!

# 반복문으로 문자열 여러 줄을 파일에 쓰기
with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

#  리스트에 들어있는 문자열을 파일에 쓰기
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
with open('hello.txt', 'w') as file:  # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)

# 파일의 내용을 한 줄씩 리스트로 가져오기
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)

# 횟수가 몇번인지 모를때는 While 문 사용, 특히 파일의 내용 불러올때
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

# for 반복문으로 파일의 내용을 줄 단위로 읽기
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

# 파일 객체는 이터레이터입니다. 따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능합니다
# (이터레이터는 'Unit 39 이터레이터 사용하기' 참조).
file = open('hello.txt', 'r')
a, b, c = file
a, b, c

# 파이썬 객체를 파일에 저장하기
import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:  # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

# 파일에서 파이썬 객체 읽기
import pickle

with open('james.p', 'rb') as file:  # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)

# 파일, 디렉터리 조작



