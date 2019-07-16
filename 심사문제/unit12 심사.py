key_name = input().split()
value_result = list(map(float, input().split()))
result_dict = dict(zip(key_name, value_result))
print(result_dict)
