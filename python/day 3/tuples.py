#tuples
#creation of tuples
#adding values manually to a tuple
#tuple data accessing
print("creating a tuple")
a=(12,123.4,True)
print(a)
print("adding values to tuple manually")
b=("a","b","c")
print(a+b)
print("tuple data accessing")
print(a[-1])
print(a[0])
print(a[2])
print("adding values to tuple from user")
for i in range(3):
    n=int(input("enter"))
    a = a + (n,)
print(a)
