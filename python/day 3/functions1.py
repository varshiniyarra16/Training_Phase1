def fun(a,b):
    print(a,b)
fun(3,2)
def an(name,a):
    print("these are",a,name)
an(a="keyword",name="arguments")
def we(a="default",name="arguments"):
    print("these are",a,name)
def func(**name):
    print("these are",name["fname"],name["lname"])
an(a="keyword",name="arguments")
we()
func(fname="unknown",lname="arguments")
