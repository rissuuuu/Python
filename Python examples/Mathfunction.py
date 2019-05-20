for i in range(1, 11):
    print("\n")
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
print("\n")
print(pow(5, 2))
print(2**3)

num = int(input("enter the number"))
powr = int(input("enter the power"))
result=1
for i in range(1, powr+1):
    result = result*num
print("the result is", result)