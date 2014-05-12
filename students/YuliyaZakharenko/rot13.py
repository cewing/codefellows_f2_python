import string 
def rot13(str):
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
    test_str = 'az'
    for i in range(len(test_str)):
        int_letter = string.lowercase.find(test_str[i])
        enc_letter = string.lowercase.find(rot13(test_str)[i])
        if ord(test_str[i]) <= 109:
            assert enc_letter - int_letter == 13   
        elif ord(test_str[i]) > 109:
            assert enc_letter - int_letter == -13 
        print "Passed All Tests"   

     




