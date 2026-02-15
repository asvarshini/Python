#it contains question
'''
1. Create a function named 'check string', the function should 
accept a string data from the user and the function should check
 if the user input contains the letters in it. If it contains the 
letter 's' then print- The string is containing the letter 's", 
if not then print "The string doesn't contain the letter 's'".'''
class check:
    def check_string(self,name):
        if "s" in name.lower():
                print("The string contain letter S")
                
            
        else:
            print("The string doesn't contain the letter 's'")
name =str(input("enter the name"))      
ob =check()
ob.check_string(name)
'''
2. Create a class named 'Super' and inside that class define a user-defined function named funt.
#a. inside the 'funl' function, pass the message "This is functionl in the super class."'''
class Super:
    def funll(self):
        print("Thise is functional in super class ")
#ob1 =super()
#ob1.funll()
3#Create another class named "Modified_Super and inherit this class from the Super class.
#a. Inside the "Modified Super' class, create a function named funl and pass the following message
#inside the print statement: 'This is functioni in the Modified Super class'
#b. Create another user-defined function named 'fun2' and pass the message: 'This is the 2nd function from the modified class?
#c. Now create an object Modified_Super class and call the fun1().
class Modified_Super(Super):
    def funl(self):
        super().funll()
        print("thise is modified super class")
    def fun2(self):
        print("Thise is the 2nd function from the modified class")
b =Modified_Super()
b.funl()
#4
class Polymor:
    
    def hello(self, a):
        print("This function only has 1 argument")
    
    def hello(self, a, b):
        print("This function has 2 arguments")


obj = Polymor()

#obj.hello(5)        # calling 1 argument
obj.hello(5, 10)    # calling 2 arguments
'''
#5 #Create a class named parent Class and inside the class, initialize a global variable num as 10.
#reate another class named child_Class and this class should be inherited from the parent class.
b. Now create an object for the child Class and with the help of child Class object, display the value of "num". '''
class parent:
    
    def read(self):
         self.num =10
         return self.num
        
class child_class(parent):
    def numb(self):
        super().read()
   
        print(self.num)
ob =child_class()
ob.numb()
#or
class parent:
    def __init__(self):
        self.num=40
class child(parent):
    def __init__(self):
        super().__init__()
o =child()
print(o.num)
#6 The C class should inherit from class A, and B. Inside the class C, create a 
# #constructor, and inside the constructor, call the constructor of class A.
class a:
    def __init__(self):
        print("It is the constructtor of class a")
class b:
    def __init__(self):
        pass
class c(a,b):
    def __init__(self):
        super().__init__()
        #a.__init__(self)
ob =c()
#7 Now, create a method inside the class C, as get details, and this function should #return the value of a name.
class a:
    def __init__(self):
       self.name =10
      
class b:
    def __init__(self):
        pass
class c(a,b):
    def __init__(self):
        super().__init__()
        #a.__init__(self)
    def get_details(self):
        return self.name
ob =c()
print(ob.get_details())
#8 #Create a class named Employee, with a constructor init method that accepts name and 
# #salary as parameters and set properties named name and salary.
class Employ:
    def __init__(self,name ,salary):
        self.name =name 
        self.salary =salary
    def read(self):
        return self.name,self.salary
ob =Employ("varshini",100000000000)
print(ob.read())
# 9 student name marks print name result if marks is greater than 40
class result:
    def reaf(self,name,marks):
        if(marks >40):
            print("✌️✌️ pass","NAME =",name,"MARKS =",marks)
        else:
            print("FAIL")
ob = result()
ob.reaf("Varshini",99)


