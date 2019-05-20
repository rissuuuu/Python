
def lcm(x,y,small):
    print("small")
    while(1):
        if((small%x==0)and(small%y==0)):
            lcm=small
            break
        small+=1
    print("LCM is",lcm)

def smaller(x,y):
    if(x>y):
        small=y
    else:
        small=x
    lcm(x,y,small)


x=int(input("Enter A"))
y=int(input("Enter B"))
