n=int(input())
n1=n
count=0
sum=0
while n>0:
    n=n//10
    count+=1
while n1>0:
    a=n1%10
    sum=sum+(a**count)
    n1//=10
    count-=1
print(sum)
