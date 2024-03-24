#create a class ticket which will be the abstract class
#inside that create a function book ticket which will be the abstract method and have nothing in it
#create a class makemytrip which will use the book ticket function from ticket class to take the details such as name,phone number,emailid
#,journey date
#and displays a message thank you for booking from make my trip
#create a class IRCTC which uses the book ticket of ticket class and takes the same details as make my trip
#but in the end it will give an option to user to select whether it is 1 way or round trip
#if the user option is roundtrip it again asks the user to enter the return date as well and then prints a message thank you for choosing IRCTC
#else prints a message thank you for choosing IRCTC
#create a class indigo which takes the details as the irctc and just asks which mode of transport you want to go in train,flight,bus
#and display thank you for choosing indigo
from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class make_my_trip(ticket):
    def book_ticket(self):
        name=input("Enter your name:")
        phone_number=int(input("Enter your phone number:"))
        emailid=input("Enter your email id:")
        journey_date=input("Enter the Journey date:")
        print("Thank you for choosing Make my trip")
class Irctc(ticket):
    def book_ticket(self):
        name=input("Enter your name:")
        phone_number=int(input("Enter your phone number:"))
        emailid=input("Enter your email id:")
        journey_date=input("Enter the Journey date:")
        while True:
            choose=input("Are you choosing 1. one way \n 2.round trip:")
            choose=choose.lower()
            if choose=="round trip" or choose=="2":
                return_date=date("Enter the return date")
                break
            elif choose=="one way" or choose=="1":
                pass
                break
            else:
                print("choose the correct one")
        print("Thank you for choosing IRCTC")
class Indigo(ticket):
    def book_ticket(self):
        name=input("Enter your name:")
        phone_number=int(input("Enter your phone number:"))
        emailid=input("Enter your email id:")
        journey_date=input("Enter the Journey date:")
        while True:
            choose=input("Are you choosing 1. one way \n 2.round trip:")
            choose=choose.lower()
            if choose=="round trip" or choose=="2":
                return_date=date("Enter the return date")
                break
            elif choose=="one way" or choose=="1":
                pass
                break
            else:
                print("choose the correct one")
        while True:
            transport=input("In which type of transport you are choosing 1. Train \n 2. Flight \n 3. Bus")
            transport=transport.lower()
            if transport=="train" or transport=="flight" or transport=="bus" or transport=="1" or transport=="2" or transport=="3":
                pass
                break
            else:
                print("please choose from the given options:")
        print("Thank you for choosing Indigo")
print("Welcome")
obj1=Indigo()
obj2=Irctc()
obj3=Indigo()
while True:
    a=input("In which you want to book the ticket \n1.Make my trip\n2.Irctc\n3.Indigo")
    a=a.lower()
    if a=="make my trip" or a=="1":
        obj1.book_ticket()
        break
    elif a=="irctc" or a=="2":
        obj2.book_ticket()
        break
    elif a=="indigo" or a=="3":
        obj3.book_ticket()
        break
    else:
        print("choose the one from the given options")
        
        
