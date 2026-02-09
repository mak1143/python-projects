def convert_cm_to_inches(cm):
    inches = cm / 2.54
    #rounds to 2 decimal places
    return round(inches, 2)

usr_height_cm = float(input("Enter height in cm: "))
print(f"That inches {convert_cm_to_inches(usr_height_cm)}! ")
