#write a login function which accepts the user only
#when the username and password are same
#and displays a message login successful
#otherwise it keeps asking the user to enter the credentials until they are correct
def login():
    while True:
        a=str(input())
        b=str(input())
        if a==b:
            print("login successful")
            break
        else:
           print("enter the correct credentials")
login()
