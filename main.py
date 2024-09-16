#identity data
print("what is your name?")
name=input()

print("what is your surname?")
surname=input()

print("which is the ID?")
id=input()

print("when is your birthday")
birthday=input()

print("what is your father's name?")
fatherName=input()

print("what is your Father's last name?")
fatherLastName=input()

print("what is your mother's name?")
motherName=input()

print("what is your mother's last name?")
motherLastName=input()

user="You are "+ name +" "+ surname + " with ID "+ id +" your father is " + fatherName +" "+ fatherLastName +" your mother is "+ motherName +" "+ motherLastName

print(user)
print("do you want to save your user?yes or no")
answer=input()
if answer=="yes":
    with open("C:/Users/info/OneDrive/Desktop/project/firstPythonApp/users.txt","a",encoding="utf-8") as file:
        file.write(user)
    print("success")
else:
    print("user not saved")

