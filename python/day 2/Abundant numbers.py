#take a number input from user check
#if the sum of factors of that number is greater than the original number or not
#if yes print yes or else no
n=12
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum=sum+i
print(sum)
if n<sum:
    print("yes")
else:
    print("no")
