print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    Age=int(input("What is your age?"))
    if Age<=12:
        bill=5
        print("Child tickets are $5")
    elif Age<=18:
        bill=7
        print("Youth tickets are $7")
    elif Age>=45 and Age<=55:

        print("You are totally free")
    else:
        bill = 12
        print("Adults tickets are $12")

    wants_photo = input("Do you want photo taken?Y or N")
    if wants_photo == "y":
        bill += 3

    print(f"your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")