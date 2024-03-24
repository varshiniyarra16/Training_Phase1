class A:
    print("hello")
    def info(self):
        print("good Morning")
class B:
    print("Namasthe")
class c(A,B):
    pass
obj=c()
obj.info()
