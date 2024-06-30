


import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "[]{}()#@!,:;.'_/%$?+%&*"

upper, lower, nums, symb = True, True, True, True
char_List= ""

if upper:
    char_List += uppercase_letters
if lower:
    char_List += lowercase_letters
if nums:
    char_List += digits
if symb:
    char_List += symbols


length=int(input("enter desired password length"))
times=int(input( "enter number of times"))

for i in range(times):
    generated_password = "".join(random.sample(char_List, length))
    print(generated_password)
print("\n")

