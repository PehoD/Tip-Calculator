

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

def the_bill ():
    total_tip = tip / 100

    final_bill = bill + (bill * total_tip)

    return final_bill / people


final_amount = round(the_bill(), 2)
print(f"Amount per person: {final_amount} ")


