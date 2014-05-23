#!/usr/bin/python
import sys


#Write a program that takes a filname and cleans the file be removing all teh leading and trailing whitespace from each line.
#Read in the original file and write out a new one, either creating a new file or overwriting the existing one.
#Give your user the option of which to perform.
#Use map() to do the work.
#Write a second version using a comprehension.

if __name__ == '__main__' :
    choice_ = raw_input ("Do you want to write existing file? yes/no\n")
    while choice_ != 'yes' and choice_ != 'no' :
        choice_ = raw_input ("Do you want to write existing file? yes/no\n")

    filename = sys.argv[1]
    f_source = open (filename, 'rb')
    lines = f_source.readlines()
    
    if choice_ == "yes" : 
        f_dest   = open(filename , 'w')
    else : 
        f_dest   = open("new_"+filename, 'w+')
    
    # with map :
    #lines = map (lambda x : x.strip()+"\n" , lines)
    # with comprehension
    lines = [x.strip()+"\r\n" for x in lines]
    f_dest.writelines (lines)
        
        
