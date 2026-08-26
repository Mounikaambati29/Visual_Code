# bank management code
class Account:      #this is the parent class
    def __init__(self, username, password, balance=0):  #it is constructor
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = [] 
# transactions is an empty list used to store deposit and withdrawal details.

#DEPOSIT

    def deposit(self, amount):  # it takes amount is an argument
        if amount > 0:
            self.balance += amount
            self.transactions.append( 
                f"Deposited: {amount}"
            )
            print("Amount deposited:", amount)
            print("Current balance:", self.balance)
        else:
            print("Enter a valid amount")

# WITHDRAW
    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= self.balance:
            self.balance -= amount
            self.transactions.append(
                f"Withdrawn: {amount}"
            )
            print("Amount withdrawn:", amount)
            print("Remaining balance:", self.balance)
        else:
            print("Insufficient balance")

#CHECK BALANCE

    def check_balance(self): #displays the current balance of the account
        print("Current balance:", self.balance)
# self.balance is used  to access the balance of the current account.

#MINI STATEMENT

    def mini_statement(self):  #it shows the transactions history
        print("\n------ MINI STATEMENT ------")
        print("Username:", self.username)
        if len(self.transactions) == 0: #if the transaction list is empty it print no transaction
            print("No transactions")  
        else:
            for transaction in self.transactions:
                print(transaction)
        print("Current Balance:", self.balance) #finally current balance is displayed

# CHILD CLASS

class SavingsAccount(Account): #saving acccount is the child class to account
    def __init__(self, username, password, balance=0):
        super().__init__(username, password, balance) 
# SavingsAccount inherits the properties and methods from the account class
# Therefore, SavingsAccount can use:
# deposit()
# withdraw()
# check_balance()
# mini_statement()
# super() is used to call the constructor of the parent class
# It initializes username, password, balance, and transactions.

# ACCOUNT TYPE

    def show_account_type(self): #show_account_type() method belongs to saving account class
        print("Account Type: Savings Account")  # it displays the type of account
# This is an additional method provided by the child class.


# BANK CLASS 

class Bank:  # bank class is used to manage all customer accounts
    def __init__(self):
        self.accounts = {} #dictionary stores the user name as key
# Account object as the value.

# CREATE ACCOUNT 

    def create_account(self, username, password): #create_account()method creates newbankaccount
        if username in self.accounts:
            print("Username already exists")
        else:
            account = SavingsAccount(username, password)
            self.accounts[username] = account
            print("Account created successfully")
# First, it checks whether the username already exists in account dictionary 
# If the username already exists, it displays:"Username already exists"
# Otherwise a new SavingsAccount object will be created.
# The account object is stored in the accounts dictionary.
# The username is used as the key and the account object is stored as value

#  LOGIN 

    def login(self, username, password): #login() method is used to authenticate the user
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login successful")
                return account
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        return None
# it checks whether the username exists in the dictionary
# If the username exists,the corresponding Account object is retrieved from the dictionary
# Then the entered password is compared with the stored password.
# If both username and password are correct:
#    Login successful
# The account object is returned.
# If the username or password is incorrect,the appropriate error message is displayed
# None is returned when login fails.


# CREATE BANK OBJECT 

bank = Bank() # Here we create an object of the Bank class.
# The object is stored in the variable named bank.
# We can use now:
# bank.create_account()
# bank.login()


#  MAIN MENU 

while True:
    print("\n------ PYTHON BANK ------")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
# while True loop continuously displays the main menu.
# The loop continues until the user selects the Exit option.
# The user gets three options:
# 1. Create Account
# 2. Login
# 3. Exit


#  CREATE ACCOUNT 

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(username, password)

# If the user selects option 1,the program asks for username and password
# Then the create_account() method of the Bank object is called.
# The username and password are passed as arguments.


#  LOGIN ----------------

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        account = bank.login(username, password)
# If the user selects option 2,the program asks for username and password
# The login() method checks the entered details.
# If login is successful, it returns the Account object.
# That object is stored in the account variable.


        if account is not None:
            while True:
                print("\n------ ACCOUNT MENU ------")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Account Type")
                print("6. Logout")
                choice = input("Enter your choice: ")

# If login is successful, the account menu is displayed.
# The account menu contains:
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Mini Statement
# 5. Account Type
# 6. Logout
# Another while loop is used here so that the user can
# perform multiple banking operations after logging in.


           #  DEPOSIT 

                if choice == "1":
                    amount = int(
                        input("Enter amount: ")
                    )
                    account.deposit(amount)
# If the user selects option 1,the program asks for the deposit amount.
# The deposit() method of the Account object is called.
# The amount is passed as an argument.



                #  WITHDRAW 

                elif choice == "2":
                    amount = int(
                        input("Enter amount: ")
                    )

                    account.withdraw(amount)
# If the user selects option 2,the program asks for the withdrawal amount.
# The withdraw() method is called using the Account object.


                #  CHECK BALANCE 

                elif choice == "3":
                    account.check_balance()
# If the user selects option 3,the check_balance() method is called.
# It displays the current account balance.


                # MINI STATEMENT 

                elif choice == "4":
                    account.mini_statement()
# If the user selects option 4,the mini_statement() method is called.
# It displays the username, all transactions,and the current account balance


                # ACCOUNT TYPE 

                elif choice == "5":
                    account.show_account_type()
# If the user selects option 5,the show_account_type() method is called.
# This method belongs to the SavingsAccount child class.
# It displays:
# Account Type: Savings Account
# This demonstrates the childclass can have its own methods in addition to inherited methods.
# its own methods in addition to inherited methods.


                #  LOGOUT 

                elif choice == "6":
                    print("Logged out successfully")
                    break
# If the user selects option 6,the user is logged out.
# The break statement exits the inner while loop
# and takes the user back to the main bank menu


                # INVALID ACCOUNT MENU 

                else:
                    print("Invalid choice")
# If the user enters a choice other than 1 to 6,the program displays "Invalid choice".


    # EXIT 

    elif choice == "3":
        print("\nThank you for using Python Bank")
        break

# If the user selects option 3 from the main menu,the program displays a thank-you message.
# The break statement exits the outer while loop and completely stops the program.


    #  INVALID MAIN MENU

    else:
        print("Invalid choice")
# If the user enters a choice other than 1, 2, or 3,the program displays "Invalid choice".

# # ---------------- FINISHED ----------------
# # ---------------- THANK YOU ----------------