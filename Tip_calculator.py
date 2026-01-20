print("Welcome to the tip calculator!")
Bill=float(input("What is your total bill? $"))
Tip=int(input("How much Tip would you like to give 10,12 or 15?" ))
tip_percentage=(Bill*(Tip/100))
people=int(input("How many people to split the bill?"))
Total_bill=Bill+tip_percentage
final_bill=Total_bill/people
print(f"Each person should pay:{final_bill}")