Y = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
X = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(Y[0])):
    for j in range(len(Y[0])):
        for k in range(len(X)):
            result[i][j]=result[i][j]+X[i][k]*Y[k][j]

for i in result:
    print(i)
