"""
小兔的棋盘
https://blog.csdn.net/wyxeainn/article/details/61926253
难点：
- 数组模拟棋盘
- 到当前点f(x,y)的路径数 = f(x-1,y) + f(x, y-1)
"""

def solution(size):

    board = [[0 for x in range(size + 1)] for y in range(size + 1)]

    for y in range(0, size + 1):
        for x in range(size + 1):
            if y > x:
                continue
            if y == 0:
                board[y][x] = 1
            else:
                board[y][x] = board[y - 1][x] + board[y][x - 1]
    return 2 * board[size][size]

if __name__ == '__main__':
    print(solution(5))