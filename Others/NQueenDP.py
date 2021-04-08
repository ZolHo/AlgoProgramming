class ChessTuple:
    chessboard = None      # 棋盘，长度为N+1的元组，前N个数的二进制代表此行有棋子的状态，N+1表示已放棋子个数，
    # 如(8,4,2,1,4)表示主对角线有棋子的棋盘
    equivalence_number = 1 # 等价类的个数
    def __init__(self, chessboard, equivalence_number):
        self.chessboard, self.equivalence_number = chessboard, equivalence_number

def NQueenByDP(N) :
    fuzhuarray = [2**(N-i-1) for i in range(N)]
    initchess = ChessTuple(tuple([0 for i in range(N+1)]),1)
    queue_dict = {initchess.chessboard:initchess}

    def adjoinChess(chessboard, x, y, N):
        newchessboard = list(chessboard)
        newchessboard[-1] += 1
        for i in range(N):
            if i == x:
                newchessboard[i] = 2 ** N - 1
            else:
                newchessboard[i] |= fuzhuarray[y]
                newchessboard[i] |= fuzhuarray[x+y-i] if 0<=x+y-i<N else 0
                newchessboard[i] |= fuzhuarray[i-x+y] if 0<=i-x+y<N else 0
        return tuple(newchessboard)

    for i in range(N):
        for j in range(N):
            for temp_chessboard in tuple(queue_dict.keys()):
                if 0 == temp_chessboard[i] & fuzhuarray[j]:
                    new_chessboard = adjoinChess(temp_chessboard, i, j, N)
                    if new_chessboard in queue_dict :
                        oldCT = queue_dict[new_chessboard]
                        oldCT.equivalence_number+=queue_dict[temp_chessboard].equivalence_number
                        queue_dict[new_chessboard] = oldCT
                    else:
                        newCT = ChessTuple(new_chessboard, queue_dict[temp_chessboard].equivalence_number)
                        queue_dict[new_chessboard] = newCT
    ans_key = [2**N-1 for i in range(N)]
    ans_key.append(N)
    ans_key = tuple(ans_key)

    return queue_dict[ans_key].equivalence_number if ans_key in queue_dict else 0


if __name__ == "__main__":
    print(NQueenByDP(8))