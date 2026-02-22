'''10 #Design a student management system:

#create a class Student with attributes as like name, roll number and marks. Write the methods to:

# display the student details.

#calculate the grade based on marks

#maintain a list if students and sort them by marks or name.'''
class studen_mangement:
    def __init__(self,name,rool,marks):
        self.name =name
        self.rool =rool
        self.marks =marks
    def display(self):
        if(self.marks>=90):
            self.grade ="A"
        elif(self.marks>= 80 and self.marks <90):
            self.grade ="B"
        elif(self.marks>= 70 and self.marks <80):
            self.grade ="C"
        else:
            self.grade="D"
        print("NAME =",self.name,"ROLL =",self.rool,"MARKS =",self.marks,"GRADE =",self.grade)
    
        
students = [
    studen_mangement("varshini", 1, 99),
    studen_mangement("amrutha", 2, 98),
    studen_mangement("hamsha", 3, 70)
]


for s in sorted(students,key =lambda x:x.name):
    s.display()

print("i modifired here because i want to see in git hub")
#question 1
s = [
    ["Asha", 78],
    ["Ravi", 85],
    ["Kiran", 78],
    ["Meena", 92],
    ["Arun", 85],
    ["Divya", 70]
]

# Extract unique scores and sort them
scores = sorted(set([student[1] for student in s]))

# Find second highest score (runner-up)
sec = scores[-2]

# Collect names with runner-up score
fi = [i[0] for i in s if i[1] == sec]

# Print names in alphabetical order
for name in sorted(fi):
    print(name)
