# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ____ apples and your change is ____ pesos.

def amountMoney():
    _money = int(input("How much money do you have? "))
    return _money

def priceApple():
    _priceA = int(input("How much is an apple? "))
    return _priceA

def totalApples():
    _totalA = moneyA // appleP
    return _totalA

def Change():
    _change = moneyA % appleP
    return _change

def display(appleT, change):
    print(f"You can buy {appleT} apples and your change is {change} pesos.")

# steps
# 1. ask for the amount of money you have then save to variable
moneyA = amountMoney()
# 2. ask for the price of an apple then save to variable
appleP = priceApple()
# 3. solve for the total amount of apples you can buy then save to variable
appleT = totalApples()
# 4. solve for the change then save to variable
change = Change()
# 5. display the total number of apples and the change
display(appleT, change)