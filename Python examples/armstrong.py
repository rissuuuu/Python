while 1:
    sums = 0
    num = int(input('Enter a number'))
    temp = num
    while temp > 0:
        a = int(temp % 10)
        sums = sums + (a*a*a)
        temp = int(temp / 10)
        print(a,sums,temp)
    if sums == num:
        print("Armstrong")
    else:
        print("Not Armstrong")
