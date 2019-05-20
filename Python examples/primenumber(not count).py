while 1:
    n=int(input("Enter the range"))
    for i in range(2,n):
        for j in range(2,i):
            if(i%j==0):
                print(i,"is Not prime")
                break
        else:
              print(i,"is Prime")