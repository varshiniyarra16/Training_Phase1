#function overriding
class Father:
    def mobile(self):
        print("Apple I-phone")
    def laptop(self):
        print("Laptop with 200 RAM and 500GB HDD ")
class me(Father):
    def mobile(self):#This function is overridden
        print("As per my interest I need\n Samsung")
obj=me()
obj.mobile()
obj.laptop()
