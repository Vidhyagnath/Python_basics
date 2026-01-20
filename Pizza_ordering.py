print("Welcome tp Python Pizza Deliveries!")
size= input("What size Pizza do you want?S, M or L:")
pepperoni = input("Do you want pepperoni in your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
# code for Pizza size bill
if size =="S":
    bill +=15
elif size =="M":
    bill +=20
elif size =="L":
    bill +=25
else:
    print("You have chosen an invalid size")

#code for pepperoni
if pepperoni =="Y":
    if size =="S":
        bill +2
    else:
        bill +=3

#code for extra cheese
if extra_cheese =="Y":
    bill +=1

#final bill
print(f"Your final bill is: ${bill}.")