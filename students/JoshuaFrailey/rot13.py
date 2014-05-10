import string

# construct table
# alpha_upper = ""
# for i in range(65, 91):
#     alpha_upper += chr(i)
# alpha13_upper = alpha_upper[13:] + alpha_upper[:13]
# alpha_lower = alpha_upper.lower()
# alpha13_lower = alpha13_upper.lower()

# table_upper = string.maketrans(alpha_upper, alpha13_upper)
# table_lower = string.maketrans(alpha_lower, alpha13_lower)

# user_text = raw_input(u"Enter text to translate: ")
# translation = ''
# for letter in user_text:
#     if not letter.isalpha():
#         translation += letter
#     elif letter.isalpha() and letter.isupper():
#         translation += letter.translate(table_upper)
#     else:
#         translation += letter.translate(table_lower)
# print u"The ROT13 translation of {} is: {}".format(user_text, translation)

alpha = u""
for i in range(65, 91):
    alpha += unichr(i)
alpha13 = alpha[13:] + alpha[:13]
# print "alpha is: {}; alpha13 is: {}".format(alpha, alpha13)
for i in range(97, 123):
    alpha += unichr(i)
# print "alpha is: {}; alpha13 is: {}".format(alpha, alpha13)
alpha13 = alpha13 + alpha[-13:] + alpha[-26:-13]
# print "alpha is: {}; alpha13 is: {}".format(alpha, alpha13)
table = string.maketrans(alpha, alpha13)

user_text = raw_input(u"Enter text to translate: ")
translation = user_text.translate(table)

print u"The ROT13 translation of {} is: {}".format(user_text, translation)
