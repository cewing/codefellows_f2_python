def rot13(str):
    import string 
    tran_list=[]
    tran_str=''
    alphabet_lower = string.lowercase
    alphabet_upper = string.uppercase
    new_str = ''.join([char for char in str if char in (alphabet_lower + alphabet_upper)])

    for i in range (len(str)):

        #new_str = ''.join([char for char in str if char in alphabet_upper])
        #tran_char = alphabet[alphabet.find(str[i])] + 13
        if str[i] in alphabet_lower:
            x = alphabet_lower.find(str[i])
            if 25 - (x+13) < 0:
                letter_13 = (x+13) % 25 - 1
            else:
                letter_13 = x + 13                  
            tran_list.append(alphabet_lower[letter_13])
            tran_str= ''.join(tran_list)
            #print new_str, tran_str
        elif str[i] in alphabet_upper:
            x = alphabet_upper.find(str[i])
            if 25 - (x+13) < 0:
                letter_13 = (x+13) % 25 -1
            else:
                letter_13 = x + 13   
            #tran_list.append(alphabet_lower[letter_13])               
            tran_list.append(alphabet_upper[letter_13])
            tran_str= ''.join(tran_list)
            #print new_str, tran_str
    tran_table = string.maketrans(new_str, tran_str)
    str_encripted = str.translate(tran_table)
    print str_encripted
    print new_str, tran_str, alphabet_upper
