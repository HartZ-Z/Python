with open ("Donkey.txt") as f:
    lines = f.readlines()

lineno = 1 

for line in lines:
    if ("donkey" in line):
        print (f" Yes Doneky is present in the text and it's at line No : {lineno}")
        break
    lineno += 1 
else:
    print("The word donkey is not present in the text")
