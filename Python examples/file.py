file=open("E:\check.txt",'r')
strings=file.read()
str2=list(strings.split())
print(str2)
while 1:
    word=list(input("Enter Word to search"))
    print(word)
    count=0
    for i in str2:
        if(i==word):
            count+=1
    print(count)
    print("-----------------------")
    words=""
    counted=0
    for i in str2:
        print("-----------------------")
        print(i)

        for k in list(i):
            print(k)

            for j in word:
               if (j == k):
                 words = words + j
                 if (words == word):
                    print("found")
                 else:
                    print("not found")


