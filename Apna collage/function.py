# def calu_sum(a,b): #parameter  
#     sum=a+b
#     print(sum)
#     return(sum)

# calu_sum(5,10)

# calu_sum(4,9) #function call  / argument
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# cities =['delhi','gurgaon','hedrabad','pune']
# hero=['ram','ajay','captain ' ]
# def print_len(list):
#     print(len(list))
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(cities)
# print_list(hero)
# print()
# char ch1='a';
# print(char ch1)




# f=open("demo.txt","r")

# data =f.read()
# print(data)
# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

# f.close()

# import os 
# os. remove("demo.txt")
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# class Student:  #class
#     name="aayush"

# s1=Student()  #object
# print(s1.name) 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# construcotr
# class Student:

#     def __init__(self,fullname):
#       self.name =fullname
#       print("adding new student in database")

# s1=Student("karan")
# print(s1.name)

# s2=Student("pooja")
# print(s2.name)


class Student:
  college_name="abc college"

  def __init__(self,name,marks):
    self.name =name
    self.marks=marks

  def welcome(self):
    print("welcome student," ,self.name)

  def get_marks(self):
    return self.marks
s1=Student("karan",97)
s1.welcome()
print(s1.get_marks())
