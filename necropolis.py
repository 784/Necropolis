#Imports the time function so I can add time between messages
import time

#Imports the random integer function
import random


#Sets the score to 0
Score = 0

#Asks if you want to do a tutorial
tutorial = input("Do you want to do the tutorial? Type Y for yes and N for no: ")

if tutorial == "Y":
    print("""  
                .--.
                |__| .-------.
                |=.| |.-----.|
                |--| || TUT ||
                |  | |'-----'|
                |__|~')_____('"""  "\n"); print("Welcome to my game! For my final project, I chose to make a text based game where you explore a world called Necropolis. It's a choose your own adventure game! \n")
    
    #Wait 3 seconds
    time.sleep(3)

else:
    print("\nA fast learner I see!\n")
    time.sleep(1)



#Choosing a username
username = input("Would you like to choose a username? Type Y for yes and N for no. If one isn't chosen, Lazarus will be chosen for you: ")

#Make it uppercase
username.upper()

if username == "Y":
    username1 = input("What username would you like to choose? ")

else:
    username1 = "Lazarus"

#Wait 1 second
time.sleep(1)


#Introduction
print("\n" "Welcome" , username1 , "to the Necropolis, a land of treachery and deceit. You must constantly be aware of your surroundings, or you may end up with a terrible fate.")

time.sleep(3)

print("Good luck, and have fun! \n")

print("*There's two paths up ahead. A cave and a road. Which will you choose?* ")

caveornot = input("Choose C for cave and R for road: ")

#Make it uppercase
caveornot.upper()

cave = False
road = False

if caveornot == "C":
    print("\n" , username1 , "has entered the gloomy cave \n")
    cave = True
    time.sleep(2)

else:
    print(username1 , "has chosen to take the long road...")
    road = True
    time.sleep(2)


if cave == True:
    print("Welcome to the cave! It's the gloomiest, scariest place you'll ever visit in the Necropolis... good luck. \n")

if road == True:
    print("Welcome to the road! You've chosen the longer path, like many before. \n ")

#Choosing to go on the road
if road == True:
    leftandright = input("Would you like to go left or right? Type L for left and R for right: ")
    leftandright.upper()
    if leftandright == "L":
        time.sleep(2)
        print("*YOU FALL DOWN AN INFINITY HOLE* You should've looked down before you stepped. You lost...")
        print("""     
                        ███████▄▄███████████▄
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓███░░░░░░░░░░░░█
                        ██████▀░░█░░░░██████▀
                        ░░░░░░░░░█░░░░█
                        ░░░░░░░░░░█░░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░░▀▀   """)
        road = False
    
    if leftandright == "R":
        time.sleep(2)
        print("\nYou chose the right path (get it)! Here's 25 points for getting it correct.")
        Score = Score + 25
        print ("Your current score is" , Score ,"\n")

        time.sleep(2)

        print("*You see a magical forest up ahead*")

        time.sleep(3)
        
        print("*You think about what life could be like if you quit adventuring and finally settled down...*")

        time.sleep(2)

        quitadventure = input("Do I want to quit adventuring and settle down? Type Y for yes and N for no: ")
        
        #Making it uppercase
        quitadventure.upper()

        if quitadventure == "Y":
            print("I'm sure there's plenty of firewood out here to keep me warm for the night.")
            time.sleep(1)
            print("*You gather firewood and make a fire. You fall asleep next to its flames.*")
            time.sleep(2)
            print("\n THE END \n")

        if quitadventure == "N":
                print("*You decide to walk back down the path towards the cave*")
                time.sleep(3)
                print("*You enter the cave*")

                road = False
                cave = True



