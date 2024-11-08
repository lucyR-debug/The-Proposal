
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

day = 1
month = 3 
year = 0 
gameStatus= ' '
userCommand = ' '


def print_no_valid_command():

    print("the command you have entered is not recognized, please enter a new command. ")
    print("what would you like to do? (travel / rest / hunt / help / quit)")



def add_day():

    global day 
    global month
    global year

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
        handle_status()

    elif userCommand == 'help':
        handle_help()
    
    elif userCommand == 'quit':
        handle_quit()

    else:
        print_not_valid_command()