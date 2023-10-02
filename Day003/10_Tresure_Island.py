print("Welcome to Treasure Island")
print("Your mission is to find the treasure ")
choice1 = input('You\'re at a crossroad, where do you want to go? Type \"left" or \"right"\n').lower()

if choice1 == "left":
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrived the island unharmed...Yay -.-\" ... There is a house with 3 doors. One is red, one is yellow and one is pink. Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("Are you really that dumb? It is a red door... That means you should not open it! A wave of bloody Vampires come at you and eat you alive... Game Over!")
        elif choice3 == "yellow":
            print("What did you think, you will find here? You opened the door and burned down in nicely yellowish fire! Wow.... Game Over!")
        else:
            print('''Nice... You have found the fuggin treasure... Are you proud now?\nLook inside and have fun with your brand new Princess Lillifee crown!\nYou won this shitty game! congrats...\n
             __       __          .--.
(  ""--__(  ""-_    ,' .-.\        *
 "-_ __  ""--__ "-_(  (^_^))      /
    (  """--___""--__" )-'(      /
     "-__      ""---/ ,(., )__o-/,  
         """----___(.'.   /--"--'
                   ("-_"/(    /
                    \   \ \ 
                     `.  \ |
                       \  \/
                       ||  \ 
                     ,-'/`. \ 
                     ) /   ) \ 
                     |/    `-.\ 
                              `\ ''')
    else:
        print("What kind of an idiot are you dumb ass? It is a big lake... There are hungry sharks in it! You just got eaten by one of them! Game Over!")
else:
    print("You are fucked! The is a wall and you ran into it so hard... Noob! Game Over!")
