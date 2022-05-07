def lowercase_check(password):
    if re.search('[a-z]', password): #atleast one lowercase character
        return True
    return False

def digit_check(password):
    if re.search('[0-9]', password): #atleast one digit
        return True
    return False

def user_input_password_check():
    password = input("Enter password : ")
        #atleast 8 character long
    if len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password):
        print("Strong Password")
    else:
        print("Weak Password")

user_input_password_check()

import re
v=input("Enter the password:")
if(len(v)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
        print("The password is strong")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print("The password is weak")
else:
    print("You have entered an invalid password.")

