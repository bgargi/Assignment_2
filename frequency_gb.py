a=raw_input('Please enter the string.')
d={} #defining a dictionary , say d

for x in range(ord('a'),ord('z')): #Varying x from ascii values of a to z
	d[chr(x)]=0                #Setting initial count of each letter to 0

for x in a:                        #Here x takes value of all letters present in string
  for y in range(ord('a'),ord('z')): #Basically matching each  letter with the list of ascii codes
    if y==ord(x):
       d[chr(y)]=d[chr(y)]+1

print d 
  
