class father:
    def a(self):
        print("hi")
    def b(self):
        print("L")
class child(father):
    def b(self):#method overriding
        print("Lahari")
obj=child()
obj.a()
obj.b()
