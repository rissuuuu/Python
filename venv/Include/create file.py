f1=open("D:/guru.txt","w+")
while(1):
    risu=input("Enter name to append")
    f1.write(risu)
    f1.close()

    f2=open("D:/guru.txt","r")
    print(f2.read())
    print(f2.readlines())
    f2.close()