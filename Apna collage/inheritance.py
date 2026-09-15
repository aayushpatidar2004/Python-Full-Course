#SINGLE LEVEL INHERITANCE

# class Car:
#  @staticmethod
#  def start():
#   print("car satrted..")

#  @staticmethod
#  def stop():
#   print("car stopped")

# class toyotaCar(Car):
#  def __init__(self,name):
#    self.name=name
# Car1 =toyotaCar("fortuner")
# Car2 =toyotaCar("prius")

# print(Car1.start())
# **********************************************************
# MULTI LEVEL INHERITANCE
# ---------------------------------------
class Car:
 @staticmethod
 def start():
  print("car satrted..")

 @staticmethod
 def stop():
  print("car stopped")

class toyotaCar(Car):
 def __init__(self,brand):
     self.brand=brand

class fortuner(toyotaCar):
 def __init__(self,type):
   self.type=type



Car1 =fortuner("diesel")
Car1.start()



