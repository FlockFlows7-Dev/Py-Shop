# allows to get randomness
import random
# sets balance
balance = random.randint(1, 100)
startbalance = balance
#Prices
applePrice = 1
bananaPrice = 2
orangePrice = 3

# clears the Console in the most stupid way possible...
def clearConsole():
    for x in range(10):
        print("\n")

#shop ui
def shopUI():
    clearConsole()
    print("")
    print("_____________________")
    print("Welcome to Fruity shop")
    print("Fruit Prices: \nApples: 1$ \nBananas 2$\nOranges 3$")
    print("Balance: $",balance)
    print("_____________________")

# to buy Apples
shopUI()
amount = int(input("How many apples do you want to buy? \n"))
totalcost = amount * applePrice
if totalcost > balance:
    if totalcost > 1:
        print(f"You don't have enough money to buy {amount} apples.")
    else:  print(f"You don't have enough money to buy {amount} apple.")

if totalcost <= balance:
    balance = balance- totalcost
    if totalcost > 1:
        print("You bought ", amount, " apples.")
    else: print("You bought ", amount, " apple.")
    print("Balance: $",balance)

if balance == 0:
    if amount > 1:
        print(f"You spent all your money on {amount} Apples...")
    else: print(f"You spent all your money on {amount} Apple.")
    exit()

if amount == 0: print("What are you a Apple hater or something?")

#to buy Bananas
shopUI()
amount = int(input("How many Bananas do you want to buy? \n"))
totalcost = amount * bananaPrice
if totalcost > balance:
    if totalcost > 2:
        print(f"You don't have enough money to buy {amount} Bananas.")
    else:  print(f"You don't have enough money to buy {amount} Banana.")

if totalcost <= balance:
    balance = balance- totalcost
    if totalcost > 2:
        print("You bought ", amount, " Bananas.")
    else: print("You bought ", amount, " Banana.")
    print("Balance: $",balance)

if balance == 0:
    if amount > 1:
        print(f"You spent all your money on {amount} Bananas...")
    else: print(f"You spent all your money on {amount} Banana.")
    exit()

if amount == 0: print("What are you a Banana hater or something?")

#to buy Oranges
shopUI()
amount = int(input("How many Oranges do you want to buy? \n"))
totalcost = amount * orangePrice

if totalcost > balance:
    if totalcost > 3:
        print(f"You don't have enough money to buy {amount} Oranges.")
    else:  print(f"You don't have enough money to buy {amount} Orange.")

if totalcost <= balance:
    balance = balance- totalcost
    if totalcost > 3:
        print("You bought ", amount, " Oranges.")
    else: print("You bought ", amount, " Orange.")
    print("Balance: $",balance)

if balance == 0: exit()
clearConsole()
if balance == startbalance:
    print("Really were you just looking at our fruit the entire time??")
else:
    print("\nThanks for shopping at Fruity Shop!")
exit()




