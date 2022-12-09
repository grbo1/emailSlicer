#define functions
def emailValidate(email):
    if atSymbolValidate(email) != True:
        return atSymbolValidate(email)
    elif periodSymbolValidate(email) != True:
        return periodSymbolValidate(email)
    else:
        return True

def atSymbolValidate(email):
    if email.count("@") == 1:
        return True
    else:
        return "1 @ symbol required"
    
def periodSymbolValidate(email):
    if email.count(".") >= 1:
        return True
    else:
        return "At least 1 period symbol required"

#main
prompt = "Enter email address"
print(prompt)
email = input()
if emailValidate(email) != True:
    print(emailValidate(email))
else:
    [username,domain] = email.split("@")
    print("Your username is " + username + " and your domain is " + domain)