print('''
********************************************************************
                888              
                888              
                888              
 .d8888b 8888b. 888  888 .d88b.  
d88P"       "88b888 .88Pd8P  Y8b 
888     .d888888888888K 88888888 
Y88b.   888  888888 "88bY8b.     
 "Y8888P"Y888888888  888 "Y8888 
                                ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
********************************************************************
''')

print("Welcome to Cake hunt Castle.")
print("When you get into the castle, BE SURE to say HI to the lady in red on category 2.")
while(True):
    print()
    print("Are you ready to start?")
    action = input("Press Yes or No? ")
    if action == 'Yes':
        choice1 = input('Be careful not to fall into a hole, what floor would you like to go to "first", "second", "third"? ')
        if choice1 == 'second':
            choice2 = input("welcome to the second floor. There are three rooms on this floor, 'room1', 'room2', 'room3. which of the room would you like to go into? \n")
            if choice2 == 'room3':
                choice3 = input('What type of cake are you looking for?, Type "Vanilla", "Chocolate", "Red velvet" \n')
                if choice3 == 'Red velvet':
                    print("You just found the treasure cake, enjoy yourself a yummy treat! 🎂")
                break
            elif choice2 == 'room1' or choice2 == 'room2':
                print("A room full of fire🔥. Game over😟")
            break
        else:
            print("you flipped 😓 and fell into a hole 🕳, please try again!")
        break
    elif action == 'No':
        choice4 = input("Do you want to quit? 'Yes' or 'No' \n")
        if choice4 == 'Yes':
            break
        else:
            print("Its an interesting hunt and I trust you'd love it, continue.....")
