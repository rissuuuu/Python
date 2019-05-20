def Count(i,c):
    print("Occurance of",i,"is",c)



def Vowel(words):
    counted=0
    letters = list(words)
    for i in letters:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            counted=letters.count(i)
            Count(i,counted)

words=input("Enter the words or letters")
Vowel(words)
