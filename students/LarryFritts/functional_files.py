import codecs
import sys

filename = sys.argv[1]

read_file = codecs.open(filename, 'r')
working_str = read_file.readlines()
read_file.close()

final_str = []
for i in working_str:
    final_str.append(i.strip())


user_input = raw_input(u"\nDo you want to write to the same file (y/n)? ")
while not (user_input == u'y' or user_input == u'n'):
    user_input = raw_input(u"\nPlease enter 'y' or 'n'!")
if user_input == u'y':
    pass
else:
    w_filename = raw_input(u"\nWhat file do you want to write to? ")

write_file = codecs.open(w_filename, 'w')
for line in final_str:
    write_file.write(line + '\n')
write_file.close()
