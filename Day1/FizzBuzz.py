for i in range(1, 101):
    if i % 3 == 0 and i % 5==0:
        print('FizzBuzz')
    elif i % 3==0:
        print('Fizz')
    elif i % 5==0:
        print('Buzz')
    else:
        print(i)

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리

# import turtle as t
# t.shape('turtle')
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.forward(100)