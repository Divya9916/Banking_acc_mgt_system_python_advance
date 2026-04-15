"""
Indian Banking System
"""
import pickle
import os
import numpy as np
from datetime import datetime

# 1. 
DATA_FILE = "easy_bank.dat"
accounts = {}

def load_data():
    global accounts
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            accounts = pickle.load(f)

def save_data():
    with open(DATA_FILE, "wb") as f:
        pickle.dump(accounts, f)
    print("Data saved successfully!")

# 2. 
def create_account():
    name = input("Enter Name: ")
    # Bonus: Login Feature
    pin = input("Set a 4-digit PIN: ")
    print("1. Savings  2. Current")
    acc_type = "Savings" if input("Choice: ") == '1' else "Current"
    
    # Input Validation
    try:
        balance = float(input("Initial Deposit: "))
        if balance < 0: raise ValueError
    except:
        print("Invalid amount!")
        return

    # Auto-generate Account Number
    acc_num = 100001 if not accounts else max(accounts.keys()) + 1
    
    # Store in data structure
    accounts[acc_num] = {
        "name": name, "pin": pin, "type": acc_type, 
        "balance": balance, "history": [balance] 
    }
    print(f"Account Created! Your Account Number is: {acc_num}")

# 3.
def perform_transaction():
    try:
        acc_num = int(input("Enter Account Number: "))
        if acc_num not in accounts:
            print("Account not found!")
            return
        
        # Bonus: Security check
        if input("Enter PIN: ") != accounts[acc_num]["pin"]:
            print("Wrong PIN!")
            return

        print("1. Deposit  2. Withdraw  3. Transfer")
        choice = input("Choice: ")
        
        if choice == '1':
            amt = float(input("Amount: "))
            accounts[acc_num]["balance"] += amt
            accounts[acc_num]["history"].append(amt)
        elif choice == '2':
            amt = float(input("Amount: "))
            # Check balance
            if amt <= accounts[acc_num]["balance"]:
                accounts[acc_num]["balance"] -= amt
                accounts[acc_num]["history"].append(-amt) # Negative for withdrawal
            else:
                print("Insufficient funds!")
        elif choice == '3':
            target = int(input("Recipient Account No: "))
            amt = float(input("Amount: "))
            if target in accounts and amt <= accounts[acc_num]["balance"]:
                accounts[acc_num]["balance"] -= amt
                accounts[target]["balance"] += amt
                accounts[acc_num]["history"].append(-amt)
                accounts[target]["history"].append(amt)
                print("Transfer Successful!")
    except:
        print("Error in transaction.")

# 4. 
def show_report():
    acc_num = int(input("Enter Account Number: "))
    if acc_num in accounts:
        acc = accounts[acc_num]
        print(f"Holder: {acc['name']} | Balance: ₹{acc['balance']}")
        
        # NumPy Statistics
        txns = np.array(acc["history"])
        print(f"Total Transactions: {len(txns)}")
        print(f"Average Transaction: {np.mean(np.abs(txns)):.2f}")
    else:
        print("Account not found.")

# 5. 
def main():
    load_data()
    while True:
        print("""
               Indian Banking System
              """)
        print("\n--- BANKING MENU ---")
        print(["1. New Account  2. Transaction  3. Report  4. Exit"])
        choice = input("Select: ")
        
        if choice == '1': create_account()
        elif choice == '2': perform_transaction()
        elif choice == '3': show_report()
        elif choice == '4': save_data(); break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()