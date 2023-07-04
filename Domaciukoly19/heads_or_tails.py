import random

coin = ["Heads", "Tails"]
cointoss = random.choice(coin)

selection = input("Heads or Tails: ").lower()

if selection == cointoss:
    print("You win! The coin landed on " + cointoss)
else:
    print("You lose. The coin landed on " + cointoss)

print("The End!")

