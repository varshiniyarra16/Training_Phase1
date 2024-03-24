#take an integer as an input from the user and
#check whether if the number is divisible by sum of its digits or not
n=int(input())
temp=n
t=0
while n>0:
    n1=n%10
    t=t+n1
    n=n//10
print("sum :",t)
if temp%t==0:
    print("divisible")
else:
    print("not divisible")
    
