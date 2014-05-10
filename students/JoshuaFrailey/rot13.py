import string

# construct table
alpha_upper = ''
for i in range(65, 91):
    alpha_upper += chr(i)
alpha13_upper = alpha_upper[13:] + alpha_upper[:13]
alpha_lower = alpha_upper.lower()
alpha13_lower = alpha13_upper.lower()

table_upper = string.maketrans(alpha_upper, alpha13_upper)
table_lower = string.maketrans(alpha_lower, alpha13_lower)
