# 재귀호출(recursive call)사용하기
def hello():
    print('Hello, world!')
    hello()
hello()

# 재귀호출에 종료 조건 만들기
def hello(count):
    if count == 0:  # 종료 조건을 만듦. count가 0이면다시 hello 함수를 호출하지않고끝냄
        return
    print('Hello, world!', count)
    count -= 1  # count를 1 감소시킨 뒤
    hello(count)  # 다시 hello에 넣음
hello(5)  # hello 함수 호출

# 재귀호출로 팩토리얼 구하기
def factorial(n):
    if n == 1:  # n이 1일 때
        return 1  # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)  # n과 factorial 함수에 n - 1을 넣어서 반환된 값을곱함
print(factorial(5))

def ari_seq(n, d):
    if n == 1:
        return 1
    return ari_seq(n-1, d)+d
ari_seq(5, 3)

# fibonacci(n)=fibonacci(n-1)+fibonacci(n-2)
# f(1)=1, f(0)=0