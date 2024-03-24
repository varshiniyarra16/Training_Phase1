#write a function which takes two arguments a and b
#typecast their value of second argument into integer
#then multiply both the arguments and print the last digit of the result
def example(a,b):
    b=int(b)
    c=a*b
    print("multiplication of the integers are:",c)
    c=c%10
    print("last digit of the result is:",c)
example(12,3.45)
