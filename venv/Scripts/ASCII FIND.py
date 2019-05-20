Big=["A","B","C","D","E","F","G","H",'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in Big:
    print("Ascii of",i,"is",ord(i))
    for j in i:
        j=j.lower()
    print("Ascii of",j,"is",ord(j))
    print("-----------------------")
