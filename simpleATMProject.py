balance = 30000

print("Welcome to Simple Bank ATM!")
while True:
    input_text = """
    What do you want to do?
    1. Check Balance
    2. Deposit Amount
    3. Withdraw Amount
    4. Exit Program
    """
    user_input = int(input(input_text))

    if user_input == 1:
        print(f"Your balance is: {balance}")

    elif user_input == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Balance deposited successfully. Your current balance is: {balance}")
    elif user_input == 3:
        amount = float(input("Enter amount to withdraw: "))

        if balance >= amount:
            balance -= amount
            print(f"Balance withdrew successfully. Your current balance is: {balance}")
        else:
            print("Insufficient Balance!")

    elif user_input == 4:
        print("Thank you for using Simple Bank ATM")
        break
    else:
        print("Error! Invalid Choice. Please try again!")
