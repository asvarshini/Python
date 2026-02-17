# simple calucaltor using functiion
'''
def cal():
    num =int(input("enter the first number :"))
    num1= int(input("enter the second number :"))
    h =input("enter the operation")
    if(h== '+'):
        print("addition of the number is ",num +num1)
    elif(h == '-'):
        print("subtration of the number is",num -num1)
    elif( h == '*'):
        print("multiplication of number is ", num *num1)
    elif(h == '/'):
        print("divesion of the number is ",num/num1)
    else:
        print("you have enter the invalid operand")
cal()
#prime number
def prime(num):
    if(num<2):
        print('it is not prime number')
    for i in range(2,num):
        if(num%i == 0):
            print(" it is not prime number")
            return
    else:
        print("number is prinme number")
        return

prime(3)'''
#find the max of three 
def max(a,b,c):
    if(a>b and a>c):
        print("the max number is : " ,a)
    elif(b>a and b>c ):
        print("the max num is ",b)
    else:
        print("the maxium  number is",c)
max(4,5,6)
#find the sereis of fibnoacci numbers
def fib(n):
    a=0
    b=1
    for i in range(0,n+1):
        s =a+b
        a=b
        b=s
        print(s)
n=int(input("enter the numbers"))
fib(n)