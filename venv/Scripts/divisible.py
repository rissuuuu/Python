div=int(input("Enter the number"))
ranges=int(input("Enter the range"))
for i in range(1,ranges+1):
    divisible=i%div
    if(divisible==0):
        a=i//div
        print(div,"*",a,'=',div*a)
        print(i,"is divisible")
