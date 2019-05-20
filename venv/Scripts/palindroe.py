num=int(input("Enter n"))
reverse=0
while(num>0):
    rem=(num%10)
    reverse=(reverse*10)+rem
    num=num//10
print(reverse)

str=list(input("Enter String"))
str2=list(reversed(str))
if(str==str2):
    print("Palindrome")
else:
    print("Not palindrome")
