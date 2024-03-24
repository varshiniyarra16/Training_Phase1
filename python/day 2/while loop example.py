#print the numbers
#print the count of numbers
#Sum of the numbers
#multiplication of the numbers
num=12345
count=0
t=0
m=1
while num>0:
    n=num%10
    print(n)
    t=t+n
    m=m*n
    num=num//10
    count=count+1
print("count is :",count)
print("sum is :",t)
print("multiplication of the digits is :",m)
