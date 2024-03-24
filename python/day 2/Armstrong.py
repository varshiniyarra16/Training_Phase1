#armstrong number
n=int(input())
temp=n
temp1=n
count=0
sum=0
while n>0:
    a=n%10
    n=n//10
    count+=1
while temp>0:
    a=temp%10
    sum=sum+(a**count)
    temp//=10
print(sum)
if temp1==sum:
    print("armstrong")
else:
    print("not armstrong")
