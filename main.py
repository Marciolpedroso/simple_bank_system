print("Welcome to your bank account!")
balance = 0
extrato = ""
limiteSaques = 0
LIMITE_SAQUES = 3

while True:
    print("\nPlease choose an option: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Statement")
    print("4. Exit")
    option = input("Enter your choice (1-4): ")

    if option == "1":
        amount = int(input("Enter the deposit amount: "))
        if amount > 0:
            balance += amount
            extrato += f"Deposit: +${amount:.2f}\n"
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    elif option == "2":
        if limiteSaques >= LIMITE_SAQUES:
            print("You have reached the maximum number of withdrawals for today.")
            continue
        amount = int(input("Enter the withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds.")
        elif amount > 500:
            print("Withdrawal amount exceeds the limit of $500.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            balance -= amount
            extrato += f"Withdraw: -${amount:.2f}\n"
            limiteSaques += 1
            print(f"Withdrew: ${amount:.2f}")

    elif option == "3":
        if not extrato:
            print("No transactions found.")
        else:
            print("Transaction Statement:")
            print(extrato)

        print(f"Current Balance: ${balance:.2f}")       

    elif option == "4":
        print("Thank you for using our banking system. Goodbye!")
        break   