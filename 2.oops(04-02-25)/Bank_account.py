class ATM:
    def __init__(self, card):
        self.card = card
        self.pin = None
        self.cn = None
    
    def InsertCard(self):
        # Get card number and PIN
        self.cn = self.card.getCardNUmber()
        self.pin = self.card.getPin()
        print("Authenticating...")
        
        if self.authenticate(self.cn, self.pin):
            print("Authentication successful!")
            return 'Welcome!'
        else:
            print("Invalid card details.")
            return 'Invalid details'

    def EjectCard(self):
        self.cn = None
        self.pin = None

    def authenticate(self, cn, pin):
        # Call getCardNumber and getPin as methods
        if self.card.getCardNUmber() == cn and self.card.getPin() == pin:
            return True
        else:
            return False

    def DisplayMenu(self):
        print('Menu:')
        print("Press 1 for Check Balance")
        print("Press 2 for Deposit")
        print("Press 3 for Withdraw")
        print("Press 4 for Print Receipt")
        print("Press 5 for Update or Generate PIN")
        
        self.input = int(input())

        if self.input == 1:
            return self.CheckBalance()
        elif self.input == 2:
            self.amount = float(input("Enter Deposit amount: "))
            return self.Deposit(self.amount)
        elif self.input == 3:
            self.amount = float(input("Enter Withdraw amount: "))
            return self.WithDrow(self.amount)
        elif self.input == 4:            
            return self.PrintReceipt()
        elif self.input == 5:
            return self.pingen()
        else:
            return "Invalid input"

    def WithDrow(self, amount):
        return self.card.WithDrow(amount)

    def Deposit(self, amount):
        return self.card.Deposit(amount)

    def CheckBalance(self):
        return self.card.getBalance()

    def pingen(self):
        new_pin = int(input("Enter new PIN: "))
        old_pin = int(input("Enter old PIN: "))
        return self.card.SetPin(new_pin, old_pin)


class Card:
    def __init__(self, account, pin):
        self.balance = account.balance
        self.type = account.type
        self.pin = pin

    def getCardNUmber(self):
        return id(self)

    def getPin(self):
        return self.pin

    def WithDrow(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Successfully withdrew {amount}. New balance: {self.balance}"

    def Deposit(self, amount):
        self.balance += amount
        return f"Successfully deposited {amount}. New balance: {self.balance}"

    def getBalance(self):
        return self.balance

    def SetPin(self, new_pin, old_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            return f"PIN successfully updated!"
        else:
            return "Incorrect old PIN."


class BankAccount:
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type
        self.pin = None

    def getBalance(self):
        return self.balance

    def Deposit(self, amount):
        self.balance += amount
        return f"Successfully deposited {amount}. New balance: {self.balance}"

    def WithDrow(self, amount):
        self.balance -= amount
        return f"Successfully withdrew {amount}. New balance: {self.balance}"

    def SetPin(self, pin, old=None):
        if self.pin is None:
            self.pin = pin
            return "PIN successfully generated!"
        elif self.pin == old:
            self.pin = pin
            return "Old PIN reset and new PIN successfully generated!"
        else:
            return "Enter your old PIN."


m = BankAccount(1000, "Savings")


card = Card(m, 1234)


atm = ATM(card)


atm.InsertCard()


atm.DisplayMenu()
