def fibno(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibno(n-1)+fibno(n-2)
n=int(input())
print(fibno(n))
