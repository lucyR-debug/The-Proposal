import random
import art


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

MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7
TOTAl_MILES = 2000

MAX_HEALTH_LEVEL = 5
MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5



food = 500
totalMilesTraveled = 0 
health = 5
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



def add_day():
    global food
    food -= 5

    global health
    global day 
    global month
    global year

    if day == 14 or day == 18:
        health -= 1

    day +=1

    if month in MONTHS_WITH_28_DAYS and day >28:

        day = 1
        month += 1

    elif month in MONTHS_WITH_30_DAYS and day > 30:

        day = 1
        month += 1

    elif month in MONTHS_WITH_31_DAYS and day > 31:
        day = 1
        month +=1 

    if month > 12:

        month = 1
        day = 1
        year += 1

        if year == 1693:
            print("The year is now 1693. You have survived the Salem Witch Trails!")
            handle_loss()

        if (month == 7 and day == 19 and year == 1962) or \
           (month == 8 and day == 19 and year == 1962) or \
           (month == 9 and day == 22 and year == 1962):
            random_kill_coven_member()
            handle_loss()

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
    chosen_character = random.choice(characters)
    print(f"\nYou approach {chosen_character} to chat about the strange events happening around town...")

    dialogue = random.choice(character_dialogues[chosen_character])
    print(f"{chosen_character}: {dialogue}")
    add_day()



def handle_rest():
    global health 
    if health < MAX_HEALTH_LEVEL:
        health += 1
        randomDaysResting = random.randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST)

        for _ in range(randomDaysResting):
            add_day()

        print("You rested for" +str(randomDaysResting) + "and your health is" + str(health))

    else:

        print ("You are fully healthed and you do not need to rest. ")


def handle_chores():
    global food 

    food += FOOD_PER_HUNT

    randomDaysHunting = random.randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT)

    for _ in range(randomDaysHunting):
            add_day()

    print("You take" + str(randomDaysHunting)+ "days tp collect 100 pounds of food.")

def handle_help():
    print("Reinder, accepted commands are: (travel / rest / hunt / status / help / quit): ")


def check_status():
    global month, day, totalMilesTraveled, health, food, year

    print(f"Current date: {month}/{day}/{year}")
    print(f"Health: {health}")
    print(f"Food: {food} pounds")
    print(f"Total miles traveled: {totalMilesTraveled}")
    print(f"Remaining miles: {TOTAl_MILES - totalMilesTraveled}")

    if health <= 0 or food <= 0:
        print("You have run out of health or food. Game over!")
        handle_loss()



def handle_loss():

    check_status()
    handle_quit()

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
print("and what is the name of the memembers of your coven?")
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
        handle_chores()

    elif userCommand == 'status':
        check_status()

    elif userCommand == 'help':
        handle_help()
    
    elif userCommand == 'quit':
        handle_quit()

    else:
        print_no_valid_command()