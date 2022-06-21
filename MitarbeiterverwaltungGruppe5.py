import pandas as pd #Modul für die Datenbankverwaltung

pd.set_option('display.max_columns', 20) #zur Übersichtlichkeit
pd.set_option('display.max_rows', 20)
pd.options.display.width = 0 #Anzeigeeinstellung
url = 'https://raw.githubusercontent.com/swenrengers/MitarbeiterverwaltungGruppe5/main/export.csv' #Einlesen der CSV
df = pd.read_csv(url, sep=';', index_col=0) #Festlegen des Semikolons als Trenner in der CSV

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
                #test

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
                      "4. sort datasets\n"
                      "5. calculate avarage age\n"
                      "6. show specific columns\n"
                      "7. back\n")

                selection = int(input("Please enter a number between 1 and 5!  "))      # The user now can give a new value to the variable.

                if selection == 1:
                    print(df) #Ausgabe der kompletten Datenbank als Liste zur Ansicht

                if selection == 2:
                    datasetnr = int(input("Which dataset do you want to show?  "))
                    print(df.iloc[datasetnr]) #Anzeige eines bestimmten Datensatzes anhand der ID

                if selection == 3:  # If the value of the variable is a 2, then this while loop will start.
                    while selection != 5:  # The while loop is running, as long as not the number 5 is inserted.
                        print("\n""1. Alter\n" #Auswahl der Rubrik, nach der gefiltert werden soll
                              "2. Name\n"
                              "3. Abteilung\n"
                              "4. Krankenkasse\n"
                              "5. back\n")

                        selection = int(input(
                            "Please enter a number between 1 and 5!  "))  # The user now can give a new value to the variable.

                        if selection == 1:
                            a = int(input("Alter?:\n"))
                            newdfa = df.query('Alter == @a') #Filter nach Alter über die Übergabevariable @a
                            print(newdfa)

                        if selection == 2:
                            n = input("Name?:\n")
                            newdfn = df.query('Name.str.contains(@n)') #Filter nach Name über die Übergabevariable @n
                            print(newdfn)

                        if selection == 3:
                            a = input("Abteilung?:\n")
                            newdfa = df.query('Abteilung.str.contains(@a)') #Filter nach Abteilung über die Übergabevariable @n
                            print(newdfa)

                        if selection == 4:
                            a = input("Krankenkasse?:\n")
                            newdfa = df.query('Krankenkasse.str.contains(@a)') #Filter nach Krankenkasse über die Übergabevariable @n
                            print(newdfa)


                        if selection > 5:  # If any number above 5 is entered, then the text below is printed out.
                            print("\nThis number is not valid. Please try again.\n")

                if selection == 4:
                    a = input("Nach was soll sortiert werden?: \n")
                    df.sort_values(by=[a], inplace=True)
                    print(df)

                if selection == 5:
                    df2 = (round(df["Alter"].mean(),0))
                    print(" The avarage age of the employees is: \n", df2)
                if selection == 6:
                    print(df.Name.to_string(index=False))

                if selection > 7:       # If any number above 5 is entered, then the text below is printed out.
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



