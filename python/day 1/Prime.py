#prime number
n=13
flag=0
for i in range(2,n//2):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("its not a prime")
else:
    print("prime")
