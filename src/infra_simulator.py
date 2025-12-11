from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ValidationError
from machine import MachineSpecs
from logger import logger, log_message, setup_logging
import subprocess
import json

# welcome message

print("Welcome to the Machine Configuration Manager")

# user agreement loop

while True:
    print("This will create a virtual machine with a preinstalled OS")
    user_response = input("Do you wish to proceed? (y/n): ").lower()

    if user_response == 'n':
        print("Terminating program.")
        exit() # Exits if the user enters 'n'
    elif user_response == 'y':
        print("Please type in the desired specs as instructed")
        break # Continue to the next iteration
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        # The loop will continue, prompting the user again for valid input

# user input section

def get_user_input():
    while True:
        try:
            name = input("Please select a name for your virtual machine: ")
            os = input("Please select one of the following OS options: centos, redhat, ubuntu: ")
            cpu = int(input("Please select one of the following CPU options and type your selection in numbers only: 1 (1 CPU), 2 (2 CPU), 4 (4 CPU): "))
            ram = int(input("Please select one of the following RAM options and type your selection in numbers only: 1 (1GB RAM), 2 (2GB RAM), 4 (4GB RAM): "))
            storage = int(input("Please select one of the following DISK options and type your selection in numbers only: 2 (2GB DISK), 4 (4GB DISK), 8 (8GB DISK): "))

            machine = MachineSpecs(
                name=name, 
                os=os, 
                cpu=cpu, 
                ram=ram, 
                storage=storage
            )
            
            log_message(f"Machine {name} was created")
            return machine
        
        except ValidationError as e:
            print("\nInvalid input:")
            print(e)
            print("\nPlease try again.\n")

# save to json

instances = get_user_input()
with open("configs/instances.json", "w") as f:
    json.dump(instances.dict(), f, indent=4)

# setup installation

def setup_installation():
    try:
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)
        logger.info("Nginx installation completed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to install Nginx: {e}")

# log

log_message("Provisioning started.")
log_message("Provisioning failed due to network issue.",
level="error")

# main

def main():
    machine = instances
    logger.info(f"Provisioning {machine.name}")
    print(machine.to_dict())
    setup_installation()

if __name__ == "__main__":
    main()