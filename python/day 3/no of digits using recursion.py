#write a recursive function to count the number of digits of a number
def fun(num):
    if num==0:
        return 0
    return 1+fun(num//10)
print(fun(int(input("enter a number:"))))
