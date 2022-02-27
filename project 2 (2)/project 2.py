from multiprocessing.sharedctypes import Value
import random
import time

#_____Init Flags_____
Cave_visit_Flag = False 
Dagger_Flag = False
user_input = 0  
isValidInput = False
gamePlay = True 


def delay():
    time.sleep(2)
    return 

def random_narritive():
    StringSubject  = ['wicked fairie', 'pirate', 'gorgon','dr']    
    return random.choice(StringSubject)

#input validation 
#recall that input method retruns a string 
def choice_validation(isValid):
    userinput = input('(Please enter 1 or 2.)\n')

    while not isValid:

        if((len(userinput) == 1  and int(userinput) == 2) or (len(userinput) == 1  and int(userinput) == 1)):
            isValid = True
            print("getting here")
            #cast  user_int to int so we can make some choices 
            user_input = int(userinput)
        else:
            userinput = input('(Please enter 1 or 2.)\n')
    isValid = False
    return user_input

1
def playAgain_validation(isValid):

    userinput = input('Would you like to play again? (y/n)')

    while not isValid:
        if((len(userinput) == 1  and userinput == 'y') or (len(userinput) == 1  and userinput == 'n')):
            isValid = True
            print("getting here")
        else:
            userinput = input('Would you like to play again? (y/n)')
    isValid = False
    return userinput


#set up random narritve to be used throught the rest of the game 
narritive = random_narritive()


print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
delay()
print("Rumor has it that a {} is somewhere around here, and has been terrifying the nearby village.\n".format(narritive))
delay()
print("In front of you is a house.")
delay()
print("To your right is a dark cave.")
delay()
print("In your hand you hold your trusty (but not very effective) dagger.\n")
delay()
print("Enter 1 to knock on the door of the house.")
delay()
print("Enter 2 to peer into the cave.")
delay()
print("What would you like to do?")



while gamePlay: 

    choice = choice_validation(isValidInput)
    print(choice)

    if choice  == 1:
                print("You approach the door of the house.")
                delay()
                print("You are about to knock when the door opens and out steps a {}.".format(narritive))
                delay()
                print("Eep! This is the {}'s house!".format(narritive))
                print("The {} attacks you!".format(narritive))
                if Dagger_Flag == False:
                    print("You feel a bit under-prepared for this, what with only having a tiny dagger")
                    delay()
                    print("Would you like to (1) fight or (2) run away?")
                    choice = choice_validation(isValidInput)
                    if choice == 1:
                        print("You do your best...")
                        delay()
                        print("but your dagger is no match for the dragon.")
                        delay()
                        print("You have been defeated!")
                        delay()
                        choice = playAgain_validation(isValidInput) 
                        if choice =='y':
                            print("Excellent! Restarting the game ...")
                            break
                        if choice =='n':
                            exit        

                

                

    if choice== 2 and Cave_visit_Flag == False:
                print("You peer cautiously into the cave.")
                delay()
                print("It turns out to be only a very small cave.")
                delay()
                print("Your eye catches a glint of metal behind a rock.")
                delay()  
                print("You discard your silly old dagger and take the sword with you.")
                delay()
                print("You have found the magical Sword of Ogoroth!")
                delay()
                print("You walk back out to the field.")
                #set visti flag to true 
                Cave_visit_Flag = True
                Dagger_Flag = True

    if choice == 2 and Cave_visit_Flag == True :
                print("You peer cautiously into the cave.")
                delay()
                print("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
                delay()
                print("You walk back out to the field.")
                
            








