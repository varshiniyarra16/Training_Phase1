#write a function to calculate sum of first and last digit of a number
#the number should be taken as an argument
def calculate(num):#543
    n=num%10#3
    while num>10:
        num=num//10#54#5
    sum=num+n
    print(sum)
calculate(int(input()))
        
        
