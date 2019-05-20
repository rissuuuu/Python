a=[[1,2,3],
   [4,5,6]]
result=[[0,0],
        [0,0],
        [0,0]]
for i in range(len(a)):
    for j in range(len(result[0])):
        result[i][j]=a[j][i]

for r in result:
    print(r)