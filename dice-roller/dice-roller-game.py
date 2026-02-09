import random



#keeps iterating 
while True:
    print("Rolling Dice....")

    print(f" The value is ", random.randint(1,6))


    repeat_el = input("ROll Dice again? 'y' for yes & 'n' for no: ")

    if repeat_el == 'n':
        #ADD ERRORS TO ANY OTHER INPUT EXCEPT Y & N
        break
