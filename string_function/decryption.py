"""
2. Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd
"""
import re

decrypted=""
encrypted=input("enter the encrypted string:")
patterns=re.findall(r'([a-zA-z]+)(\d+)',encrypted)
for pattern in patterns:
    decrypted += pattern[0] * int(pattern[1])

print(f'the decrypted string is:{decrypted}')
print(f"length of the decrypted string is:{len(decrypted)}")

"""
OP:
enter the encrypted string:ac2acc#cd3
the decrypted string is:acaccdcdcd
length of the decrypted string is:10

enter the encrypted string:ac2bd3
the decrypted string is:acacbdbdbd
length of the decrypted string is:10
"""
