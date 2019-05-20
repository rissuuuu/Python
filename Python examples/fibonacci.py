type=int(input("Enter 1 for range and 2 for in between"))
if(type==1):
    ranges=int(input("Enter the range"))
    a=0
    b=1
    print(a,b,end=",")
    for i in range(1,ranges):
        c=a+b
        print(c,end=",")
        temp=a+b
        a=b
        b=temp
if(type==2):
    ranges = int(input("Enter the range"))
    a = 0
    b = 1
    print(a, b, end=",")
    for i in range(1, ranges):
        c = a + b
        if(c<=ranges):
            print(c, end=",")
            temp = a + b
            a = b
            b = temp
