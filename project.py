import random



welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

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
month = 3 
year = 0 
gameStatus= ' '
userCommand = ' '


def print_no_valid_command():

    print("the command you have entered is not recognized, please enter a new command. ")
    print("what would you like to do? (travel / rest / hunt / help / quit)")



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

    if day >= 25 and month in MONTHS_WITH_28_DAYS:

        day = 1
        month += 1

    elif day >= 25 and month in MONTHS_WITH_30_DAYS:

        day = 1
        month += 1

    elif day >= 31 and month in MONTHS_WITH_31_DAYS:
        day = 1
        month +=1 

    if month > 12:

        month = 1
        day = 1
        year = 1


def handle_travel():
    global totalMilesTraveled
    randomMilesTraveled = random.randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)
    totalMilesTraveled += randomMilesTraveled
    milesRemaining = TOTAl_MILES - totalMilesTraveled

    print("you traveled" +str(randomMilesTraveled) + "for a total of" + str(totalMilesTraveled) + "total miles traveled!")
    print("You have" + str(milesRemaining) + "miles left to go until Oregon.")
    randomDaysTraveled = random.randint(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)
    for day in range(randomDaysTraveled):
        add_day()


def handle_rest():
    global health 
    if health < MAX_HEALTH_LEVEL:
        health += 1
        randomDaysResting = random.randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST)

        for day in range(randomDaysResting):
            add_day()

        print("You rested for" +str(randomDaysResting) + "and your health is" + str(health))

    else:

        print ("You are fully healthed and you do not need to rest. ")


def handle_hunt():
    global food 

    food += 100

    randomDaysHunting = random.randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT)

    for day in range(randomDaysHunting):
            add_day()

    print("You take" + str(randomDaysHunting)+ "days tp collect 100 pounds of food.")

def handle_help():
    print("Reinder, accepted commands are: (travel / rest / hunt / status / help / quit)")


def check_status():
    global month
    global day
    global totalMilesTraveled
    global health
    global food
    print( "and your health is" + str(health))
    print("you have" +str(food)+"total pounds of food")
    milesRemaining = TOTAl_MILES - totalMilesTraveled
    print("you traveled a total of" + str(totalMilesTraveled) + "total miles traveled!")
    print("You have" + str(milesRemaining) + "miles left to go until Oregon.")

    
def check_status():
    global year
    global food
    global health

    if year >= 1:
        handle_loss()

    if food >= 1:
        handle_loss()

def handle_loss():
    
    check_status()
    handle_quit()

def handle_quit():
    global gameStatus
    gameStatus + "game over"


print(welcome_text)
print()


while gameStatus != 'game over' and userCommand != 'quit':

    check_status()

    userCommand = input("what would you like to do? (travel / rest / hunt / help / quit)")

    if userCommand == "travel":
        handle_travel()

    elif userCommand == 'rest':
        handle_rest()
    
    elif userCommand == 'hunt':
        handle_hunt()

    elif userCommand == 'status':
        check_status()

    elif userCommand == 'help':
        handle_help()
    
    elif userCommand == 'quit':
        handle_quit()

    else:
        print_not_valid_command()