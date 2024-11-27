import os
from datetime import datetime

INSTRUCTIONS_FILE = "instructions.txt"

def file_operations():
    while True:
        print("\nOptions:")
        print("1. Add an instruction")
        print("2. Execute instructions")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            instruction = input("Enter your instruction: ").strip()
            with open(INSTRUCTIONS_FILE, "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{instruction} | {timestamp}\n")
            print("Instruction logged!")

        elif choice == "2":
            if not os.path.exists(INSTRUCTIONS_FILE):
                print("No instructions found.")
            else:
                with open(INSTRUCTIONS_FILE, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        try:
                            instruction, timestamp = line.strip().rsplit(" | ", 1)
                            if instruction.lower() == "time":
                                print(f"Current Time: {datetime.now().strftime('%H:%M:%S')}")
                            elif instruction.lower() == "date":
                                print(f"Current Date: {datetime.now().strftime('%Y-%m-%d')}")
                            else:
                                raise ValueError("Unknown instruction")
                        except Exception as error:
                            print(f"Error with instruction: {instruction}")
                            print(f"Error details: {error}")
        
        elif choice == "3":
            print("Goodbye! Check 'instructions.txt' for your instructions.")
            break

        else:
            print("Invalid choice. Please try again.")
