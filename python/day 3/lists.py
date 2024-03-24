#lists
#creation
print("creation of list")
list=[12,2+3j,"Lahari",1.234]
print(list)
#access
print("Accessing the list")
print(list[-1])
print(list[0])
print(list[2])
#slicing
print("slicing of the list")
print(list[1:2])
print(list[-3:-1])
print(list[:2])
print(list[-2:])
#loops accessing
print("accessing the lists using loops")
for i in list:
    print(i)
for i in range(len(list)):
    print(list[i])
#append
print("appending the items to the list")
list.append(123)
print(list)
#insert
print("inserting the elements to the list")
list.insert(2,True)
print(list)
#multidimensional creation and access
print("creating multidimensional list")
list1=[[1,2,3],["a","b","c"]]
print(list1)
print("accessing multidimensional list")
print(list1[0][1])
#update
print("updating the lists")
list[4]=False
print(list)
    
