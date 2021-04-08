from functools import reduce
def NQueenByDP(N) :
    fuzhuarray = [2**(N-i-1) for i in range(N)]     # 选择二进制的第i位的辅助函数
    queue_dict = {tuple([0 for i in range(N+1)]):1} # 字典，key为棋盘状态的N+1元组，value为该状态等价类的个数，初始化
    # 将坐标为x,y的棋子放入某个状态的棋盘，返回新的棋盘状态N+1元组
    def adjoinChess(newchessboard, x, y):
        newchessboard[-1] += 1 # 元组的最后一位代表当前棋子数，使其加一
        for i in range(N):
            newchessboard[i] |= fuzhuarray[y]                          # 使棋子列所在的二进制位变为1
            newchessboard[i] |= fuzhuarray[x+y-i] if 0<=x+y-i<N else 0 # 使棋子左斜线所在的二进制位变为1
            newchessboard[i] |= fuzhuarray[i-x+y] if 0<=i-x+y<N else 0 # 使棋子右斜线所在的二进制位变为1
        newchessboard[x] = 2 ** N - 1                                  # 使棋子行所在的二进制位变为1
        boardand = reduce(lambda x,y:x&y,[newchessboard[i] for i in range(N)])
        return tuple(newchessboard), sum([(boardand>>i & 1)for i in range(N)]) > newchessboard[-1]

    temp = 0
    for i in range(N):
        for j in range(N):
            for temp_chessboard in tuple(queue_dict.keys()): # 将每一个棋子与字典中的所有状态比较
                temp +=1
                if 0 == temp_chessboard[i] & fuzhuarray[j]:  # 判断第该状态的第i,j位置是否二进制为0
                    new_chessboard, flag = adjoinChess(list(temp_chessboard), i, j)
                    if flag:
                        continue
                    if new_chessboard in queue_dict :        # 若该状态存在，合并等价类
                        queue_dict[new_chessboard]+=queue_dict[temp_chessboard]
                    else:                                    # 若不存在则添加进字典，并保存等价类个数
                        queue_dict[new_chessboard] = queue_dict[temp_chessboard]
    ans_key = tuple([2**N-1 for i in range(N)] + [N])        # 解的棋盘状态是一定的，看字典是否存在，其等价类个数即为解的个数
    print(N,"状态数：",len(queue_dict), "循环数：",temp)
    # for i in queue_dict:
    #     if queue_dict[i] >=2:
    #         print(i, queue_dict[i])
    return queue_dict[ans_key] if ans_key in queue_dict else 0

if __name__ == "__main__":
    # print(NQueenByDP(7))
    for i in range(11):
        NQueenByDP(i)