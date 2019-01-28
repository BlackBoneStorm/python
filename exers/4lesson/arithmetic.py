write = input("Please, give correct answer: 4 * 100 - 54 = ")
try:
    write = int(write)
except ValueError:
    print("Please, enter the number.")

correct = 4 * 100 - 54
if write == correct:
    print("You are right! Answer is %d!:)" % correct)
else:
    print("%d is not correct. Correct answer is %d!" % (write, correct))

