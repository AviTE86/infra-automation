from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import json
from machine import MachineSpecs
import subprocess

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

def get_user_input():
    machines = []
    while True:
        name = input("Please select a name for your virtual machine: ")
        os = input("Please select one of the following OS options: centos, redhat, ubuntu: ")
        cpu = input("Please select one of the following CPU options and type your selection in numbers only: 1 (1 CPU), 2 (2 CPU), 4 (4 CPU): ")
        ram = input("Please select one of the following RAM options and type your selection in numbers only: 1 (1GB RAM), 2 (2GB RAM), 4 (4GB RAM): ")
        storage = input("Please select one of the following DISK options and type your selection in numbers only: 2 (2GB DISK), 4 (4GB DISK), 8 (8GB DISK): ")

        instance_data = {"name": name, "os": os, "cpu": cpu, "ram": ram, "storage": storage}
instances = get_user_input()
with open("configs/instances.json", "w") as f:
    json.dump(instances, f, indent=4)

def setup_installation():
    try:
        subprocess.run(["bash", "scripts/setup_ngnix.sh"],
check=True)
        print("[INFO] Nginx installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install Nginx: {e}")

logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def log_message(message, level="info"):
    if level == "error":
        logging.error(message)
    else:
        logging.info(message)
    print(message)

log_message("Provisioning started.")
log_message("Provisioning failed due to network issue.",
level="error")

def main():
    machine = MachineSpecs("AviServer", "centos", 1, 2, 8)
    logger.info(f"Provisioning {machine.name}")
    print(machine.to_dict())

if __name__ == "__main__":
    main()