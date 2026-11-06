#Program for Reading   JSON File Data into Dict Object --By using load()
import json
with open("D:\\python\\Files\\JSON Files\\dobj.json","r") as fb:
    dobj=json.load(fb)
    print("Json File Data={} type={}".format(dobj,type(dobj)))
print("---------------------------------------")
for k,v in dobj.items():
    print("\t{}--->{}   ".format(k,v))
print("---------------------------------------")