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
    test_str = 'abcdefghijklmnopqrstuvwxyz, ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(test_str)):
        if test_str[i] in string.lowercase:
            if ord(test_str[i]) <= 109 and ord(test_str[i]) > 78:
                assert ord(rot13(test_str)[i]) - ord(test_str[i]) == 13   
            elif ord(test_str[i]) > 109:
                assert ord(rot13(test_str)[i]) - ord(test_str[i]) == -13 
        elif test_str[i] in string.uppercase:
            if ord(test_str[i]) <= 77:
                assert ord(rot13(test_str)[i]) - ord(test_str[i]) == 13   
            elif ord(test_str[i]) > 77 and ord(test_str[i]) < 109:
                assert ord(rot13(test_str)[i]) - ord(test_str[i]) == -13 
        print "Passed All Tests"   

     




