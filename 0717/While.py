import random    # random 모듈을 가져옴
random.randint(1, 6)
i = 0
while i != 3:    # 3이 아닐 때 계속 반복
    i = random.randint(1, 6)    # randint를 사용하여 1과 6 사이의 난수를 생성
    print(i)
# while True:    # while에 True를 지정하면 무한 루프
#     print('Hello, world!')
# Ctrl+C를 입력하여 무한 루프를 끝냅니다.
# while 1:    # 0이 아닌 숫자는 True로 취급하여 무한 루프로 동작
#     print('Hello, world!')
# while 'Hello':    # 내용이 있는 문자열은 True로 취급하여 무한 루프로 동작
#     print('Hello, world!')

i = 0
while True:    # 무한 루프
    print(i)
    i += 1          # i를 1씩 증가시킴
    if i == 100:    # i가 100일 때
        break       # 반복문을 끝냄. while의 제어흐름을 벗어남

for i in range(100):       # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:         # i를 2로 나누었을 때 나머지가 0면 짝수
        continue           # 아래 코드를 실행하지 않고 건너뜀
    print(i)

i = 0
while i < 100:        # i가 100보다 작을 때 반복. 0부터 99까지 증가하면서 100번 반복
    i += 1            # i를 1씩 증가시킴
    if i % 2 == 0:    # i를 2로 나누었을 때 나머지가 0이면 짝수
        continue      # 아래 코드를 실행하지 않고 건너뜀
    print(i)

for i in range(100):
    if i % 2==0:
        continue
    print(i, end='')

# for, while의 반복할 코드에서 아무 일도 하지 않지만, 반복문의 형태를 유지하고 싶다면 pass를 사용하면 됩니다.
# for i in range(10):    # 10번 반복
#     pass               # 아무 일도 하지 않음

# while True:    # 무한 루프
#     pass       # 아무 일도 하지 않음

count = int(input('반복할 횟수를 입력하세요: '))
i = 0
while True:  # 무한 루프
    print(i)
    i += 1
    if i == count:  # i가 입력받은 값과 같을 때
        break  # 반복문을 끝냄

for i in range(1, 6):
    for k in range(i):
        print('*', end='')
    print()

for i in range(5):            # 5번 반복. 바깥쪽 루프는 세로 방향
    for k in range(5):        # 5번 반복. 안쪽 루프는 가로 방향
        print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)

for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for k in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if k <= i:                # 세로 방향 변수 i만큼
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)

for i in reversed(range(5)):
    for k in range(i):
        print(' ', end='')
    print('*')
