password = "babushray3sh"
j=2
for i in range(3):
    name=input("Enter the password")
    if(name==password):
        print("Welcome to your facebook account")
        break

    else:
        print("The password is incorrect. Remaining tries:",j-i)
        continue
if(name!=password):
    print("BETTER LUCK NEXT TIME")
    



