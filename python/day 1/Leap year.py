#check the year given is leap year or not
##if the year is divisible by 4
##and not divisible by 100
##or if it is divisible by 400
##then it is called a leap year
year=int(input("enter a year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print("not a leap year")
