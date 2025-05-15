print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_no = int(input("How many people to split the bill? "))
bill_per_person = (bill + bill * tip / 100) / people_no
bill_per_person_approx = round(bill_per_person, 2)

print(f"Each person should pay: ${bill_per_person_approx}")