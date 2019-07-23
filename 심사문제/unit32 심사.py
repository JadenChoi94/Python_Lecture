files = input().split()

print(list(map(lambda x: "{:0>3}.{}".format(x.split('.')[0], x.split('.')[1]), files)))
