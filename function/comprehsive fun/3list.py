lst=[10,21,30,40,13,15,12]
el=[val for val in lst if val % 2 == 0]
ol=[val for val in lst if val % 2 != 0]
print("even list:",el)
print("odd list:",ol)