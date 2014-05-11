def rot13(str):
    import string 
    tran_list=[]
    alphabet_lower = string.lowercase
    alphabet_upper = string.uppercase
    test_table = []
    new_str = ''.join([char for char in str if char in (alphabet_lower + alphabet_upper)])
    for i in range (len(str)):
        if str[i] in alphabet_lower:
            x = alphabet_lower.find(str[i])
            if 25 - (x+13) < 0:
                letter_13 = (x+13) % 25 - 1
            else:
                letter_13 = x + 13                  
            tran_list.append(alphabet_lower[letter_13])
            tran_str= ''.join(tran_list)
        elif str[i] in alphabet_upper:
            x = alphabet_upper.find(str[i])
            if 25 - (x+13) < 0:
                letter_13 = (x+13) % 25 -1
            else:
                letter_13 = x + 13                
            tran_list.append(alphabet_upper[letter_13])
            tran_str= ''.join(tran_list)
    tran_table = string.maketrans(new_str, tran_str)
    str_encripted = str.translate(tran_table)
    return str_encripted
    if __name__ == '__main__': 
        #assert len(str) = len(rot13(str))
test_table = []
for i, val in enumerate(alphabet_lower):
            #test_table.append.(list(enumerate(alphabet_lower, start=1))[i+13][1])
    test_table.append([i, val])
for i in range(len(alphabet_lower)):
    if i <=12:
        test_table.append([test_table[i][1], test_table[i+13][1]])
    elif i > 12:
        test_table.append([test_table[i][1], test_table[(i+13)%25-1][1]])

print test_table


