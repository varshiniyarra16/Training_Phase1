#constructor using super Keyword

##class Father:
##    def __init__(self):
##        print("Father:I'm on time for breakfast")
##class me(Father):
##    def __init__(self):
##        super().__init__()
##        print("Me:I'm late for breakfast")
##ob=me()

class Father:
    def __init__(self):
        print("Father:I'm on time for breakfast")
class me(Father):
    def __init__(self):
        Father.__init__(self)
        print("Me:I'm late for breakfast")
ob=me()

#Functions using super keyword can't be done

##class Father:
##    def mobile(self):
##        print("Apple I-phone")
##    def laptop(self):
##        print("Laptop with 200 RAM and 500GB HDD ")
##class me(Father):
##    Father.mobile(self)
##    def mobile(self):#This function is overridden
##        print("As per my interest I need\n Samsung")
##obj=me()
##obj.mobile()
##obj.laptop()
