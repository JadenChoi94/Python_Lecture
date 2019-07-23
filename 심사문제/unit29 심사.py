x, y = map(int, input().split())

def calc(x, y):
    a = x + y
    s = x - y
    m = x * y
    d = x / y
    return a, s, m, d

a, s, m, d = calc(x, y)
print('덧셈: {}, 뺄셈: {}, 곱셈: {}, 나눗셈: {}'.format(a, s, m, d))