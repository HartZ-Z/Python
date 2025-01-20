
with open ( "This.txt" ) as f :
    original = f.read()

with open ( "This_copy.txt " , "w") as f:
    copy = f.write (original)

# Now to check if the content copied over is the same or not 

with open ( "This_copy.txt") as f:
    check = f.read()

if (check == original ):
    print(" The content has been copied over successfully ")

else:
    print(" No the content has not been transfered over successfully ")