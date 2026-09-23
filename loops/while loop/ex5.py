word=input("Enter a Word / Line of Text:")
print("By Using while Loop in FORWARD Direction with +VE Indices ")
i=0
while(i<=len(word)-1):
    print("\t{}".format(word[i]))
    i=i+1
print("By Using while Loop in FORWARD Direction with -VE Indices ")
i=-len(word)
while(i<=-1):
    print("\t{}".format(word[i]))
    i=i+1
print("By Using while Loop in BACKWARD Direction with +VE Indices ")
i=len(word)-1
while(i>=0):
    print("\t{}".format(word[i]))
    i=i-1
print("----------------------------------------------------")
print("By Using while Loop in BACKWARD Direction with -VE Indices ")
print("----------------------------------------------------")
i=-1
while(i>=-len(word)):
    print("\t{}".format(word[i]))
    i=i-1
print("----------------------------------------------------")
