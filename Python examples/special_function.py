class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Welcome ",name)

   # def __str__(self):
    #        return ("name is {} and age is {}".format(self.name,self.age))


def __del__(self):
    print("p1 deleted")
    print("p deleted")


p=person("risu",24)
print(p)

p1=person("Hari",100)
print(p1)
del(p)
del(p1)


