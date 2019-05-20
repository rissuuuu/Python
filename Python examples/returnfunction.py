a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))

def returnedfunction(a,b):
    return(a+b,b*a)

val1,val2=returnedfunction(a,b)
print(val1,val2)