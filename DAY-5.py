<<<<<<< HEAD
#polymorphism(many forms same method for diffent behaviour
#no overloding (same method name different parameter) overriding (same method name in different class)

class animal:
  def sound(self):
    print("They make sound")
class dog:
  def sound(self):
    print("They bark")
class cat:
  def sound(self):
    print("they meow")
s1 =dog()
s1.sound()
s2 =cat()
s2.sound()
# or
#mehod overloading
class cal:
    def add(self,a,b=0,c=0):
        print(a+b+c)
ob =cal()
ob.add(1,2)
ob.add(1,5,6)
#Encapsulation(Wrapping data (variables) and methods (functions) inside a class and restricting direct access to them.)
#Python uses:Public  Protected  Private
#example for public (no underscore,can acess outside class,default)
class per:
    def __init__(self,age):
        self.age=age
s1=per(21)
print(s1.age)
#or
class per:
    def show(self,age):
        return age
s1=per()
print(s1.show(21))
#acess in different class
class per:
    def __init__(self,age):
        self.age=age
class chi(per):
    def show(self):
        print(self.age)

s2=chi(21)
s2.show()
#protected(use one underscore,it is same as public but technically telling as it is protected)
class per:
    def __init__(self,age):
        self._age=age
s1=per(21)
print(s1._age)
#or
class per:
    def show(self,_age):
        return _age
s1=per()
print(s1.show(21))
#acess in different class
class per:
    def __init__(self):
        self._age=22
class chi(per):
    def show(self):
        print(self._age)

s2=chi()
#private (using  2 undersccore,cannot acess in class directely)
# 1(a) acessinfg private members in same class 

class nam:
    def __init__(self):
        self.name="var"
        self.__age =22
s1=nam()
print(s1.name)
print(s1._nam__age)#thise also wrok but not good practice
#or
class nam:
    def __init__(self):
        self.name="var"
        self.__age =22
    def show(self):
        return self.__age
s1=nam()
print(s1.name,s1.show())
#1 (b) acessing from different class
class nam:
    def __init__(self):
        self.name="ammu"
        self.__age =26
    def show(self):
        return self.__age
class b(nam):
    def read(self):
        print(self.name,self.show())
s1=b()
s1.read()
# 1(c) acess private in child class




class per:
    def __init__(self,__age):
        self.__age=__age
    def read(self):
        return self.__age
s1=per(21)
print(s1.read())
print(s1._per__age)#not good practice
#Trying in different class
class per:
    def __init__(self):
        self.__age=22
    def get(self):
        return self.__age  #TO ACESSS VALUES OF PRIVATE CLASS YOU NEED TO DEFINE A METHOD FIRST  
class chi(per):
    def show(self):
        print(self.get())

s2=chi()
s2.show()
#peivate and public
class stu:
    def __init__(self,name,__age):
        self.name=name
        self.__age=__age
    def set(self):
        return self.__age
    def get(self):
        print("name =",self.name,"age=",self.__age)#orself.set()

s1 =stu("varshini",21)
s1.get()
#example for 3 together(private member acn acess freeliy inside same same class,not in child class and another class)
class  company:
    def __init__(self,name,_accno,__balance):
        self.name =name
        self._accno =_accno
        self.__balance=__balance
    def set(self):
       return self.__balance
    def deposite(self,amo):
        self.__balance +=amo
        print("name =",self.name,"accno =",self._accno,"balance =",self.__balance)
    def withdraw(self,am):
        if(self.__balance>am):
            self.__balance-=am
            print("name =",self.name,"accno =",self._accno,"balance =",self.__balance)
        else:
            print("not suffiecient balance")
s1=company("amrutha",26,2000)
s1.deposite(2000)
s1.withdraw(1000)
print(s1.name)
print(s1.set())#private members cannot acess overcome by name mangling
print("i am learing git")
print("i stage and commit because eariler commit was done befor pull")
        
        





=======
 #polymorphism(many forms same method for diffent behaviour
#no overloding (same method name different parameter) overriding (same method name in different class)

class animal:
  def sound(self):
    print("They make sound")
class dog:
  def sound(self):
    print("They bark")
class cat:
  def sound(self):
    print("they meow")
s1 =dog()
s1.sound()
s2 =cat()
s2.sound()
# or
#mehod overloading
class cal:
    def add(self,a,b=0,c=0):
        print(a+b+c)
ob =cal()
ob.add(1,2)
ob.add(1,5,6)
#Encapsulation(Wrapping data (variables) and methods (functions) inside a class and restricting direct access to them.)
#Python uses:Public  Protected  Private
#example for public (no underscore,can acess outside class,default)
class per:
    def __init__(self,age):
        self.age=age
s1=per(21)
print(s1.age)
#or
class per:
    def show(self,age):
        return age
s1=per()
print(s1.show(21))
#acess in different class
class per:
    def __init__(self,age):
        self.age=age
class chi(per):
    def show(self):
        print(self.age)

s2=chi(21)
s2.show()
#protected(use one underscore,it is same as public but technically telling as it is protected)
class per:
    def __init__(self,age):
        self._age=age
s1=per(21)
print(s1._age)
#or
class per:
    def show(self,_age):
        return _age
s1=per()
print(s1.show(21))
#acess in different class
class per:
    def __init__(self):
        self._age=22
class chi(per):
    def show(self):
        print(self._age)

s2=chi()
#private (using  2 undersccore,cannot acess in class directely)
class per:
    def __init__(self,__age):
        self.__age=__age
    def read(self):
        return self.__age
s1=per(21)
print(s1.read())
print(s1._per__age)#not good practice
#Trying in different class
class per:
    def __init__(self):
        self.__age=22
    def get(self):
        return self.__age  #TO ACESSS VALUES OF PRIVATE CLASS YOU NEED TO DEFINE A METHOD FIRST  
class chi(per):
    def show(self):
        print(self.get())

s2=chi()
s2.show()
#peivate and public
class stu:
    def __init__(self,name,__age):
        self.name=name
        self.__age=__age
    def set(self):
        return self.__age
    def get(self):
        print("name =",self.name,"age=",self.__age)#orself.set()

s1 =stu("varshini",21)
s1.get()
#example for 3 together(private member acn acess freeliy inside same same class,not in child class and another class)
class  company:
    def __init__(self,name,_accno,__balance):
        self.name =name
        self._accno =_accno
        self.__balance=__balance
    def set(self):
       return self.__balance
    def deposite(self,amo):
        self.__balance +=amo
        print("name =",self.name,"accno =",self._accno,"balance =",self.__balance)
    def withdraw(self,am):
        if(self.__balance>am):
            self.__balance-=am
            print("name =",self.name,"accno =",self._accno,"balance =",self.__balance)
        else:
            print("not suffiecient balance")
s1=company("amrutha",26,2000)
s1.deposite(2000)
s1.withdraw(1000)
print(s1.name)
print(s1.set())#private members cannot acess overcome by name mangling
        
        






>>>>>>> 53e8798f010d72f7d3cb1d88fcf7ad401d197eed
