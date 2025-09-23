#write the dictonary and intilize the values
'''fruitr ={
    "apple" :[2,4,5],
    "mango" :[7,2,1],
    "guva" :  [2,5,6]
}
print(fruitr)
#write the set and perform union and intersection

s1={1,23,5,7,3}
s2={1,3,7,9,7,6}

union_set =s1.union(s2) #for union set
print(union_set)
intersection_set =s1 and s2  #for intersection set
print(intersection_set)
#swap the two numbers eithout using inbulit function
def swap(n1,n2):
    temp =n1 
    n1=n2
    n2 =temp
    return n1,n2
n1 =int(input("enter the n1 value"))
n2 =int(input("enter the value of n2"))
print("the values before awaping",n1,n2)
n1,n2 =swap(n1,n2)
print("values after awaping",n1,n2)
#find the largestt element index from  your list withput using predefined function

def getmax(arr):
    max =0
    for i in range(len(arr)):
     if(arr[i]>arr[max]):
        max =i
    return max
arr =[3,6,9,10,33]
s=getmax(arr)
print(s)
##in dictinory intilize each value
tu ={
    "name":["varsh","ammu","prathu","sri"],
    "age ":[21,26,31,42],
    "fav":["biriyani","chicken","non_veg","none"]
}
for x,y in tu.items():
    print(x,y)
#code to remove particular elemt from list
l1 =[4,6,9,2]
print(l1.remove(2))
#print the mutiplication table
n =int(input("ener the numbern u want to do mulitiplication"))
for i in range(1,11):
    print(n ,"*",i ,"=",n*i)'''
#make class student and storee information age and name using constructor
class student:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def display(self):
        print(f"{self.name } is the name of student")
        print("age of the student is",self.age)
ob =student("var",3)
ob.display()


