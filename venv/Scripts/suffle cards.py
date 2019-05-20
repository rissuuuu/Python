import random
while 1:
    input()
    a=['Spade','Heart','Diamond','Club']
    b=[1,2,3,4,5,6,7,8,9,10,'J','Q','K']
    random.shuffle(b)
    random.shuffle(a)
    for i in range(1):
        print("You got",b[i],"of",a[i])
