def the_main(N):
    ans = 0 # 初始化返回结果
    jishuqi = 0
    # 初始化闭合线记录数组，分别为行、列、左斜线、右斜线
    hang, lie = [[False for i in range(N)] for j in range(2)]             # N行N列
    leftxie, rightxie = [[False for i in range(2*N-1)] for j in range(2)] # 斜线共2N-1条
    cishudict = {}
    # 定义回溯函数
    def huisu(x) :
        nonlocal ans,jishuqi # 声明全局变量
        temp = 0
        if x >= N:   # 递归界限
            ans += 1
            return
        for y in range(0, N):
            jishuqi +=1
            if not (hang[x] or lie[y] or leftxie[x+y] or rightxie[N+x-y-1]) :                       # 判断是否冲突
                hang[x], lie[y], leftxie[x + y], rightxie[N + x - y - 1] = [True for i in range(4)] # 设置记录数组
                huisu(x+1)     # 递归
                temp+=1
                hang[x], lie[y], leftxie[x + y], rightxie[N + x - y - 1] = [False for i in range(4)]# 还原记录数组
        if x in cishudict:
            cishudict[x]+=temp
        else:
            cishudict[x]= temp

    # 运行并返回结果
    huisu(0)

    # for i in range(N):
    #     if i == 0:
    #         print("第",i,"层节点数：",cishudict[i])
    #     else:
    #         print("第", i, "层节点数：", cishudict[i]/cishudict[i-1])
    # print("语句执行数:", jishuqi)

    return ans

if __name__ == '__main__':
    for i in range(1,15):
        print("N=",i,end=" 解为：", sep="")
        print(the_main(i))
    # the_main(9)

