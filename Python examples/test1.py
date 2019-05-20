def sum(list):
    odd=0
    even=0
    for i in list:
        if(i%2==0):
            even=even+i
            print("even",i)
        else:
            odd=odd+i
            print("odd",i)
    return even,odd

a=[1,2,3,4,5,6,7,8,9,10]
e,o=sum(a)
print(e,o)

