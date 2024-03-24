#write a program to find the second smallest negative number from the list
a=[22,42,65,1,-4,6,-1]
print(a)
min1=999
min2=999
#type 1
for i in range(len(a)):
    if min1>a[i]:
        min1=a[i]
for i in range(len(a)):
    if min2>a[i] and min!=min1:
        min2=a[i]
print("second minimum element is",min2)
#type2
##for i in range(len(a)):
##    if min1>a[i]:
##        min2=min1
##        min1=a[i]
##    elif min2>a[i] and min2>min1:
##        min2 = a[i]
##print(min2)
