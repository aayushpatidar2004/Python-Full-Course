lst=[10,17,-2,0,5,6,7,8,9,-22]
pd={val: val **2 for val in lst if val > 0}
nd={val: val **2 for val in lst if val < 0}
print("positive dictionary:",pd)
print("negative dictionary:",nd)