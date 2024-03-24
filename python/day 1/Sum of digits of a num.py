#calculate the sum of digits of a number which is taken input from the user
n=int(input())
sum=0
while n!=0:
    add=n%10
    sum=sum+add
    n=n//10
print(sum)


