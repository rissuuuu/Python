import time

lin=time.time()
mes=time.time()
lout=time.time()
lin1=time.localtime(lin)
mes1=time.localtime(mes)
lout1=time.localtime(lout)
login=time.asctime(lin1)
message=time.asctime(lin1)
logout=time.asctime(lin1)
while(1):
    type=input("Enter Credentials")
    if(type=="login"):
        print(lin)
        print(lin1)
        print(login)
    elif(type=="message"):
        print(mes)
        print(mes1)
        print(message)
    elif(type=="logout"):
        print(lout)
        print(lout1)
        print(logout)
        exit()
    else:
        print("Thank you")

