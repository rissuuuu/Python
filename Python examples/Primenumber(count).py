while 1:
    count=0
    n=int(input("Enter the range"))
    i=1
    if(n==1):
        print("Enter value greter than 1")
    if(n==2):
        print("Prime")

    for i in range(2,n+1):
        counter = 0
        print("i is",i)
        print("Count is",counter)

        for j in range(1,i+1):
            print("j is ",j)
            print("Count is",counter)
            if(i%j==0):
                counter+=1
                print(i,"%",j,"=",i%j)
                print("Counter is",counter)
            if(i%j!=0):
                print(i,"is not divisible by",j)
        if(counter==2):
            print(i,"is  prime number")
        else:
            print(i,"is not prime number")