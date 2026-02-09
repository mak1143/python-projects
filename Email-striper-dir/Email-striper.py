userEmail = input("Enter your email: ").strip()


#check if '@' is missing
if "@" not in userEmail:
    print("Invalid email: missing the '@' symbol.")
else:
    userName , seperator, userDomain = userEmail.partition('@')
    #what is the use partition

#store = help(partition)

print(f"Your userName is: {userName}")
print(f"Your domain is: {userDomain}")


found_numbers = ""
for something in userEmail:
    if something.isdigit():
        found_numbers += something
if found_numbers:
    print(f"Numbers found in email: {found_numbers}")
else:
    print("No numbers found in the email.")
