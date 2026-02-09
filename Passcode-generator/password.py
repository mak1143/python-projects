import string,random

allChar = string.ascii_letters + string.digits + string.punctuation


#now you can pick from this pool
length = 15
password = "".join(random.choices(allChar, k=length))


print(password)
