#fibnocci series
prev2=0
prev1=1
print("Fibnocci series")
print(prev2)
print(prev1)
for i in range(8):#for i in range(3,11):
    fibno=prev2+prev1
    print(fibno)
    prev2=prev1
    prev1=fibno
