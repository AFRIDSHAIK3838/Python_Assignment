import os
import pandas as pd

def pandas_operations():
    while True:
        print("\nOptions:")
        print("1. Open/Read CSV")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            file_name = input("Enter the CSV file name (with extension): ").strip()
            if not os.path.exists(file_name):
                print("No such file found. Please check the file name.")
            else:
                try:
                    df = pd.read_csv(file_name)
                    print("\nCSV Content:")
                    print(df)
                except Exception as e:
                    print(f"Error reading file: {e}")

        elif choice == "2":
            print("Exiting Pandas operations.")
            break

        else:
            print("Invalid choice. Please try again.")
