a, b = map(int, input().split())

x = [2 ** i for i in range(a, b+1)]
del x[1]
del x[-2]
print(x)