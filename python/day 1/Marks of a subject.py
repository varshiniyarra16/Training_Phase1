#write a program to accept the subject marks from the user
#and check if the marks are greater than 35 print cheated
#if marks are equal to 35 pass
#if marks less than 35 fail
marks=int(input("enter the subject marks:"))
if marks>35:
    print("cheated")
elif marks==35:
    print("pass")
else:
    print("fail")
