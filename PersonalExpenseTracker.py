# -*- coding: utf-8 -*-
"""
@author: Susmita Tripathi
"""

#personal expense tracker
import csv

expenseList = []
global totalBudget

def personal_expense_tracker():
    load_expenses()
    while True:
        user_choice()
        choice = input("\nEnter your choice: ")
        string_choice = "\nChoice: " + choice
        
        if choice == '1':
            print(string_choice + " : Add Expenses")
            add_expenses()
        elif choice == '2':
            print(string_choice + " : View Expenses")
            view_expenses()
        elif choice == '3':
                print(string_choice + " : Track Budget")
                save_budget()
                track_budget()
        elif choice == '4':
            print(string_choice + " : Save Expenses")
            save_expenses()
        elif choice == '5':
            print(string_choice + " : Exit")
            break
        else:
            print(string_choice + " : Invallid Choice. Please choose an option from the menu.")

def user_choice():
    print("\n\nMenu:")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")
    
def add_expenses():
    expenseDate = input("Enter date of expense in format YYYY-MM-DD: ")
    expenseCategory = input("Enter category of expense (Food/Travel): ")
    expenseAmount = input("Enter expense amount: ")
    expenseDescription = input("Enter expense description: ")
    expense = { "date" : expenseDate, "category" : expenseCategory, "amount" : expenseAmount, "description" : expenseDescription }
    expenseList.append(expense)
    
def view_expenses():
    for i in expenseList:
        record = True
        if (i.get("date") == ""):
            print("Record incomplete. Missing value: Date")
            record = False
        if (i.get("category") == ""):
            print("Record incomplete. Missing value: Category")
            record = False
        if (i.get("amount") == ""):
            print("Record incomplete. Missing value: Amount")
            record = False
        if (i.get("description") == ""):
            print("Record incomplete. Missing value: Description")
            record = False   
        if(record):
            print("Record | Date: " + str(i.get("date")) + " | Category: " + str(i.get("category")) + " | Amount: " + str(i.get("amount")) + " | Description: " + str(i.get("description")) )

def save_budget():
    global totalBudget
    totalBudget = float(input("Enter your monthly budget: "))
    
def track_budget():
    global totalBudget
    totalSpend = 0
    for i in expenseList:
        totalSpend += float(i.get("amount"))  
    if((totalSpend) > float(totalBudget)):
        print("You have exceeded your budget!")
    else:
        balance = float(totalBudget) - totalSpend
        print("Remaining Balance: ",balance)
        
def load_expenses():
    filename="personalExpenseTracker.csv"
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenseList.append(row)
        print("Previous expenses loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")


def save_expenses():
    filename="personalExpenseTracker.csv"
    with open(filename, "w", newline="") as file:
        fieldnames = ["date", "category", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenseList)       
        
personal_expense_tracker()
