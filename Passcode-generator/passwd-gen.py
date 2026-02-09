import random
import string

#combine standard character sets
passwd_char = string.ascii_letters + string.digits + string.punctuation

passwd_len = int(input("Enter the length of password: "))

#choices instead of .sample to allow repetitions
passcode = "".join(random.choices(passwd_char,k=passwd_len))

if passwd_len > 0:
    print(f"Generated Password: {passcode}")
else:
    print("Please enter a valid length greater than 0.")
