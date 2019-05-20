class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def Name(self):
        return self.firstname+" "+self.lastname

class Employee(person):
    def __init__(self,first,last,staffnum):
        person.__init__(self,first,last)
        self.staffnum=staffnum
    def GetEmployee(self):
        return self.Name()+ ", "+str(self.staffnum)
x=person("Rishav","Paudel")
y=Employee("Risu","Nisu",1)

print(x.Name())
print(y.GetEmployee())