#write a python program to demonstrat multipal inhertance   reading 5 employis and display and display top 3 students
'''class Employee:
   
    def get(self):
        self.Employee_ID =int(input("enter the employ id"))
        self.Gender =input("enter the gender")
        self.salary=float(input("enter the salary"))
        self.pr_out_of_5=int(input("enter the performance_rating_out of_5"))
        

class JOININGDETAIL:

        def getDOJ(self):
            self.date=int(input("enter the date of joining"))
        
class information(Employee,JOININGDETAIL):
    def read_data(self):
        self.get()
        self.getDOJ()
    def display(self):
         print(f"Employee_ID :{self.Employee_ID} \n Gender :{self.Gender} \n salaery :{self.salary} \n pr:{self.pr_out_of_5} \n dae :{self.date}")
employees = []

# Read 5 employees
for i in range(5):
    print(f"\nEnter details for Employee {i+1}")
    emp = information()
    emp.read_data()
    employees.append(emp)

# Sort employees by date of joining (ascending)
employees.sort(key=lambda x: x.date)

print("\nAll Employees sorted by Date of Joining:")
for emp in employees:
    emp.display()

# Pick top 3 by performance rating
top_employees = sorted(employees, key=lambda x: x.pr_out_of_5, reverse=True)[:3]

print("\nTop 3 Employees by Performance Rating:")
for emp in top_employees:
    emp.display()
## exmaple for polymorphis
class Vechile:
    def Fare(self,amount):
        return amount
bus =Vechile()
car =Vechile()
Train = Vechile()
Truck =Vechile()
shop =Vechile()
a=bus.Fare(20)
a1=car.Fare(30)
a2=Train.Fare(40)
a3=Truck.Fare(30)
a4 =shop.Fare(40)
print("total_Fare  :",a+a1+a2+a3+a4)'''
m ={
    "test 1" :{'dhoni':56,'balaji' :85},
    "test 2" :{ 'dhoni': 87,'balaji':200}
}
def Max_Score(self):
    print(m.max())
