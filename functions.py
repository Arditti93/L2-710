# Built in Print function in Python. Needs a pramaeter to run
print("Hello wolrd") 

# Len is another built in function in python
print(len("Hello wolrd"))

# Input is another built in function, allows a user to input something in the terminal
input("Please enter your name - ")

#  -------- Writing our own Functions --------------------- 

# Defining our function
def press_grind_beans():
    print("grinding beans for 20 seconds")

# Calling the function for it to run
press_grind_beans()

# ----------- Pramaeters --------------- 

def cash_machine (amount, accnum):
    # print(amount)
    # print(accnum)
    print(f"Withdraw {amount} from {accnum}.")
    # print("withdrawing 300 from account number 12345")

cash_machine(300, 12356)
cash_machine(150, 7585398)
cash_machine(25, 8787956)


def coffee_order(size, type_of_drink):
    print(f"You have orderd a {type_of_drink} and size {size}")

coffee_order("small", "Flat White")
coffee_order("Large", "Latte")


account_balance = 100
def cash_machine(amount, accnum):
    if amount > account_balance:
        print("Sorry account balance is too low")
    else:
        print(f"Withdrawing {amount} from {accnum}")

cash_machine(65, 13562464)
