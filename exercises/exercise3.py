
deposit = "D"
withdrawal = "W"
total_amount = 0

while True:
    transaction = input("Input transaction log (enter q or quit to finish)>>> ")
    if transaction.lower() in ("q", "quit"):
        break
    try:
        action, amount = transaction.split(" ")
        action = action.upper()
        if action == deposit:
            total_amount += float(amount)
        elif action == withdrawal:
            total_amount -= float(amount)
        else:
            print("Transaction has no effect, incorrect input action.")
    except ValueError:
        print("Incorrect input. Try one more time or send `q` to quit")

print(total_amount)
