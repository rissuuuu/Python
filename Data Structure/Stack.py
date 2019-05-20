class Stack:
    def __init__(self):
        self.stacks=[]
        print(self.stacks)

    def add(self,val):
        self.stacks.append(val)
        print(self.stacks)


    def see(self):
        if(len(self.stacks)!=0):
            peek=len(self.stacks)
            return self.stacks[peek-1]
        else:
            return("Empty stack")

    def delete(self):
        if(len(self.stacks)<=0):
            return("Empty stack")
        else:
            return(self.stacks.pop())
stack=Stack()
while(True):
    choice1=input(("Do you want to add element"))
    if(choice1=="y"):
        ele=input("Enter element")
        stack.add(ele)
    else:
        pass
    print(stack.see())
    choice=input("Do you want to delete element?")
    if(choice=="y"):
        stack.delete()
        print(stack.stacks)
        print(stack.see())

