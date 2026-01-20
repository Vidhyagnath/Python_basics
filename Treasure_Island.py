print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossrods = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()
if crossrods=="left":
    choice1=input( 'You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice1=="wait":
        choice2=input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice2 == "red":
            print("you entered a fire room, GAME OVER")
        elif choice2 == "yellow":
            print("You found the tressure" , "YOU WON!")
        elif choice2 == "blue":
            print("You entered a room of thieves,YOU LOST ")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by shark. Game Over.")
else:
    print("You fell in to a hole." ' GAME IS OVER ')