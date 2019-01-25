import random

deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

random.shuffle(deck)

print("Let's play Blackjack!")
count = 0

while True:
    choice = input("Do you need a card? y/n\n")
    if choice == 'y':
        current = deck.pop()
        print("You took this card: %d" %current)
        count += current
        if count > 21:
            print("You have %d points. You lost:(" %count)
            break
        elif count == 21:
            print("You won!")
            break
        else:
            print("You have %d points." %count)
    elif choice == "n":
        print("You have %d points and the game is stopped." %count)
        break

print("Good Day!")
