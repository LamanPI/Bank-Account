class BankAcc():
    def __init__(self,name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance

    def login(self):
        entered_password = int(input("Enter your password: "))
        if entered_password == self.password:
            print("Login successful!")
        else:
            print("Wrong password!")
    
    def deposit(self):
        amount = int(input("Input the amount you want to deposit: "))
        self.balance = self.balance + amount
        print(f"Deposited amount: \n New balance: {self.balance}")

    def withdraw(self):
        value = int(input("Enter the value you want to withdraw: "))

        if value > self.balance:
            print("Invalid number")

        else:
            self.balance = self.balance - value
            print(f"Withdrawn amount: \n New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance {self.balance}")


user_database = {}

try:
    with open("accounts.txt", "r") as file:
        for line in file:
            existing_user, existing_password, existing_balance = line.strip().split(":")
            user_database[existing_user] = {
                "password": int(existing_password),
                "balance": int(existing_balance)
            }
except FileNotFoundError:
    pass


name = input("Input your name, please").strip()
choice = input(f"Welcome, {name} do you have an acc? --> Yes/No ").strip().lower()

account = None

if choice =="yes":
    if name in user_database:
        entered_password = int(input("Enter your password: "))
        if entered_password == user_database[name]["password"]:
            print("Login successful!")
            account = BankAcc(name, user_database[name]["password"], user_database[name]["balance"])
        else:
            print("Wrong password!")
    else:
        print("Account not found in our database!")

elif choice == "no":
    lname = input("Enter your last name: ")
    new_password = int(input("Create a password (numbers only): "))
    initial_balance = 0
    with open("accounts.txt", "a") as file:
        file.write(f"{name}:{new_password}:{initial_balance}\n")
    print("Registration successful!")
    account = BankAcc(name, new_password, initial_balance)


if account != None:
    move = input("What do you want to do --> withdraw/deposit/check balance").strip().lower()
    if move =="deposit":
        account.deposit()
    elif move =="withdraw":
        account.withdraw()
    elif move =="check balance":
        account.check_balance()
    else:
        print("Invalid input")
