#Abstraction(it hides the implementation)
'''from abc import ABC,abstractmethod #(means in abc modlule contain ABC class and abstractmathod is function inside in that class )
class payment:
    @abstractmethod
    def pay(self):
        pass   #pass means contain only body in thise we can only declare not usemethod
class debit(payment):
    def pay(self,amount):
        print("paied",amount,"through debit card")
class upi(payment):
    def pay(self,amount):
        print("paied",amount,"through UPI")
s1 =debit()
s1.pay(200)
s2 =upi()
s2.pay(1000)'''
#calculator using abstration
from abc import ABC,abstractmethod
class cal:
    
    def add(self):
        pass
    
    def sub(self):
        pass
    
    def mul(self):
        pass
    
    def div(self):
        pass
class calulate(cal):
    def __init__(self,a,b):
        self.a =a
        self.b=b
    def add(self):
        print("sum=",self.a+self.b)
    def sub(self):
        print("sub =",self.a-self.b)
    def mul(self):
        print("mul=",self.a*self.b)
    def div(self):
        print("divi=",self.a/self.b)
ob = calulate(15,5)
ob.add()
ob.sub()
ob.mul()
ob.div()
#or
from abc import ABC,abstractmethod
class cal:
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def mul(self):
        pass
    @abstractmethod
    def div(self):
        pass

    def __init__(self,a,b):
        self.a =a
        self.b=b
    def add(self):
        print("sum=",self.a+self.b)
    def sub(self):
        print("sub =",self.a-self.b)
    def mul(self):
        print("mul=",self.a*self.b)
    def div(self):
        print("divi=",self.a/self.b)
ob = cal(10,5)
ob.add()
ob.sub()
ob.mul()
ob.div()


