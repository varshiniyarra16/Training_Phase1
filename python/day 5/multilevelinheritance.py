#create a class of name PLACEMENTS
#which has a function info which displays we have 623 selects and still counting.
#create another class name department
#with function display which will display the names of departments present in the college
#create a class pragati
#with a function welcome which displays the message welcome to pragati engineering college we are glad to have you on board
#this pragati class should also display the details about departments and placements
class Placements:
    def info(self):
        print("The count of the placements this year was 623 and still counting**")
class department(Placements):
    def display(self):
        departments=["Civil","Mech","ECE","EEE","CSE","IT","CSD","CSE-AI","CSE-AIML"]
        print("The departments in our college are\n",departments)
class Pragati(department):
    def welcome(self):
        print("Welcome to Pragati engineering portal \n We are glad to have you on board")
prag=Pragati()
prag.welcome()
prag.display()
prag.info()
    
    
    
