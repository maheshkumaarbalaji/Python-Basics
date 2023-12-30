import textwrap

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_list = textwrap.wrap(str, 4)
print('\n'.join(str_list))