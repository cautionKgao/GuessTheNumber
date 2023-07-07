import random
from click import echo

game_level = ['1', '2', '3']
game_level[0] = 'Easy'
game_level[1] = 'Medium'
game_level[2] = 'Hard'


#number = random.randint(0,10)
count = 5 # Number of attempts given

level_pick = input("Choose your level between Easy, Medium, and Hard: ")
#code for level easy
if level_pick == str(game_level[0]):
    selected_num = random.randint(0,10) # Pick a random number and store it
    while count > 0: 
        num_picked = input("Pick a number between 0 and 10: ") # Prompts the user to enter a number betwwen the given range
        count -= 1
        if num_picked == str(selected_num):
            print("Wow, It took you",  5 - count , "tries to get the number", num_picked )
            break
        else: # Give the user a hint
            print("Oops try again, you got", count, "tries left!!")
            if selected_num < 5:
                echo("Hint: The number is less than 5")
            elif selected_num >= 5:
                echo("The number is greater then 5")
    if count == 0:
        print("Out of attempts! The correct number was", selected_num)
#code for level medium
elif level_pick == str(game_level[1]):
    selected_num = random.randint(0,100) # Pick a random number and store it
    while count > 0: 
        num_picked = input("Pick a number between 0 and 100: ") # Prompts the user to enter a number betwwen the given range
        count -= 1
        if num_picked == str(selected_num):
            print("Wow, It took you",  5 - count , "tries to get the number", num_picked )
            break
        else: # Give the user a hint
            print("Oops try again, you got", count, "tries left!!")
            if selected_num < 50:
                echo("Hint: The number is less than 50")
            elif selected_num >= 50:
                echo("The number is greater then 50")
    if count == 0:
        print("Out of attempts! The correct number was", selected_num)
#code for level hard
else:
    if level_pick == str(game_level[2]):  
        selected_num = random.randint(0,1000) # Pick a random number and store it
        while count > 0: 
            num_picked = input("Pick a number between 0 and 1000: ") # Prompts the user to enter a number betwwen the given range
            count -= 1
            if num_picked == str(selected_num):
                print("Wow, It took you",  5 - count , "tries to get the number", num_picked )
                break
            else: # Give the user a hint
                print("Oops try again, you got", count, "tries left!!")
                if selected_num < 500:
                    echo("Hint: The number is less than 500")
                elif selected_num >= 500:
                    echo("The number is greater then 500 ")
    if count == 0:
        print("Out of attempts! The correct number was", selected_num)

    


