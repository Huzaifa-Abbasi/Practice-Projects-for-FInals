''' Password Generator:
1.Create a program that generates a random password for the user.
2.The password should include a combination of uppercase and lowercase letters, numbers, and special characters.
3.Allow the user to specify the desired password length'''

import random
import string
length = int(input("Enter the Length of password"))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation
password = " "
for i in range(length):
    next = random.choice(chars)
    password += next
print(password)