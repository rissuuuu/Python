x=[[41,32,13],
   [54,57,67],
   [70,88,97]]
y=[[38,41,28],
   [51,26,99],
   [11,12,56]]
result=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)
print("------------------")
for i in range(len(x)):
    for j in range(len(x)):
        result[i][j]=x[i][j]-y[i][j]
for r in result:
    print(r)