n=int(input())
temp=n
rev=0
while n>0:
    n1=n%10
    rev=rev*10+n1
    n=n//10
print(rev)
if rev==temp:
    print("palindrome")
else:
    print("not palindrome")
