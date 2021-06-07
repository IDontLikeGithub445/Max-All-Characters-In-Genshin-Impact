#I don't know how to do all of the fancy command line prompt things like I see youtube-dl doing, so I'll just use a python script instead

#Anyway,
#Tired of all of my terrible, and annoying comments?
#Get rid of em! Courtesy of me.


import random
import time

print("New file is written in the same directory as the Old file")
print("File Location?  (' and \" are automatically ignored, \\ are automatically doubled)")
File = input("> ")
File = File.replace("\"", "")
File = File.replace("\\", "\\\\")
print(File)

NewFile = File.replace(".py", "")
NewFile = NewFile + "_Copy" + str(round(random.random(), 2)*100) + ".py" #Just prevent overriding a pre-existing file

with open(NewFile, "w") as NewFile2:
    with open(File, "r") as OpenFile:
        while True:
            New_Line = OpenFile.readline()
            if New_Line == "":
                break
            if "####" in New_Line:
                pass
            elif "#" in New_Line:    
                New_Line = New_Line.split("#")
                if New_Line[0] == "":
                    continue
                New_Line = str(New_Line[0]) + "\n"
            NewFile2.write(New_Line)
print("done...?")
time.sleep(50)
        
