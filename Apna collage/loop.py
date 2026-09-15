# i =1
# while i<= 5:
#     print(i)
#     i +=1

# print("loop end")

# i =5
# while i>= 1:
#     print(i)
#     i -=1

# print("loop end")
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# i=1
# while i<=100:
#     print(i)
#     i += 1
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# i=100
# while i>=1:
#     print(i)

#     i-=1
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# n= int(input("enter the num : "))

# i=1
# while i<=10:
   
#     print(n*i)
#     i +=1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# list1 =[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(list1):

#   print(list1 [i])
#   i =i+1

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# num =(1,4,9,16,25,36,49,64,81,100)
# x=36

# i=0
# while i<len(num):
#     if(num[i]==x):
        
#        print("found at ind",i)
#     # else:
#     #    print("finding....")
#     i +=1 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# for loop\

# num = [1,2,3,4,5]
# for val  in num:
#     print(val)

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# num =[1,4,9,16,25,36,49,64,81,100]

# for el in num:
#     print(el)

# num =(1,4,9,16,25,36,49,64,81,100,36)
# x =36
# idx =0
# for el in num:
#     if(el== x):
#         print('fond at idx',idx) 
#     idx+=1
  
#     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# RANGE
# for i in range (1,101):  #star ,stop,step
#     print(i)

# # _____________________________
# for i in range(101,0,-1):
#     print(i)
# # ___________________________
# n= int(input('enter the num : '))
# for i in range (1,11):
#   print(n*i)


# for i in range(5):
#      pass
# if i>5:
#      pass
# print("some useful work")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# n= 7
# sum =0
# i=1
# while i<=n:
#         sum+=i
#         i +=1
# print("total sum =",sum)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
n =7
fact =1

for i in range(1,n+1):
    fact =fact*i

  
print("factorial of = ",fact)