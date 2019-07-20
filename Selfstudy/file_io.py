#open():파일을 특정한 모드로 여는 함수, 읽을 때는 r, 쓸때는 w를 사용함
#read(): 파일객체로부터 모든 내용을 읽는 함수
#readline(): 파일객체로부터 한 줄씩 문자열을 읽는 함수
#readlines(): 전체 내용을 한 번에 리스트에 담는 함수
'''
f = open("input.txt", "r", encoding="UTF-8")

f.seek(9) #한글자당 3byte, 3글자 건너뛰고 읽음
data = f.read()
print(data)
f.close()

# 한줄씩 읽기

count = 0
while count < 3:
    data=f.readline()
    count=count+1
    print("%d번째 줄: %s" %(count, data), end='')
f.close()

list = f.readlines()
#print(list) 줄바꿈 기호가 포함됨
for i, data in enumerate(list):
    print("%d번째 줄: %s" %(i+1, data), end='')
f.close




with open("input.txt", "r", encoding="UTF-8") as f:
    list=f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" %(i+1, data), end='')
'''

#빈도수 추출
def process(filename):
    with open(filename, "r") as f:
        #키: 알파켓, 값: 빈도수
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

dict = process("input.txt")
#빈도수를 기준으로 내름차운으로 정렬
dict= sorted(dict.items(), key=lambda a:a[1], reverse=True)
for data, count in dict:
    if data == '\n' or data == ' ':
        continue
    print("%d번 출현: [%c]" %(count, data))
