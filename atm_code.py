balance=2000
ministate=[]
def credit():
    global balance
    amount=float(input("enter the amount"))
    if amount>=0:
        balance+=amount
        ministate.append(f"credit amount{amount}")
        print("successful credit")
        print(f"balance {balance}")
       
    else:

        print("enter the valid number")
    
def debit():
    global balance
    amount=float(input("enter debit amount"))
    if amount<=balance:
        balance-=amount
        ministate.append(f"debit amount{amount}")
        print("debit successful")
        print(f"debit amount{balance}")
    elif amount>balance:
        print("enter the valid number")
def balanc():
    global balance
    print(f"check balance {balance}")

def ministatement():
    for i in ministate:
        print(i)
        print("balance{balance}")
def exit_amount():
    
    print("thank you for visit")
while True:
    print("ATM")
    print("1. credit")
    print("2. debit")
    print("3. balance")
    print("4. mimistatement")
    print("5. exit")
    choice=(input("choice the number 1 t0 5"))
    if choice=="1":
        credit()
    elif choice=="2":
        debit()
    elif choice=="3":
        balanc()
    elif choice=="4":
        ministatement()
    elif choice=="5":
        exit_amount()
        break
    else:
        print("enter valid number")

