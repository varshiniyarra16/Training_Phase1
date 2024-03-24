#constructor Overriding
class Father:
    def __init__(self):
        print("Father:I'm on time for breakfast")
class me(Father):
    def __init__(self):
        print("Me:I'm late for breakfast")
ob=me()

#method-2
##class Father:
##    def __init__(self):
##        print("Father:I'm on time for breakfast")
##class me(Father):
##     pass
##ob=me()