#Choosing to enter the cave
if cave ==  True:
    leftorright = input("Would you like to go left or right? Type L for left and R for right: " )

    #Makes it uppercase
    leftorright.upper()

    #If you go right immediately, you have to fight the boss early.
    if leftorright == "R":
        print("\nI think I just stepped in something...")
        time.sleep(1)
        print("I better keep moving... there's lots of creepy crawlies down here.")

        time.sleep(3)

        print("\nRAWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\n")
        time.sleep(3)   
        print("OH NO!!! I WASN't SUPPOSED TO SEE THIS YET")
        time.sleep(2)
        print("*Wow, he's gigantic.*")
        time.sleep(2)
        print("\n" , username1.upper() , "VS BOSS \n")

        #Setting the boss health to 250
        bosshealth = 250

        #Setting the player health to 100
        playerhealth = 100

        #Boss fight
        while bosshealth > 0:
            time.sleep(1)
            print("The boss has" , bosshealth , "health")

            #Chooses a random integer between 1 and 10 
            randomnum = random.randint(1,10)

            #If the number is more than 3, you get to attack
            if randomnum > 3: 

                    #Asks if you want to fight the boss
                    usefists = input("Do you want to use your fists to attack the boss? Type Y for yes and N for no: ")
                    
                    #Makes it uppercase
                    usefists.upper()

                    if usefists == "Y":
                        bosshealth = bosshealth - 5

                    if usefists == "N":
                        print("Oh no! The boss has hit you. Your score has decreased by 25")
                        Score = Score - 25
                        time.sleep(1)
                        print("Your current score is" , Score)

            #If the number is less than 3, you lose 10 health
            if randomnum < 3:
                playerhealth = playerhealth - 20
                Score = Score - 10
                print("You have" , playerhealth , "health left.")
                print("Your current score is" , Score)

            if playerhealth < 0:
                print("You've lost.")
                print("""     
                        ███████▄▄███████████▄
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓███░░░░░░░░░░░░█
                        ██████▀░░█░░░░██████▀
                        ░░░░░░░░░█░░░░█
                        ░░░░░░░░░░█░░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░░▀▀   """)
            
            cave = False



    
    #If you go left, you can find a sword and fight a slime
    if leftorright == "L":
        time.sleep(2)
        print("\n*You see a shiny object*") 
        
        shiny = input("Do you want to pick it up? Type Y for yes and N for no: ")
        
        #Makes it uppercase
        shiny.upper()
        
        #Find the sword
        if shiny == "Y":
            print("You found a sword! It could be useful if you find any nasty enemies down there.")
            has_sword = True

            time.sleep(3)
            slimehealth = 75
            print ("Perfect timing! There's a slime up ahead.")
            
            time.sleep(1)
            print("\n" , username1.upper(), "VS SLIME" "\n")
            
            #Slime battle
            while slimehealth > 0:
                time.sleep(1)
                print("The slime has" , slimehealth , "health")
                usesword = input("Do you want to use your sword to attack the slime? Type Y for yes and N for no: ")

                if usesword == "Y":
                    slimehealth = slimehealth - 25

                if usesword == "N":
                    print("Oh no! The slime has hit you. Your score has decreased by 10")
                    Score = Score - 10
                    time.sleep(1)
                    print("Your current score is" , Score)

            #After slime fight
            time.sleep(1)
            print("\n Wow, that was quick. That must be one powerful sword.")
            

        #If you choose not to pickup the sword, the game becomes much harder at the boss fight
        if shiny == "N":
            has_sword = False
            print("Oh well, it was probably a trap anyways.")

        
    #Boss battle is getting ready to begin   
    time.sleep(2)
    print("\nI see a large cave opening up there. Hmmm, I wonder what could be in there.")  
    time.sleep(5)
        
        
        
        
        
    #If you chose to pick up the sword earlier, you'll do more damage    
    if has_sword == True:
        print("\nRAWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\n")
        time.sleep(3)    
        print("*Wow, he's gigantic.*")
        time.sleep(2)
        print("\n" , username1.upper() , "VS BOSS \n")

        #Setting the boss health to 250
        bosshealth = 250

        #Setting the player health to 100
        playerhealth = 100

        #Actual boss fight
        while bosshealth > 0:
            time.sleep(1)
            print("The boss has" , bosshealth , "health")

            #Chooses a random integer    
            randomnum = random.randint(1,10)

            #If the number is more than 3, you get to attack
            if randomnum > 3: 

                usesword = input("Do you want to use your sword to attack the boss? Type Y for yes and N for no: ")

                if usesword == "Y":
                    bosshealth = bosshealth - 25
                

                if usesword == "N":
                    print("Oh no! The boss has hit you. Your score has decreased by 25")
                    Score = Score - 25
                    time.sleep(1)
                    print("Your current score is" , Score)

            #If the number is less than 3, you lose 10 health       
            if randomnum < 3:
                playerhealth = playerhealth - 10
                Score = Score - 10
                print("You have" , playerhealth , "health left.")
                print("Your current score is" , Score)
        
            #If your health reaches 0, you lose
            if playerhealth < 0:
                print("You've lost.")
                print("""     
                        ███████▄▄███████████▄
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓███░░░░░░░░░░░░█
                        ██████▀░░█░░░░██████▀
                        ░░░░░░░░░█░░░░█
                        ░░░░░░░░░░█░░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░░▀▀   """)
            
            cave = False

            #If the bosses health is equal to 0, you win!
            if bosshealth == 0:
                print("Woah! That was easier than I thought.")
                Score = Score + 100
                time.sleep(1)
                print("Congrats on winning the game and traversing through the Necropolis alive. I hope you enjoyed!")    

                time.sleep(1)
                print("Your total score was" , Score)



    #If you chose not to pick up the sword, your life is going to be a lot more difficult
    if has_sword == False:
        print("\nRAWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\n")
        time.sleep(3)   
        print("*Wow, he's gigantic.*")
        time.sleep(2)
        print("\n" , username1.upper() , "VS BOSS \n")

        #Setting the boss health to 250
        bosshealth = 250

        #Setting the player health to 100
        playerhealth = 100

        #Boss fight
        while bosshealth > 0:
            time.sleep(1)
            print("The boss has" , bosshealth , "health")

            #Chooses a random integer between 1 and 10 
            randomnum = random.randint(1,10)

            #If the number is more than 3, you get to attack
            if randomnum > 3: 

                    usefists = input("Do you want to use your fists to attack the boss? Type Y for yes and N for no: ")

                    if usefists == "Y":
                        bosshealth = bosshealth - 10

                    if usefists == "N":
                        print("Oh no! The boss has hit you. Your score has decreased by 25")
                        Score = Score - 25
                        time.sleep(1)
                        print("Your current score is" , Score)

            #If the number is less than 3, you lose 10 health
            if randomnum < 3:
                playerhealth = playerhealth - 10
                Score = Score - 10
                print("You have" , playerhealth , "health left.")
                print("Your current score is" , Score)

            if playerhealth < 0:
                print("You've lost.")
                print("""     
                        ███████▄▄███████████▄
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                        ▓▓▓▓▓▓███░░░░░░░░░░░░█
                        ██████▀░░█░░░░██████▀
                        ░░░░░░░░░█░░░░█
                        ░░░░░░░░░░█░░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░█░░█
                        ░░░░░░░░░░░░▀▀   """)
            
            cave = False

            
            
            #If the bosses health is equal to 0, you win!
            if bosshealth == 0:
                print("Woah! That was easier than I thought.")
                
                Score = Score + 100
                
                time.sleep(1)
                print("Congrats on winning the game and traversing through the Necropolis alive. I hope you enjoyed!")   

                time.sleep(1)
                print("Your total score was" , Score)


            #If you get a perfect score, you get this message
            if Score == 125:
                print("Wow! You had a perfect score :D")
 


          






    










