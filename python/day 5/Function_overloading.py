#function overloading-python doesn't support it
class arithmetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
ob=arithmetic()
##ob.add(10)#missing 2 positional arguments
##ob.add(10,20) #missing 1 positional arguments
ob.add(10,20,30)
        
    
