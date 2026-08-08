print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_pct = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = (tip_pct / 100) * bill

total_per_person = round((tip + bill)/people, 2)

print("Each person should pay: $" + str(total_per_person))



