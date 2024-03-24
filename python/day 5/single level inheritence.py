class A:
    def __init__(self,f_name,dept,f_id):
        self.f_name=f_name
        self.dept=dept
        self.f_id=f_id
    def print_info(self):
        print("Class information:",self.f_name,self.dept,self.f_id)
obj=A("Lahari","CSD",4404)
obj.print_info()
class B(A):
    pass
obj=B("abc","csd",4417)
obj.print_info()
