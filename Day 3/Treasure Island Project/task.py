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

choice_1 = input("You,re at a crossroad,"
                 "Which way would you like to go?:\n    Type L to go left or R to go Right: ").lower()
if choice_1 == "l":
    choice_2 = input("You've reached a Lake with an island in the middle of it, "
                     "Do you want to Swim across or Wait for a boat?\n"
                     "Type S to Swim or W to Wait: ").lower()
    if choice_2 == "w":
        choice_3 = input("You've reached a cabin with 3 doors, One red, the other yellow and the last one blue\n"
                         "Which Door do you want to Follow?\n    "
                         "Type R to follow the Red door, B for the Blue door, Y for the Yellow door: ").lower()
        if choice_3 == "r".lower():
            print("It's a room full of fire, Game Over")
        elif choice_3 == "y".lower():
            print("You Found the Treasure\n You Win!")
        elif choice_3 == "b".lower():
            print("You We're Captured by Pirates\n Game Over")
        else:
            print("You chose a door that doesn't exist. Game Over")
    else:
            print("Attacked by Crocodiles, Game Over :(")

else:
    print("Attacked by Monsters, Game Over :(")
