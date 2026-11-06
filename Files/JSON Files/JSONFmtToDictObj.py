#Program for Converting JSON Data Format into Dict Object---by using  loads()
import json

jsonfmt='{"sno":100,"sname":"rossum","marks":45.6,"cname":"psf"}'

print("Json Data={} type={}".format(jsonfmt,type(jsonfmt)))
dobj=json.loads(jsonfmt)
print("Dict Object Data={} type={}".format(dobj,type(dobj)))
for k,v in dobj.items():
    print("\t{}--->{}   ".format(k,v))