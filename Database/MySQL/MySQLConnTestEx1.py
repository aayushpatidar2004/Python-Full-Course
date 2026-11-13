
#MySQLConnTestEx1.py
import mysql.connector as mc #step-1
try:
    conobj=mc.connect(host="127.0.0.1",
                      user="root",
                      passwd="@Aayush123")#Step-2
    print("Python Program Got Connection from MySQL Data Base")
except mc.DatabaseError as e:
    print("Problem in MySQL Data Base:",e)