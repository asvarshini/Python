#single inhertaince
'''class home:
    def bed(self):
        print("house hasa 1 bedroom")
class house(home):
    def floor(self):
        super().bed()
        print("home has 4 bedroom")
ob =house()
ob.floor()
#write an ex for single inhertannce 
class employ:
    def __init__(self):
        self.name =""
        self.age =0
        self.salary =0.0
        
    
    def read(self):
        self.age=int(input("enter the age of an employee"))
        self.salary=float(input("enter the sa;ary of an employee"))
        self.name=input("enter the name of the employ")
        print(f"name of empoy is :{self.name} and age is : {self.age} \n and salary is {self.salary}")     
class promotion_employee(employ):
    def display(self):
        
        
        if(self.age >= 40 ):
            self.salary =self.salary+self.salary *(20/100)
            print(f"u got promotin and your salary is {self.salary}")

        else:
            print("their is no increment in salary")
while True:

    a= promotion_employee()
    a.read()
    a.display()
    con =input("do you want to continue the program yes or no").strip().upper()
    if(con !="YES"):
        print("exitinf the program")
        break
#multiple inhertanice
class collage():
    def __init__(self):
        self.name =""
        self.age =0
    def read(self):
        self.name=input("enter the name of student")
        self.age=int(input("enter the age of student"))
        print(f"name is :{ self.name} \n age is :{self.age}")
class department():
    def __init__(self):
        self.marks =0
    def display(self):
        self.marks=int(input("enter the marks"))
        print(f'marks is {self.marks}')
class child(collage,department):
    def get(self):
        super().read()
        super().display()
        print("i innerted from pRENT CLASS1,AND CLASS 2")
OB =child()
OB.get()
#multilevel
class grandparent():
    def read(self):
        self.n1 =input("enter your grand parent name")
class parent(grandparent):
    def display(self):
        super().read()
        print(f"my grand parent name is {self.n1}")
        self.n2 =input("enter your parent name")
class sibling(parent):
    def get(self):
        super().display()
        
        print(f"my parnts name is  : {self.n2}")
ob = sibling()
ob.get()  
#Hierachicl level
class parent():
    def read(self):
        print("hi")
class child1(parent):
    def display(self):
        super().read()
        print("hello i am arutha")
class chlid2(parent):
    def get(self):
        super().read()
        print("hello i am varshini as")
ob =child1()
ob.display()
#merhos ovwerriding :-- having same method and parameters but in different class
class Animal():
    def speak(self):
        print("it speak")
class dog(Animal):
    def speak(self):
        print("it bark")
c=dog()
c.speak()'''
#method overloading :-- same method different parameter
class addition():
    def sum(self,a,b=0,c=0):
        return a+b+c
c= addition()
print(c.sum(1,2))
print(c.sum(3,2,1))
       
       