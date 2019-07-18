import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):   
    t.fd(line)
    t.rt(720 / n)
    t.fd(line)
    t.lt(360/n)