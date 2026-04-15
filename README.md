# Indian Banking System: Account Management Automation

## Project Overview
This project is a Python-based Bank Account Management System designed to simulate real-world banking workflows. It provides a secure, menu-driven interface for managing customer accounts, performing financial transactions (deposits, withdrawals, transfers), and maintaining data persistence using file handling. The system focuses on robust input validation and transaction tracking to ensure financial data integrity.

## Repository Structure
<img width="539" height="316" alt="image" src="https://github.com/user-attachments/assets/9ec46ff9-2b7c-4330-8626-33336c27583e" />


## Technical Workflow
1. System Architecture & Data Storage
Data Persistence: Utilized the pickle module to serialize and deserialize Python objects, allowing account data to be saved permanently to a binary file and retrieved across different sessions.

Efficient Data Structures: Employed Dictionaries to store customer information where the Account Number serves as the unique key, ensuring O(1) lookup time for transactions.

Transaction History: Integrated Lists within the customer object to maintain a chronological log of all deposits and withdrawals for audit purposes.

2. Core Banking Functionalities
Account Lifecycle: Managed the full lifecycle from account creation (assigning unique account numbers and secure PINs) to closing or updating records.

Financial Operations:

Deposits & Withdrawals: Implemented logic to update account balances while validating that withdrawal amounts do not exceed the current balance.

Fund Transfers: Developed a secure transfer mechanism that simultaneously updates the sender's and recipient's ledgers.

Reporting: Built a report generator that provides a snapshot of account details, including current balance and recent activity.

3. Security & Validation
PIN Authentication: Implemented security checks requiring a valid PIN for any transaction-related activity.

Input Validation: Integrated error handling to manage invalid inputs, such as non-numeric amounts or non-existent account numbers, preventing system crashes.

## Key Features
Menu-Driven Interface: A user-friendly command-line menu offering options for "New Account," "Transaction," "Report," and "Exit."

Real-World Simulation: Mimics actual banking logic, including minimum balance requirements and transaction success/failure notifications.

Automated Record Keeping: Every transaction is automatically saved to the file system, ensuring no data loss.

## Final Deliverables
Banking_system_code.py: The complete Python script containing the banking engine and data management logic.

Banking System project.pdf: A visual presentation detailing the programming solutions (Dictionaries, File Storage) used to meet banking needs.

Problem Statement: The foundational document outlining the project scope and functional requirements.

## Tools & Concepts Used
Language: Python

Libraries: pickle (for file handling/serialization)

Programming Concepts: Object-Oriented Logic, Dictionaries, File I/O, Error Handling, and Conditional Logic.

## Author

Divya Sharma
Email: divya649sharma99@gmail.com
GitHub: github.com/Divya9916
LinkedIn: www.linkedin.com/in/divya9916

## License

This project is open source and available under the MIT License.
