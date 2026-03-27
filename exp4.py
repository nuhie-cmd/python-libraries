import numpy as np

# Temperature dataset
temp = np.array([30, 31, 29, 32, 30, 28, 35, 33, 31, 30])

while True: #menu for user operation
    print("\n--- Climate Stability Analysis ---")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Calculate Variance")
    print("4. Calculate Standard Deviation")
    print("5. Evaluate Climate Stability")
    print("6. Exit")

    choice = int(input("Enter your choice: ")) #to store the input choice

    if choice == 1:
        print("Mean Temperature:", np.mean(temp)) #performs and prints mean

    elif choice == 2:
        print("Median Temperature:", np.median(temp)) #performs and prints median

    elif choice == 3:
        print("Variance:", np.var(temp)) #prforms and prints variance

    elif choice == 4:
        print("Standard Deviation:", np.std(temp)) #performs and prints standard deviation

    elif choice == 5: #defines conditions for climate analysis
        std = np.std(temp) 
        if std > 2:
            print("Prediction: Irregular temperature pattern detected.")
        else:
            print("Prediction: Climate is relatively stable.")

    elif choice == 6: 
        print("Exiting program...")
        break #exits from the menu

    else:
        print("Invalid choice! Try again.")
