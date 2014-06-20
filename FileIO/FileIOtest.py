file = open("C:\Users\Kaya\Documents\Python2014\FileIO\python.txt",'r')
print file

line = file.readline()
target1 = " in "
target2 = " at "
target3 = " of "
changeTo = " *** "
print "original \n" + line + "\n"

if((target1 in line) or (target2 in line) or (target3 in line)):
    replaced = line.replace(target1,changeTo)
    changed = replaced.replace(target2, changeTo)
    change = changed.replace(target3, changeTo)
    print change
else:
    print "\n this sentence does not have any target word."
        
    



x = " "
replaced = line.replace(x," &&& ")
print replaced +"\n\n"


#Not work
#print file.readline().replace("  in  "," *** ")



print "\nend!"



#filedata = file.read()
#print filedata + "\n"
#print file.readlines()
"""
for line in file:
    print line 
    print "\n"
"""

"""
print "\nreading line \n\n"
line1 =  file.readline()
line2 = file.readline()
line3 = file.readline()
#print file.readlines()
print line1 + "\n\n"
print line2 + "\n\n"
print line3

print "\nhello"
"""
