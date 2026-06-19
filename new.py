#f = open("myfile.txt","x")
with open("demofile.txt" , "w") as f:
    f.write("oops!! whats that!!")

with open("demofile.txt" , "r") as f:
    print(f.read())

with open("demofile.txt" , "a") as f:
    f.write("ewww!1 whats thatt!! bruhhhhh")

    #to delete file
    import os
os.remove("demofile.txt")




