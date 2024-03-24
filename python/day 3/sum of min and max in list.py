#add the minimum value and max value
#replace the sum with max value
#replace the subtracted value with min value
a=[12,42,23,96,7,18,10,133]
min=a[0]
max=a[0]
minid=0
maxid=0
for i in range(len(a)):
    if min>a[i]:
        min=a[i]
        minid=i
    if max<a[i]:
        max=a[i]
        maxid=i
print(min,minid)
print(max,maxid)
sum=min+max
sub=max-min
print(sum)
print(sub)
a[minid]=sub
a[maxid]=sum
print(a)
