import random
import art

win_image = art.text2art("You Win!")
lose_image = art.text2art("You're a witch!")


welcome_text = """
The year is 1692 and in colonial Massachusetts and in a town called
Salem a mass hysteria has taken the people of the town, and the people of Salem
are accussing women of being witches left and right, resulting in hangings and 
burnings at the stake. The women of Salem walk on eggshells trying to advoid being accused. 
Now you must do the same, you must avoid being accused of being a witch, except, you are a witch,
and you and your coven must advoid being caught.
"""
banner = art.text2art("Salem Witch Trails")

MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

totalMilesTraveled = 0 
suspicion = 0
day = 1
month = 1 
year = 1692
gameStatus= ' '
userCommand = ' '

coven_member = []
player1 = ""
coven1 = ''
coven2 = ''
coven3 = ''
coven4 = ''

characters = ["Tiffany, the Apothecary", "Mia, the Tailor", "Owen, the Printer"]

character_dialogues = {
    "Tiffany, the Apothecary": [
        f"Tiffany walks towards you, she reeks of herbs and medicene, and around suspiciously. 'Did you hear the rumors {player1}? There are witches everywhere now. People are whispering... I don't feel safe.'",
        f"'I can't help but feel like someone will accuse me next. I wonder if I should leave town before it's too late. You should too, {player1}.'"
    ],
    "Mia, the Tailor": [
        f"Mia eyes her surroundings, her voice hushed. 'It's getting worse, isn't it {player1}? Everyones pointing fingers at everyone. I fear it's just a matter of time before they come for me.'",
        "'I overheard some villagers talking about strange happenings. It makes my skin crawl. These witch hunts are spiraling out of control!'"
    ],
    "Owen, the Printer": [
        "Owen quitely whispers to you in a moment of fear. 'The witch hysteria is growing. I see people pointing fingers at their neighbors. Who's next?'",
        f"'I don't know how much longer I can stay here {player1}. The tensions are high. It's like everyone's too afraid to even speak openly anymore.'"
    ]
}

def print_no_valid_command():

    print("the command you have entered is not recognized, please enter a new command. ")
    print("what would you like to do? (Socialize / rest / chores / help / quit): ")

totalDaysPassed = 0 
no_chores_counter = 0

def add_day():
    global suspicion, day, month, year, totalDaysPassed

    totalDaysPassed += 1  
    day += 1

    days_in_month = 31
    if month in MONTHS_WITH_31_DAYS:
        days_in_month = 31
    elif month in MONTHS_WITH_30_DAYS:
        days_in_month = 30
    elif month in MONTHS_WITH_28_DAYS:
        days_in_month = 28

    if day > days_in_month:
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1
        if year == 1693:
            print("The year is now 1693. You have survived the Salem Witch Trials!")
            handle_win()

    print(f"Days have passed: {totalDaysPassed}. Current Date: {month}/{day}/{year}. Suspicion level: {suspicion}")

    if day == 14 or day == 18:
        suspicion += 1
    print(f"Days have passed: {totalDaysPassed}. Current Date: {month}/{day}/{year}. Suspicion level: {suspicion}")

    if (month == 7 and day == 19 and year == 1692) or \
       (month == 8 and day == 19 and year == 1692) or \
       (month == 9 and day == 22 and year == 1692):
        random_kill_coven_member()


    if day == 14 or day == 18:
        suspicion += 1 
    print(f"Days have passed: {totalDaysPassed}. Current Date: {month}/{day}/{year}. Suspicion level: {suspicion}")

    if (month == 7 and day == 19 and year == 1692) or \
       (month == 8 and day == 19 and year == 1692) or \
       (month == 9 and day == 22 and year == 1692):
        random_kill_coven_member()

def random_kill_coven_member():
    if len(coven_member)>0:
        killed_member = random.choice(coven_member)
        coven_member.remove(killed_member)
        print(f"On {month}/{day}/{year}, the town has discovered one of your coven members is a witch!")
        print(f"Tragically, {killed_member} has been executed!")
        print("Your coven is now down by one member!")
    else:
        print("Your coven has already lost all its members.")
        handle_loss()

