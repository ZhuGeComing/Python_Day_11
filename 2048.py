import random

matrix = [[0 for i in range(4)] for ii in range(4)]

def notzero(x):
    return x if x != 0 else ''

def welcome():
    print("""
    ┌────┬────┬────┬────┐
    │%4s│%4s│%4s│%4s│
    ├────┬────┬────┬────┤
    │%4s│%4s│%4s│%4s│
    ├────┬────┬────┬────┤
    │%4s│%4s│%4s│%4s│
    ├────┬────┬────┬────┤
    │%4s│%4s│%4s│%4s│
    └────┴────┴────┴────┘
    A,S,D,W 分别控制向左、向下、向右、向上，R重新，Q退出
    """ % (notzero(matrix[0][0]), notzero(matrix[0][1]), notzero(matrix[0][2]), notzero(matrix[0][3]), \
           notzero(matrix[1][0]), notzero(matrix[1][1]), notzero(matrix[1][2]), notzero(matrix[1][3]), \
           notzero(matrix[2][0]), notzero(matrix[2][1]), notzero(matrix[2][2]), notzero(matrix[2][3]), \
           notzero(matrix[3][0]), notzero(matrix[3][1]), notzero(matrix[3][2]), notzero(matrix[3][3]),))

def start():
    num = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                num += 1
    if num == 0:
        return False
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if matrix[x][y] == 0:
            matrix[x][y] = 2 if random.random() < 0.5 else 4
            break

def check():
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == 0 or matrix[i][j] == matrix[i][j+1] or matrix[j+1][i] == matrix[j][i]:
                return True
    return False

def moveLeft():
    for i in range(4):
        for j in range(3):
            for k in range(j+1, 4):
                if matrix[i][k] > 0:
                    if matrix[i][j] == 0:
                        matrix[i][j] = matrix[i][k]
                        matrix[i][k] = 0
                    elif matrix[i][j] == matrix[i][k]:
                        matrix[i][j] = matrix[i][j] * 2
                        matrix[i][k] = 0

def moveDown():
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j-1, -1, -1):
                if matrix[k][i] > 0:
                    if matrix[j][i] == 0:
                        matrix[j][i] = matrix[k][i]
                        matrix[k][i] = 0
                    elif matrix[j][i] == matrix[k][i]:
                        matrix[j][i] = matrix[j][i] * 2
                        matrix[k][i] = 0

def moveRight():
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j-1, -1, -1):
                if matrix[i][k] > 0:
                    if matrix[i][j] == 0:
                        matrix[i][j] = matrix[i][k]
                        matrix[i][k] = 0
                    elif matrix[i][j] == matrix[i][k]:
                        matrix[i][j] = matrix[i][j] * 2
                        matrix[i][k] = 0

def moveUp():
    for i in range(4):
        for j in range(3):
            for k in range(j+1, 4):
                if matrix[k][i] > 0:
                    if matrix[j][i] == 0:
                        matrix[j][i] = matrix[k][i]
                        matrix[k][i] = 0
                    elif matrix[j][i] == matrix[k][i]:
                        matrix[j][i] = matrix[j][i] * 2
                        matrix[k][i] = 0


if __name__ == '__main__':
    start()
    start()
    welcome()
    while True:
        key = input()
        if key == 'w':
            moveUp()
        elif key == 's':
            moveDown()
        elif key == 'a':
            moveLeft()
        elif key == 'd':
            moveRight()
        elif key == 'q':
            break
        elif key == 'r':
            print('重新开始~')
            matrix = [[0 for i in range(4)] for ii in range(4)]
        else:
            pass
        start()
        start()
        welcome()
        print(check())
