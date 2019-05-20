class person:
    def __init__(self,name,age):
        self.name=name
        self.classe=age
        print("name is {} and class is {}".format(name,age))


class Rishav(person):
    def print(self,name,age):
        person.__init__(self,name,age)


class Neesu(person):
    def disp(selfn,name,age):
        person.__init__(selfn,name,age)

c1=Rishav("Risu",24)
c2=Neesu("Neesu",19)