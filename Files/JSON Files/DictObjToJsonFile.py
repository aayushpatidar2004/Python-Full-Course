#Program for Saving the Dict Object Data into  Json File----By using   dump()

import json
dobj={'sno':100,'sname':'rossum','marks':45.6,'cname':'psf'}

with open("D:\\python\\Files\\JSON Files\\dobj.json","w") as fb:
    
    json.dump(dobj,fb)
    print("Dict Object Data saved into Json File Successfully")