#program to find the letter a and its occurance

name=input("Enter the word")
count=0
while(1):

    key=input("Enter the key to search")
    for i in range(len(name)):
        if(key==name[i]):
            count=count+1
    if (count < 1):
        print("Not Found")
    if(count>1):
        print(key,count)
        count=0
