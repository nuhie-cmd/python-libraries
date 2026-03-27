import pandas as pd   # Import the pandas library and give it the short name 'pd'

data = pd.read_csv("covid_data.csv")   # Read the CSV file named 'covid_data.csv' and store it in a DataFrame called 'data'

while True:   # Start an infinite loop so the menu keeps showing until the user exits

    # Display the menu options to the user
    print("\n--- COVID DATA ANALYSIS MENU ---")
    print("1. Show first few records")      # Option 1: Display first few rows of the dataset
    print("2. Patients per district")      # Option 2: Show district-wise total cases
    print("3. Total male and female cases")# Option 3: Calculate total male and female cases
    print("4. Total recoveries and deaths")# Option 4: Calculate total recoveries and deaths
    print("5. Exit")                       # Option 5: Exit the program

    ch = int(input("Enter choice: "))   # Take user input for menu choice and convert it to integer

    if ch == 1:   # If user selects option 1
        print(data.head())   # Display the first 5 rows of the dataset

    elif ch == 2:   # If user selects option 2
        print(data[['District','TotalCases']])  
        # Display only the 'District' and 'TotalCases' columns from the dataset

    elif ch == 3:   # If user selects option 3
        print("Total Male Cases:", data['Male'].sum())  
        # Calculate and display the sum of the 'Male' column

        print("Total Female Cases:", data['Female'].sum())  
        # Calculate and display the sum of the 'Female' column

    elif ch == 4:   # If user selects option 4
        print("Total Recoveries:", data['Recoveries'].sum())  
        # Calculate and display total recoveries

        print("Total Deaths:", data['Deaths'].sum())  
        # Calculate and display total deaths

    elif ch == 5:   # If user selects option 5
        print("Program ended")   # Display exit message
        break   # Break the loop and terminate the program

    else:   # If user enters an invalid choice
        print("Invalid choice")   # Show error message
