# Banking System (Bank Account Simulator)

This is a simple banking system in Python, where the user can perform **deposit**, **withdrawal**, **check statement**, and view the **current balance**.

## Features

- **Deposit**: The user can deposit a positive amount into the account.
- **Withdrawal**: The user can make withdrawals, with the following restrictions:
  - The maximum number of withdrawals per day is **3**.
  - The maximum amount per withdrawal is **$500**.
- **Statement**: The user can check the statement with all the transactions made so far.
- **Balance**: The system keeps track of the current balance, updating it after each deposit or withdrawal.

## How to Run

1. **Prerequisites**:
   - This project is developed in **Python 3.x**.

2. **Running the Project**:
   - Clone the repository to your computer:
     ```bash
     git clone https://github.com/your-username/repository-name.git
     ```
   - Navigate into the project folder:
     ```bash
     cd repository-name
     ```
   - Run the script:
     ```bash
     python file-name.py
     ```

## How It Works

1. **Deposit**: The user can deposit an amount into the account, and the balance will be updated. The deposit will be recorded in the statement.
2. **Withdrawal**: The user can withdraw funds, respecting the limitations of withdrawal amount (maximum $500 per withdrawal) and the daily withdrawal limit of 3 withdrawals.
3. **Statement**: The user can check all transactions made (deposits and withdrawals) so far.
4. **Exit**: The user can exit the system.

### Example Interaction

```bash
Welcome to your bank account!

Please choose an option: 
1. Deposit
2. Withdraw
3. Statement
4. Exit
Enter your choice (1-4): 1
Enter the deposit amount: 100
Deposited: $100.00
