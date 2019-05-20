list1=["Rishav",'Paudel',1,2,3,4,5,6]
print(list1.index(1))
for i in list1:
    print(i)
list1.append("Neesu")
print(list1)

tup1=(1,2,3,4,5)
print(tup1)

def returned():
    return(10,15)

x,y=returned()
print(x,y)

print(tup1.count(1))