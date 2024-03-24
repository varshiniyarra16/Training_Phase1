#write a recursive program to print the digits of a number in the reverse order
def rev(num):
    if num==0:
        return
    print(num%10)
    return rev(num//10)
rev(123)

