col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for k in range(col):
        print(matrix[i][k], end ='')
    print()
for i in range(row):
    for k in range(col):
        if matrix[i][k] == '*':
            continue
        matrix[i][k] = 0
        for y in range(i-1, i+2):
            for x in range(k-1, k+2):
                if y < 0 or x <0 or y >= row or x >= col:
                    continue
                if matrix[y][x] == '*':
                    matrix[i][k] += 1
for i in range(row):
    for k in range(col):
        print(matrix[i][k], end ='')
    print()