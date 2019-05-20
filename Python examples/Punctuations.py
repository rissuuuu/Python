punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!*&%$*&%@$#*!@&#(!&#, he said ---and went."
new=""
for i in my_str:
    if i not in punctuations:
        new=new+i
print(new,end="")
