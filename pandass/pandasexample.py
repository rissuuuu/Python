import pandas
total1=0
total2=0
total3=0
total4=0
l1=[1,2,4,6435,2341,2413]
l2=[21,3,35,64,23,655]
l3=[12,231,45435,56756,23,12]
l4=[54,7676,342,5675,23432,21]
for i in l1:
    total1=total1+i
for i in l2:
    total2=total2+i
for i in l3:
    total3=total3+i
for i in l4:
    total4=total4+i
l1.append(total1)
l2.append(total2)
l3.append(total3)
l4.append(total4)
dataframe=pandas.DataFrame([l1,l2,l3,l4],columns=["Sum","Diff","Div","Mod","Mul","Another","Total"],
                           index=["Sunday","Monday","Tuesday","Wednesday"])
print(dataframe)
print(dataframe.Total)
excelread=pandas.read_excel("C:\\Users\\Rishav\\Downloads\\airline.xlsx")
print(excelread)
