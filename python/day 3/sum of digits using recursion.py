#write a recursive function to calculate the sum of digits of a number
def fun(num):
    if num==0:
        return 0
    return num%10+fun(num//10)
print(fun(int(input("enter a number:"))))

