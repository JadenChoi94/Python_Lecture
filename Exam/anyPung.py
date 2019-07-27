# 다음의 규칙대로 동작하는 프로그램을 작성하시오.
#    1) 타일판은 5 x 5
#    2) 타일 종류는 1 ~ 4의 네가지로 랜덤값으로 정한 후 타일판 출력
#    3) 가로나 세로로 3개 이상 같은 타일이 연속될 경우
#       타일을 '*'로 바꾸고 타일판 출력
#    4) '*' 타일은 위에서부터 내려오고 빈 칸은 랜덤값으로 채움
#    5) 3), 4) 과정을 '*'이 나오지 않을 때 까지 반복
import random as rd
NO_OF_ROW = 5
NO_OF_COLUMN = 5

def printMatrix(mat):
    for i in range(len(mat)):
        for k in range(len(mat[i])):
            print(mat[i][k], end=' ')
        print()

def findPung(line):  # 한 라인을 매개변수로 받아, 결과, 시작, 끝 인덱스 반환
    start = 0
    stop = 0
    pung = False
    for i in range(NO_OF_COLUMN - 2):
        if line[i] != line[i+1] or line[i+1] != line[i+2]:
            continue
        pung = True
        start = i
        stop = i+2
        if i == NO_OF_COLUMN - 3:
            break
        if line[i+2] != line[i+3]:
            break
        stop = i+3
        if i == NO_OF_COLUMN - 4:
            break
        if line[i+3] == line[i+4]:
            stop = i+4
        break
    return pung, start, stop

def copyLine(pung, start, stop, line):
    newLine = line.copy()
    if pung:
        for i in range(start, stop+1):
            newLine[i] = '*'
    return newLine

def collapse():
    for i in range(NO_OF_ROW):
        for k in range(NO_OF_COLUMN):
            if tile[i][k] == '*':
                if i == 0:
                    tile[i][k] = str(rd.randint(1, 4))
                elif i == 1:
                    tile[i][k] = tile[i-1][k]
                    tile[i-1][k] = str(rd.randint(1, 4))
                elif i == 2:
                    tile[i][k] = tile[i - 1][k]
                    tile[i - 1][k] = tile[i - 2][k]
                    tile[i - 2][k] = str(rd.randint(1, 4))
                elif i == 3:
                    tile[i][k] = tile[i - 1][k]
                    tile[i - 1][k] = tile[i - 2][k]
                    tile[i - 2][k] = tile[i - 3][k]
                    tile[i - 3][k] = str(rd.randint(1, 4))
                else:
                    tile[i][k] = tile[i - 1][k]
                    tile[i - 1][k] = tile[i - 2][k]
                    tile[i - 2][k] = tile[i - 3][k]
                    tile[i - 3][k] = tile[i - 4][k]
                    tile[i - 4][k] = str(rd.randint(1, 4))

# Program starts here!!!
tile = [[str(rd.randint(1, 4)) for k in range(NO_OF_COLUMN)] for i in range(NO_OF_ROW)]
print('  Given')
printMatrix(tile)

counter = 0
while True:
    counter += 1
    rowResult = []
    wholePung = False
    for i in range(NO_OF_ROW):
        pung, start, stop = findPung(tile[i])
        if pung:
            wholePung = True
        rowResult.append(copyLine(pung, start, stop, tile[i]))

    colResult = []
    tpTile = [list(x) for x in zip(*tile)]
    for i in range(NO_OF_ROW):
        pung, start, stop = findPung(tpTile[i])
        if pung:
            wholePung = True
        colResult.append(copyLine(pung, start, stop, tpTile[i]))
    tpColResult = [list(x) for x in zip(*colResult)]

    if not wholePung:
        break;

    print('   ==>')
    # Merge the result
    for i in range(NO_OF_ROW):
        for k in range(NO_OF_COLUMN):
            if rowResult[i][k] == '*' or tpColResult[i][k] == '*':
                tile[i][k] = '*'
    printMatrix(tile)

    collapse()
    print(" Combo", counter)
    printMatrix(tile)

print('게임이 끝났습니다.')