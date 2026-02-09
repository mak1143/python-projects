import random 


def guessNum(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'c':
        if low != high:
            guessNum = random.randint(low,high)
        else:
            guessNum = low
        feedback = input(f"Is it {guessNum}? is it too low (L) , too high (H) or its just correct (C)?: ").lower()
        if feedback == 'l':
            low = guessNum + 1
        elif feedback == 'h':
            high = guessNum - 1
        print(f"I got it! Its {guessNum}")


guessNum(10)



