ranges=int(input("Enter range"))
for i in range(1,ranges+1):
    order = len(str(i))
    temp=i
    sum=0
    while temp>0:
        a=(temp%10)
        sum=sum+(a**order)
        temp=(temp//10)
    if(i==sum):
        print("Armstrong:",i)


