print("Welcome to the tip calculator!")
try:
    bill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? 0 to 100 "))
    people = int(input("How many people to split the bill? "))
except ValueError:
    print("Please enter valid numbers.")
else:
    if bill < 0:
        print("The bill cannot be negative.")
    elif not 0 <= tip <= 100:
        print("The tip percentage must be between 0 and 100.")
    elif people <= 0:
        print("The number of people must be greater than zero.")
    else:
        tip_as_percent = tip / 100
        total_tip_amount = bill * tip_as_percent
        total_bill = bill + total_tip_amount
        bill_per_person = total_bill / people
        final_amount = round(bill_per_person, 2)
        print(f"Each person should pay ${final_amount:.2f}")