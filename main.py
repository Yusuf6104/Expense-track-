expenses = []

def load_expenses():
     try:
          with open("expenses.txt","r") as file:
               for line in file:
                    amount, category, note = line.strip().split(",")
                    expenses.append({
                         "amount":float(amount),
                         "category":category,
                         "note": note
                    })
     except FileNotFoundError:
         pass                    
def add_expense():
    amount=float(input("enter the amount:",))
    category=input("Write the catogary name:",)
    note=input("write a note:",)

    expense={
        "amount": amount,
        "category":category,
        "note": note 
    }

    expenses.append(expense)
    
    with open("expenses.txt", "a") as file:
              file.write(f"{amount},{category},{note}\n")

    print("Expenses added successfully!\n")

def view_expenses():
        if not expenses:
            print("No expenses recorded.\n")
            return
        
        
        for exp in expenses:
            print(f"{exp['catogory']} - ₹{exp['amount']} - {exp['note']}")

def total_expense():
    total=0
    for exp in expenses:
          total += exp["amount"]
    print(f"\nTotal Expense: ₹{total}\n")   

def menu():
     while True:
          print("1. Add expenses")
          print("2. View Expenses")
          print("3. Total expenses")
          print("4. Exit") 

          choice = input("choose an option:",)

          if choice == "1":
                add_expense()
          elif choice == "2":
                view_expenses()
          elif choice == "3":
                total_expense()
          elif choice == "4":
                print("Goodbye 👋") 
          else:
               print("Invalid choice. Try again.\n")
load_expenses()              
menu()    


     
