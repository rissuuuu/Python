import pandas
data1=list(open("E:\\irisu.txt",'r'))
print(data1)
for word in data1:
    words=list(word)
    print(words)

data=pandas.read_csv("E:\\irisu.txt",sep="\t")
print(data)

wordd=list(input("Enter Word"))
count=0
for i,j,k, in zip(list(data["risu"]),list(data["risu.1"]),list(data["risu.2"])):
    print(i,end=",")
    print(j,end=",")
    print(k,end=",")
    if(i==j==k):
        print(" Match Found")
    else:
        print(" not Found")
    for ii,jj,kk in zip(list(i),list(j),list(k)):
        for iii in zip(wordd,ii):
            if(iii==ii):
                count+=1
print(count)

