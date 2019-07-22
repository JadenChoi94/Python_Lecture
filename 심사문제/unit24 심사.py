words = input().split()
count_the = 0
for word in words:
    if word.strip(',.-') =='the':
        count_the += 1

print(count_the)
#
prices = list(map(int, input().split(';')))
prices.sort(reverse=True)
for price in prices:
    print('{:>9,d}'.format(price))