def handle_socialize():
    global suspicion
    chosen_character = random.choice(characters)
    print(f"\nYou approach {chosen_character} to chat about the strange events happening around town...")

    dialogue = random.choice(character_dialogues[chosen_character])
    print(f"{chosen_character}: {dialogue}")
    suspicion += 1
    add_day()



def handle_rest():
    global suspicion
    if suspicion < 3:
        print("you've chosen rest to avoid gaining more suspicion.")
        suspicion = 0  
        randomDaysResting = random.randint(1, 3)
        add_day()


        print(f"You rested for {randomDaysResting} days and your suspicion level is now {suspicion}.")
    else:
        print("your suspicion level is too high.")


def handle_chores():
    global suspicion
    print("\nYou have decided to do some chores. Choose one of the following tasks:")
    print("1. Sweep the floor")
    print("2. Tend to the garden")
    print("3. Prepare the food")
    print("4. Do the wash")

    chore_pick = input("Which do you pick? (enter a number, please)")

    if chore_pick == "1":
        print("You sweep the floor and clean around the house.")
        suspicion = 0  
        add_day()

    elif chore_pick == "2":
        print("You tend to the garden, smell the flowers, and collect some herbs.")
        suspicion = 0  

    elif chore_pick == "3":
        print("You spend the day preparing food for the coven.")
        suspicion = 0  
        add_day()

    elif chore_pick == "4":
        print("You spend the day doing the wash, cleaning your clothes.")
        suspicion = 0 
        add_day()

    else:
        print("Invalid choice. Please choose a valid task.")
        handle_chores()
 

def handle_turn(choice):
    global no_chores_counter
    if choice == "chores":
        no_chores_counter = 0  
        handle_chores()  
    else:
        no_chores_counter += 1  
        if no_chores_counter == 3:
            print("You have been accused of being a witch and killed!")
            handle_loss()  

def handle_help():
    print("Reinder, accepted commands are: (travel / rest / hunt / status / help / quit): ")


def check_status():
    global month, day, totalMilesTraveled, suspicion, year

    print(f"Current date: {month}/{day}/{year}")
    print(f"Suspicion: {suspicion}")
    print(f"Today: {totalDaysPassed} days have passed since the start of the year.")
    
    days_in_1962 = 365 * 1
    days_left = days_in_1962 - totalDaysPassed

    print(f"Total days remaining until 1963: {days_left}")
    
    if suspicion >= 3:
        print("You've reached max suspicion and town has declared you a witch!")
        handle_loss()



def handle_loss():

    print(lose_image)
    print("Game Over!")
    handle_quit()

def handle_win():
    print(win_image)
    print("Congradulations! you survived!")

def handle_quit():
    global gameStatus
    print("Game Over!")
    gameStatus + "game over"

def handle_quit():
    global gameStatus
    print("You have quit the game.")
    gameStatus = 'game over'


print(banner)
input("Press Enter to play!")
print(welcome_text)
print()
player1= input("What is your name, witch?:")
print(f"welcome {player1}!")
print("and what is the name of the memebers of your coven?")
coven1= input("name of Coven Member 1:")
coven2 = input("name of Coven Member 2:")
coven3 = input("name of Coven Member 3:")
coven4 = input("name of Coven Member 4:")

print(f"Welcome {player1} and coven memebers, {coven1}, {coven2}, {coven3}, and {coven4} the goal of the game is to make it through the year without being caught and killed.")

while gameStatus != 'game over' and userCommand != 'quit':

    check_status()

    userCommand = input("what would you like to do? (Socialize / rest / chores / help / quit): ")

    if userCommand == "socialize":
        handle_socialize()

    elif userCommand == 'rest':
        handle_rest()
    
    elif userCommand == 'chores':
        handle_turn("chores")

    elif userCommand == 'status':
        check_status()

    elif userCommand == 'help':
        handle_help()
    
    elif userCommand == 'quit':
        handle_quit()

    else:
        print_no_valid_command()

   