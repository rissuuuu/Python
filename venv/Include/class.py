class student:
    def Add(self,name):
        self.name=name
        #self.clas=clas
        print("The name is {} and class ".format(name))


s1=student()
while(1):
    name=input("Enter the names")
    names=s1.Add(name)
    l1=[]

    i=5
    l1.append(name)
    print(l1)
    if(name=="exit"):
        exit()
