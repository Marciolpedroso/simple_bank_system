print("Welcome to your bank!")
balance = 0
statement = ""
withdrawals = 0
witidraws_limit = 3
agency = "0001"
users = []
accounts = []

def userRegister(name, dob, cpf, address):
    user = {
        "name": name,
        "dob": dob,
        "cpf": cpf,
        "address": address
    }
    users.append(user)
    print("\nUser registered successfully!")
    return user

def accountRegister(agency, account_number, users):
    if not users:
        print("No users registered. Please register a user first.")
        return None

    print("Select a user by their CPF:")
    cpf = input("Enter CPF: ")
    user = next((user for user in users if user["cpf"] == cpf), None)

    if not user:
        print("User not found. Please register the user first.")
        return None

    account = {
        "agency": agency,
        "account_number": f"{account_number:04d}",
        "user": user
    }
    accounts.append(account)
    print("\nAccount created successfully!")
    return account

def deposit(amount, balance, statement):
    if amount > 0:
        balance += amount
        statement += f"Deposit: +${amount:.2f}\n"
        print(f"Deposited: ${amount:.2f}")
    else:
        print("Deposit amount must be positive.")
    return balance, statement

def withdraw(amount, balance, statement, withdrawals):
    if amount > balance:
        print("Insufficient funds.")
    elif amount > 500:
        print("Withdrawal amount exceeds the limit of $500.")
    elif amount <= 0:
        print("Withdrawal amount must be positive.")
    elif withdrawals >= witidraws_limit:
        print("Daily withdrawal limit reached.")
    else:
        balance -= amount
        statement += f"Withdraw: -${amount:.2f}\n"
        withdrawals += 1
        print(f"Withdrew: ${amount:.2f}")
    return balance, statement, withdrawals

def printStatement(balance, statement):
    print("\nTransaction Statement:")
    if not statement:
        print("No transactions found.")
    else:
        print(statement)
    print(f"Current Balance: ${balance:.2f}")


## MENU ##
while True:
    print("\n=== Menu ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Print Statement")
    print("4. Register User")
    print("5. Create Account")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":
        amount = int(input("Enter deposit amount: "))
        balance, statement = deposit(amount, balance, statement)

    elif option == "2":
        amount = int(input("Enter withdrawal amount: "))
        balance, statement, withdrawals = withdraw(amount, balance, statement, withdrawals)

    elif option == "3":
        printStatement(balance, statement)

    elif option == "4":
        name = input("Enter full name: ")
        dob = input("Enter date of birth (DD/MM/YYYY): ")
        cpf = input("Enter CPF (only numbers): ")
        address = input("Enter address (Street, Number - Neighborhood - City/State): ")
        userRegister(name, dob, cpf, address)

    elif option == "5":
        account_number = len(users) + 1
        account = accountRegister(agency, account_number, users)
        if account:
            print(account)

    elif option == "6":
        print("Thank you for using our services!")
        break

    else:
        print("Invalid option. Please try again.")

