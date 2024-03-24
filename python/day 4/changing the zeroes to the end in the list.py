#shit the zeroes to the end
list1=[2,0,1024,0,40,230,0]
j=0
for i in range(len(list1)):
    print(i,list1)
    if list1[i]!=0:
        list1[i],list1[j]=list1[j],list1[i]
        j+=1
print(list1)
#another one
l2=[]
for i in list1:
    if i!=0:
        l2.append(i)
for i in list1:
    if i==0:
        l2.append(i)

print(l2)
