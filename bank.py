class BankAccount():
    """
    BankAccount class to store the balance, and the holder
    """
    def __init__(self, balance, holder):
        """
        
        """
        self.balance = balance
        self.holder = holder
    
    def deposit(self, amount):
        """
        Deposits the amount of the balance

        Argumenten:
         - amount (int): the number of amount to withdraw
        """
        self.balance += amount

    
    def withdraw(self, amount):
        """
        Withdraws the amount of the balance

        Argumenten:
         - amount (int): the number of amount to withdraw
        """
        # Checks if the balance is enough for the withdrawel
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print(f"Not enough money, you only have {self.balance}")
    
    def info(self):
        return f"The bankaccount from {self.holder} has a balance of {self.balance}"


           


bank1 = BankAccount(100, 'Tessel')
bank2 = BankAccount(50, 'Bart')
bank3 = BankAccount(1000, 'Janneke')

bankaccounts = [bank1, bank2, bank3]
while True:
    # Ask the user which account to access
    print("Which account do you want to access?")
    for i, bankaccount in enumerate(bankaccounts):

        print(f"\t [{i+1}] {bankaccount.holder}")
    print("\t [4] No account")
    
    choice = int(input('\n'))
    
    if choice == 4:
        # If there is no account o acces, break the while loop
        break
    
    else:
        todo = int(input("What do you want to do? Withdraw [1], deposit [2] or infomartion [3]"))
        if todo == 1:
            amount = int(input("How many money do you want to withdraw?"))
            bankaccounts[choice-1].withdraw(amount)
        elif todo == 2:
            amount = int(input("How many money do you want to deposit?"))
            bankaccounts[choice-1].deposit(amount)
        elif todo == 3:
            print(bankaccounts[choice-1].info())        
        else:
            "There is no such action"

    
