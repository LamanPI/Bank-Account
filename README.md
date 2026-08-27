# Bank-Account
Bank Account System
# Bank Account System

A simple command-line bank account management system built with Python.

## Features

The program allows users to:

* Create a new bank account
* Log in to an existing account
* Deposit money
* Withdraw money
* Check the current balance
* Store account information in a text file

## How It Works

When the program starts, the user enters their name and chooses whether they already have an account.

### Existing Account

If the user already has an account, the program checks the entered password against the saved account information.

If the password is correct, the user can access their account.

### New Account

If the user does not have an account, they can create one by entering:

* First name
* Last name
* Password

The new account is saved in `accounts.txt` with an initial balance of `0`.

## Account Operations

After logging in, the user can choose one of the following operations:

* `deposit` — add money to the account
* `withdraw` — withdraw money from the account
* `check balance` — display the current balance

The program also prevents users from withdrawing more money than their current balance.

## Data Storage

Account information is stored in a text file called:

```text
accounts.txt
```

Each account is stored in the following format:

```text
name:password:balance
```

## How to Run

Make sure Python is installed on your computer.

Run the program with:

```bash
python bank_account.py
```

The `accounts.txt` file will be created automatically when a new account is registered.

## Technologies

* Python
* Object-Oriented Programming (OOP)
* Classes and Objects
* File Handling
* Dictionaries
* `try/except`
* User Input
