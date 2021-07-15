from typing import List
import queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        is_v = [[False] * len(maze[0]) for _ in range(len(maze))]
        for i in range(len(maze)) :
            for j in range(len(maze[0])) :
                if maze[i][j] == '+' : is_v[i][j] = True
        que = queue.Queue()
        que.put(tuple(entrance +[0]))
        is_v[entrance[0]][entrance[1]] = True

        lu = [[0,-1], [-1,0], [1,0],[0,1]]
        ans = 0
        flag = False
        while True:
            if que.empty() : break
            t = que.get()
            # print(t)
            if (t[0] ==0 or t[1] == 0 or t[0] == len(maze)-1 or t[1] == len(maze[0])-1) and  t[2]!=0:
                flag = True
                ans = t[2]
                break
            for i in range(4) :
                x ,y = t[0] + lu[i][0], t[1] + lu[i][1]
                if 0<=x < len(maze) and 0<= y < len(maze[0]) and is_v[x][y] ==False:
                    # print(x,y)
                    is_v[x][y] = True
                    que.put((x,y,t[2]+1))
        return ans if flag else -1
