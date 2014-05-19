myfile = file("rot13_copy.py","r+" )
newfile = file("rot13_new.txt", "w") 
print ("   M A I N - M E N U")
#print (30 * '-')
print ("1. Create a new file")
print ("2. Overwrite an existing file") 
## Get input ###
choice = raw_input('Enter your choice [1-2] : ')
 
### Convert string to int type ##
choice = int(choice)
if choice ==1:
    map(lambda line: newfile.write(line.strip()+'\n') , myfile)
elif choice==2:
    map(lambda line: myfile.write(line.strip()+'\n') , myfile)
myfile.close()
newfile.close()