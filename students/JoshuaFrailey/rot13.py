import string

# construct table
alpha_upper = ""
for i in range(65, 91):
    alpha_upper += chr(i)
alpha13_upper = alpha_upper[13:] + alpha_upper[:13]
alpha_lower = alpha_upper.lower()
alpha13_lower = alpha13_upper.lower()

table_upper = string.maketrans(alpha_upper, alpha13_upper)
table_lower = string.maketrans(alpha_lower, alpha13_lower)

user_text = raw_input(u"Enter text to translate: ")
translation = ''
for letter in user_text:
    if not letter.isalpha():
        translation += letter
    elif letter.isalpha() and letter.isupper():
        translation += letter.translate(table_upper)
    else:
        translation += letter.translate(table_lower)
print "The ROT13 translation is: {}".format(translation)