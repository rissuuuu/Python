import os
import pandas

a=os.listdir("C:\\Users\\Rishav\\Downloads\\pyth")
print(a)

df3=pandas.read_csv("C:\\Users\\Rishav\\Downloads\\pyth\\text.txt",sep="\t")
df3=df3.set_index("YEAR")
print(df3)

df3=df3.loc[:,"W"]
print(df3)
