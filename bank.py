class Bank:
    acno = 0
    name = ""
    Bank = ""
    branch = ""
    balance = 0

    def createaccount(obj):
        obj.acno = int(input("Enter account number: "))
        obj.name = input("Enter name of account holder:  ")
        obj.Bank = input("Enter name of Bank: ")
        obj.branch = input("Enter Bank branch: ")
        obj.balance = float(input("Enter account balance: "))

    def displayaccount(obj):
        print("Account no: ", obj.acno)
        print("Name of account holder: "), obj.name
        print("Name of Bank: ", obj.Bank)
        print("Name of branch: ", obj.branch)
        print("Balance: ", obj.balance)

    def deposit(obj):
        deposamt = int(input("Enter amount to be deposited: "))
        obj.balance = obj.balance + deposamt
        print("New balance is: ", obj.balance)

    def withdraw(obj):
        withamt = float(input("Enter amount to be withdrawn: "))
        if (obj.balance < withamt):
            print("low balance!!")
        elif (obj.balance > withamt):
            obj.balance = obj.balance - withamt
            print("Amount withdrawl success")
            print("Updated balance is : ", obj.balance)


customers = []
while (True):
    print("=" * 100)
    print("1.Create account")
    print("2.Display account")
    print("3.Deposit ")
    print("4.Withdraw")
    print("5.Fund Transfer")
    print("0.Exit")
    print("=" * 100)

    print()
    choice = int(input("Enter choice: "))
    print()

    if (choice == 1):
        cust=Bank()
        cust.createaccount()
        customers.append(cust)
    elif (choice == 2):
        acno = int(input("Enter customer Account Number: "))
        isfound = False
        for cust in customers:
            if (cust.acno == acno):
                cust.displayaccount()
                isfound = True
                break
        if (isfound == False):
            print("Invalid Account! ")
    elif (choice == 3):
        acno = int(input("Enter customer account number: "))
        isfound = False
        for cust in customers:
            if (cust.acno == acno):
                cust.deposit()
                isfound = True
                break
        if (isfound == False):
            print("Invalid Account! ")

    elif (choice == 4):
        acno = int(input("Enter customer account number"))
        isfound = False
        for cust in customers:
            if (cust.acno == acno):
                cust.withdraw()
                isfound = True
                break
            if (isfound == False):
                print("Invalid Account")
    elif (choice == 5):
        acno = int(input("Enter customer account number: "))
        bacno = int(input("Enter beneficiay account number: "))
        isfound = False
        for cust in customers:
            if (cust.acno == acno):
                print("enter details: ")
                isbfound = False
                for bcust in customers:
                    if (bcust.acno == bacno):
                        amt = float(input("Enter amt to transfer: "))
                        cust.balance -= amt
                        bcust.balance += amt
                        isbfound = True
                        break
                if (isbfound == False):
                    print("Invalid beneficary account: ")
            isfound = True
            break
        if (isfound == False):
            print("Invalid Account")

b1 = Bank()
b1.createaccount()
b1.displayaccount()
b1.deposit()
b1.withdraw()
