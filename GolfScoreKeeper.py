# The first program will input each player's first name, last name, handicap and golf score  
# and then save these records in a file named golf.txt (each record will have a field for the 
# first name, last name, handicap and golf score).

# -------------------------------------------------------------------------------------------------------------------------------------------------#
# Author: JM Cameron
# Date: November 2020

# Importing the csv package to use the csv.writer function.
import csv


# This is the main function of the program.
def main():
    # This line prints a formatted header row for the program.
    print('\n', '-' * 20, "Country Club Tournament Scores", '-' * 20, '\n')

    # This is a repeating while loop to accept as many names as the user would like enter. 
    # This will accommodate all players in the tournament (and more).
    repeat = "yes"
    while repeat == "yes":

        # The next steps asks the user to input the player data.
        first_name = input("\nPlease enter the player's first name: ")
        last_name = input("\nPlease enter the player's last name: ")
        handicap_number = input("\nPlease enter the player's handicap: ")

        # This step handles an error is the golf score entered raises an exception.
        try:
            golf_score = int(input("\nPlease enter the player's golf score: "))
        except:
            golf_score = "-NOT VALID-"

        # This step determines if the player made par for the course.
        result_text = determine_result(golf_score)
        print("\nFor this tournament, " + first_name + " " + last_name + "'s final result was: " + result_text)

        # These steps create the golf.txt file when the program is first run.
        # and appends the player data to the file. 
        # csv writer function is used so the file data can be delimited with a comma.
        with open('golf.txt', 'a', encoding='ascii', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([first_name, last_name, handicap_number, golf_score, result_text])

            # This repeater variable allows the user to run the program for more user input or terminate the program.
        repeat = input("\nPlease enter 'yes' if you would like to continue to the next player: ")

    # This line prints a formatted footer row for the program.
    print('\n', '-' * 36, "Goodbye", '-' * 36, '\n')


# This function determines the player's par result.
def determine_result(a):
    if type(a) != int:
        Par_result = "-NOT VALID-"
    elif a == 80:
        Par_result = "Made Par"
    elif a < 80:
        Par_result = "Under Par"
    elif a > 80:
        Par_result = "Over Par"
    else:
        Par_result = "-NOT VALID-"
    return Par_result


# The main function is called and all of the above code is run.
main()

# Author: JM Cameron
# Date: November 2020
# -------------------------------------------------------------------------------------------------------------------------------------------------#
