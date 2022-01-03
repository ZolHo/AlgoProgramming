# 1，2，5，10
bag = [[0 for i in range(11)] for j in range(5)]
bag[1] = [1 for i in range(11)]
type = [0,1,2,5,10]

for i in range(2,5) :
    for j in range(1,11) :
        if j>=type[i]:
            bag[i][j] = bag[i-1][j] + bag[i-1][j-type[i]]
        else :
            for k in range(1,5):
                if j>type[k]:
                    bag[i][j] += bag[i-1][j]

for i in range(1,5) :
    print (bag[i])

