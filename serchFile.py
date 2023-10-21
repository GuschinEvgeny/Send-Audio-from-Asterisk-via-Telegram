import os
import glob

# Initialize a variable 
inVar = glob.iglob(
    '//monitor/**/in-*.wav',
    recursive = True
    ) # Set Pattern in iglob() function 
# Returning class type of variable 
print(type(inVar)) 
# Printing list of names of all files that matched the pattern 
#print("List of the all the files in the directory having extension .py: ") 
for py in inVar:  
    print(py) 
