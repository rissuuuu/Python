class student:
    def __init__(self,name):
        self.name=name
        self.names=[]
    def namesadd(self,add):
        self.names.append(add)
        print(self.names)
s1=student("risu")
while(1):
    enteragain=input("Enter names")
    s1.namesadd(enteragain)
    if(enteragain=="exit"):
        exit()
for i in s1.names:
    if(s1.names[i]=="a"):
        print("a is found")
    print(s1.names)