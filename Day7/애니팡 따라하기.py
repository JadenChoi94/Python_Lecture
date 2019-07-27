import random as rd
from pprint import pprint
#터뜨리고 채우는 함수(확장성 확보, 이후에 블럭이 터지는 다른조건을 추가할 수 있도록)
def peung(board):
    while(peung_chain(board)):
        print('==>')
        filled_board(board)


#3개 이상 연속되어 있는 블럭을 터뜨리는 함수

def peung_chain(board):
    peung_list = []

    flag = 0    #3개 이상 연속되는 블럭이 있었는지를 체크하는 플래그
    for i in range(1, 5):
        for j in range(1, 5):
            if board[i][j] != 0:
                #같은 열에 3개 이상 같은 블럭이 반복되는지.
                if j < 3 and (board[i][j] == board[i][j+1] == board[i][j+2]):
                    flag =1
                    k = j
                    while (k<5 and (board[i][j] == board[i][k])):
                        peung_list.append((i, k))
                        k += 1
                #같은 행에 3개 이상 같은 블럭이 반복되는지
                if i<3 and (board[i][j] == board[i+1][j] == board[i+2][j]):
                    flag = 1
                    k = i
                    while (k<5 and (board[i][j] == board[k][j]) ):
                        peung_list.append((k, j))
                        k += 1

    for item in peung_list:
        board[item[0]][item[1]] = 0

    if flag == 1:
        return True
    else:
        return False

#빈공간 채우기 함수
def filled_board(board):
    #두번째 행 부터 원소가 0이고 이전 행의 같은 열 원소가 0이 아닌 경우 내리기
    for i in range(1, 5):
        for j in range(1, 5):
            k = i
            while(k > 0):
                if board[k][j] == 0 and board[k-1][j] != 0:
                    board[k][j] = board[k-1][j]
                    board[k-1][j] = 0
                    k -= 1
                else:
                    break

#보드 출력 함수
def print_board(board):
    for i in range(5):
        print("{0} {1} {2} {3} {4}".format(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]))
    print("")

board = []
def main():
    for i in range(5):
        row = []
        for k in range(5):
            tmp = rd.randint(1, 4)
            row.append(tmp)
            print(tmp, end=' ')
        board.append(row)
        print()
    peung(board)
    print_board(board)
main()

