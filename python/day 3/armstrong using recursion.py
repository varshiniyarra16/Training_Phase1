#write the code of armstrong number using recursion
n=int(input())
def count(num):
    if num==0:
        return 0
    return 1+count(num//10)
count=count(n)
print(count)
def armstron(n,count):#189,3
    if n==0:
        return 0
    return (n%10)**count + armstron(n//10,count)
n1=armstron(n,count)
if n==n1:
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number")
