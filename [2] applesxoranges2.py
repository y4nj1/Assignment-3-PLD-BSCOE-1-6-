# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ________.

def showPriceA():
    _PriceA = 20
    print(f"The price of an apple is {_PriceA} pesos.")
    return _PriceA
    

def showPriceO():
    _PriceO = 25
    print(f"The price of an orange is {_PriceO} pesos.")
    return _PriceO

def amountA():
    _AmountA = int(input("How many apples will you buy? "))
    return _AmountA

def amountO():
    _AmountO = int(input("How many oranges will you buy? "))
    return _AmountO

def totalP():
    _TPApple = PriceApple * QuantiApple
    _TPOrange = PriceOrange * QuantiOrange
    _TotalPrice = _TPApple + _TPOrange
    return _TotalPrice

def display(TotalPrice):
    print(f"The total amount is {TotalPrice} pesos.")

# steps
# 1. show the price of an apple then set as variable
PriceApple = showPriceA()
# 2. show the price of an orange then set as variable
PriceOrange = showPriceO()
# 3. ask how many apples will they buy then save to variable
QuantiApple = amountA()
# 4. ask how many oranges will they buy then save to variable
QuantiOrange = amountO()
# 5. solve for the total price then save to variable
TotalPrice = totalP()
# 6. display the total price
Total = display(TotalPrice)