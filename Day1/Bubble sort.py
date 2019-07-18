sample_list = [5, 4, 21, 3, 15, 68, 11, 40, 34, 39]
sample_list = list(map(int, input('숫자를 입력하세요: ').split()))

for i in range(len(sample_list)-1):
    for k in range(i+1, len(sample_list)):
        if sample_list[i] > sample_list[k]:         #부등호 바뀌면 내림차순
            sample_list[i], sample_list[k] = sample_list[k], sample_list[i] #swap 변수 change
print(sample_list)


