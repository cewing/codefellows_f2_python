import string
from urllib2 import *
url = urlopen('http://codefellows.github.io/sea-c15-python/_downloads/sherlock_small.txt')
contents = url.readlines()
ls_orig = []
ls = []
ls_dict=[]
dictionary = {}
text_new = []
for line in contents:
    string_new = ''.join(ch for ch in line if ch in string.letters or ch in string.whitespace or ch == '-')
    string_striped = string_new.strip('')
    ls_orig.extend(string_striped.split(" "))
for i in range(len(ls_orig)-1):
    ls.append(ls_orig[i].strip('--\r\n'))
print ls
for i in range (len(ls) - 4):
    #ls_dict.append([ls[i] + ' ' + ls[i+1], [ls[i+2]]])
    #print ls_dict
    #dictionary = dict(ls_dict)
    #print dictionary
    dictionary.setdefault(ls[i] + ' ' + ls[i+1], []).append(ls[i+2])
for k, v in dictionary.items():
    text_new.append(k + ' ' + v[0])
    text_new1 = ' '.join(text_new)
print text_new1[len(text_new1)-1]
    dictionary[text_new[len(text_new)-1]]
    
    print text_new
#print dictionary

file1 = open('sherlock_small.txt')
print file.read()