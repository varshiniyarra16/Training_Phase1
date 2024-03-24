#write a program to check the type of triangle
##where you take the input from user for three sides
##and classify it accordingly into equilateral,isoceless,scalene
a=int(input("enter the side a:"))
b=int(input("enter the side b:"))
c=int(input("enter the side c:"))
if a==b==c:#all sides are equal
    print("Equilateral triangle")
elif a==b or a==c or b==c:#any two sides should be equal
    print("Isosceles triangle")
elif a!=b!=c:#no sides should be equal
    print("Scalene triangle")
#you can also use the else condition for scalence
#i have used it for just denoting scalene triangle formula

