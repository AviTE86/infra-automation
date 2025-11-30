from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import json


print("Welcome to the Machine Configuration Manager")
while True:
    print("This will create a virtual machine with a preinstalled OS")
    user_response = input("Do you wish to proceed? (y/n): ").lower()

    if user_response == 'n':
        print("Terminating program.")
        break  # Exits if the user enters 'n'
    elif user_response == 'y':
        print("Please type in the desired specs as instructed")
        # Continue to the next iteration
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        # The loop will continue, prompting the user again for valid input
        
name = input("Please select a name for your virtual machine: ")
os = input("Please select one of the following OS options: centos, redhat, ubuntu: ")
cpu = input("Please select one of the following CPU options and type your selection in numbers only: 1 (1 CPU), 2 (2 CPU), 4 (4 CPU): ")
ram = input("Please select one of the following RAM options and type your selection in numbers only: 1 (1GB RAM), 2 (2GB RAM), 4 (4GB RAM): ")
storage = input("Please select one of the following DISK options and type your selection in numbers only: 2 (2GB DISK), 4 (4GB DISK), 8 (8GB DISK): ")

if __name__ == "__main__":
    main()
    
    