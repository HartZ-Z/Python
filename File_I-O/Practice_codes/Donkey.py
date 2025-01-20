word = "donkey"

with open ( "Donkey.txt",  "r") as f:
    content = f.read ()

contentNew=content.replace(word,"####")

with open ("Donkey.txt" , "w") as f:
    f.write(contentNew)