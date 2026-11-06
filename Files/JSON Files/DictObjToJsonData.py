
#Program for Saving the Dict Object Data into  Json File----By using   str()
dobj={'sno':100,'sname':'rossum','marks':45.6,'cname':'psf'}
print("Dict Object Data={} type={}".format(dobj,type(dobj)))
jsonfmt=str(dobj)
print("json data ={} type={}".format(jsonfmt,type(jsonfmt)))