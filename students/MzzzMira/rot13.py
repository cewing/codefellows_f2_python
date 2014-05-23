#!/usr/bin/python
import codecs


def rot13 (str_) :
    str_ = list(str_[:])
    for i in range(len(str_)) :
        num = ord(str_[i]) + 13
        if   77<num<104  :
            if num > 90 : num = (num%91) + 65
        elif 109<num<136 :
            if num > 122 : num = (num%123) + 97
        else : continue
        str_[i] = chr(num)

    str_ = "".join(str_)
    return str_


def rot13_builtin (str_) :
    return codecs.encode(str_, 'rot-13')


if __name__ == '__main__' :
    u"Testing ROT13 implementation."
    #str_ = raw_input ('Enter a text to encrypt : \n')
    #str_ = rot13_builtin(str_)
    #print str_
    
    # whitespace, punctuation and capitalization
    # limits
    rot13_test = (
        (' !@#$%^&*', ' !@#$%^&*'),
        ('()_-+=`~[]', '()_-+=`~[]'),
        ('\;      \',', '\;      \','),
        ('./<>?   :"{}|', './<>?   :"{}|'),
        ('ABC abc', 'NOP nop'),
        ('XYZ xyz', 'KLM klm'),
        ('NOP nop', 'ABC abc'),
        ('123 456 789 0', '123 456 789 0'),
    )
    
    for i, expected in rot13_test :
        assert not expected.find(rot13(i),0,len(expected)) 
        assert not expected.find(rot13_builtin(i),0,len(expected)) 
    else :
        print u"All Tests Pass"
    