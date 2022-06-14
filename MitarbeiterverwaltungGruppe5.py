import pandas as pd

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
pd.options.display.width = 0
url = 'https://raw.githubusercontent.com/swenrengers/MitarbeiterverwaltungGruppe5/main/export.csv'
df = pd.read_csv(url, sep=';', index_col=0)

selection = 0       # A variable is added for inputs from the user, to go through while loops.
while selection != 6:       # As long as the variable is not 6, the while loop will be running.
        print("Welcome to the Employee Management Program (EMP)\n"      # The menu will be printed.
              "==================================================\n"
                  "\n"
                  "Please choose one of the following options:\n"
                  "1. create\n"
                  "2. read\n"
                  "3. update\n"
                  "4. delete\n"
                  "5. save/export\n"
                  "6. end program\n")

        selection = int(input("Please enter a number between 1 and 6!\n"        # The variable will get a new value from the user.
                              "Input: "))

        if(selection == 1):     # If the value of the variable is a 1, then this while loop will start.
            while selection != 4:       # The while loop is running, as long as not the number 4 is inserted.
                print("\n""1. add datasets from file (merge)\n"     # The submenu is printed.
                      "2. add new single dataset (via console)\n"
                      "3. add new column (for all datasets)\n"
                      "4. back\n")

                selection = int(input("Please enter a number between 1 and 4!  "))      # The user now can give a new value to the variable.

                if selection != 4:      # If any number except the number 4 is entered, then the text below will be printed and the submenu will be displayed again.
                    print("\n This function is not developed yet.\n")

                if selection > 4:       # If any number above 4 is entered, then the text below is printed out.
                    print("\nThis number is not valid. Please try again.\n")

        elif(selection == 2):       # If the value of the variable is a 2, then this while loop will start.
            while selection != 5:       # The while loop is running, as long as not the number 5 is inserted.
                print("\n""1. show all datasets\n"
                      "2. show single dataset\n"
                      "3. filter ...\n"
                      "4. show empty fields\n"
                      "5. back\n")

                selection = int(input("Please enter a number between 1 and 5!  "))      # The user now can give a new value to the variable.

                if selection == 1:
                    print(df)

                if selection == 2:
                    datasetnr = int(input("Which dataset do you want to show?  "))
                    print(df.iloc[datasetnr])

                if selection == 3:
                    df.filter(like='Werner', axis=1)
                    df.filter

                if selection > 5:       # If any number above 5 is entered, then the text below is printed out.
                    print("\nThis number is not valid. Please try again.\n")

        elif(selection == 3):       # If the value of the variable is a 3, then this while loop will start.
            selection = 1       # The variable is set to 1, because if this would not happen the submenu would close because the input to close the while loop is 3 too.
            while selection != 3:       # The while loop is running, as long as not the number 3 is inserted.
                print("\n""1. update all\n"
                      "2. update single dataset\n"
                      "3. back\n")

                selection = int(input("Please enter a number between 1 and 3!  "))      # The user now can give a new value to the variable.

                if selection != 3:      # If any number except the number 5 is inserted, then the text below will be printed and the submenu will be displayed again.
                    print("\n This function is not developed yet.\n")

                if selection > 3:       # If any number above 3 is entered, then the text below is printed out.
                    print("\nThis number is not valid. Please try again.\n")

        elif(selection == 4):       # If the value of the variable is a 4, then this while loop will start.
            selection = 1       # The variable is set to 1, because if this would not happen the submenu would close because the input to close the while loop is 4 too.
            while selection != 4:       # The while loop is running, as long as not the number 4 is inserted.
                print("\n""1. delete all\n"
                      "2. delete single row\n"
                      "3. delete single column\n"
                      "4. back\n")

                selection = int(input("Please enter a number between 1 and 4!  "))

                if selection != 4:      # If any number except the number 5 is inserted, then the text below will be printed and the submenu will be displayed again.
                    print("\n This function is not developed yet.\n")

                if selection > 4:       # If any number above 4 is entered, then the text below is printed out.
                    print("\nThis number is not valid. Please try again.\n")

        elif(selection == 5):       # If the value of the variable is a 5, then the text below will be displayed.
            print("Saved.")

        elif(selection == 6):       # If the value of the variable is a 6, then the text below will be displayed.
            print("Good Bye!\n"
                  "\n"
                  "====================== END =======================")

        else:       # If any number above 4 is entered, then the text below is printed out and the while loop starts again.
            print("\nThis number is not valid. Please try again.\n")



