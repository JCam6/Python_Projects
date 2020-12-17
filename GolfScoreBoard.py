# The second program will read the records from the golf.txt file 
# and display them with appropriate headings above the data being displayed.

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
# Author: JM Cameron
# Date: November 2020

# Importing the csv package to use the csv.reader function.
import csv

# This is the main function of the program.
def main():
    # This is a repeating while loop to display the scores as many times as the user would like.
    repeat = "yes"
    while repeat == "yes":

        # This step is an Exception handler if the golf.txt file does not exist.
        try:

            # This step opens and reads the records from golf.txt.
            with open('golf.txt','r', encoding='ascii', newline='\n') as f:
                
                # This line prints a formatted header row for the program.
                print('\n','-'*20,"Country Club Tournament Results",'-'*20,'\n')            
                
                # This step prints headings for the data being displayed.
                header = ["First Name","Last Name","Handicap","Score","Result"]
                for column in header:
                    print(fixed_length(column,18), end= "")
                print()
            
                # This step formats the data from golf.txt to display in a table according to the headings above.
                reader = csv.reader(f)
                data = []
                for row in reader:
                    data.append(row)
                for row in data:
                    for column in row:
                        print(fixed_length(column,18), end= "")
                    print()
        
        # This step closes the exception handler.
        except:
            print("\nThe tournament data has not been entered yet. Please run that program first!")
            break

        # This repeater variable allows the user to run the program again or terminate.
        repeat = input("\nPlease enter 'yes' if you would like to display the tournament results again: ")

    # This line prints a formatted footer row for the program.
    print('\n','-'*36,"Goodbye",'-'*36,'\n')

# Create function to determine length to print each field.
def fixed_length(text,length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " * length)[:length]
    return text

# The main function is called and all of the above code is run.
main()

# Author: JM Cameron
# Date: November 2020
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
