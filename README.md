Infrastructure Provisioning Simulator

This project simulates infrastructure provisioning workflows using Python, Pydantic validation, structured logging, and external shell scripts.
It allows you to define machine configurations, validate them, log provisioning steps, and run OS-level commands such as installing Nginx on a remote or local Ubuntu machine.

📁 Project Structure
infra-automation/
|
├── configs/
|  ├── instances.json
|── logs/
|  ├── provisioning.log
├── scripts/
|  ├── setup_nginx.sh
├── src/
|  ├── infra_simulator.py
|  ├── logger.py
|  └── machine.py
└── README.md

🧩 Components
1. Python Provisioning Engine

The main provisioning logic is written in Python.
It includes:
machine.py – a Machine class representing each host (OS, CPU, RAM, storage)
logger.py – central logging setup using logging module
infra_simulator.py – loads machine definitions, validates them, logs provisioning steps, and triggers scripts

2. Logging

Logging is centrally configured in logger.py:
Log file: provisioning.log
Formats: timestamp, level, message
Use log_message("text") across the project

3. Bash Script: Installing Nginx

The file setup_nginx.sh automates Nginx installation on Ubuntu:

#!/bin/bash
set -e

sudo apt update -y
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

exit 0

This script is invoked by infra_simulator.py during provisioning if the machine is running Ubuntu.

▶️ Running the Project
1. Ensure the script is executable
chmod +x setup_nginx.sh

2. Run the provisioning program
python3 infra_simulator.py


This will:

Load your machine configs
Validate with Pydantic
Log all actions
Install Nginx (if the machine OS is Ubuntu)

🛠 Requirements

Python 3.10+
Ubuntu (for running the bash script)
Pydantic - if pydantic error occurs run: sudo apt install python3-pydantic
Logging module (built-in)

Install dependencies:
pip install pydantic

📒 Notes

Nginx installation is only triggered for Ubuntu machines
All logging is automatically configured on import (no need to call setup_logging() manually)
Machine definitions must follow the structure in instances.json

📜 License
MIT (or specify your own if needed)