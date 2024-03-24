#create a class f15 with functions light,fans and AC
#lights:
#when light function is called it prints out the colour of light
#which is taken as parameter to the function
#fan:
#when fan function is called it displays the regulator speed
#as parameter of the function
#AC:
#it displays the room temperature and the outside temperature
#which are taken as the parameters
#write a fourth function whose name is display
#which displays the difference in outside temperature and inside temoperature of ac and
#also it displays the fan speed
class F15:
    def __init__(self,cs,ce):
        print("its an constructor")
        self.c=cs
        self.e=ce
        print("start time",cs,"\nend time",ce)
    def lights(self,colour):
        print("light is in",colour,"colour")
    def fan(self,speed):
        #variable=value
        self.rspeed=speed
        print("the regulator speed of the fan is",speed)
    def Ac(self,roomtemp,outtemp):
        self.rtemp=roomtemp
        self.otemp=outtemp
        print("room temperature:",roomtemp)
        print("outside temperature:",outtemp)
    def display(self):
        print("difference of the room temp and outside temp is",self.rtemp-self.otemp)
        print("speed of the fan",self.rspeed)
        print(self.c,self.e)
obj=F15("9:00","4:00")
obj.lights(input("enter the light colour:"))
obj.fan(int(input("enter the speed of the regulator:")))
obj.Ac(43,21)
obj.display()
            
