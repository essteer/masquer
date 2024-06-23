#!/bin/bash

######################################################
# update.sh
######################################################

# This version 23 June 2024

# Activates venv and runs ./update.py 
# to get and save latest assets

######################################################

# Activate virtual environment
source .venv/bin/activate

# Check whether virtual environment is activated
if ! source .venv/bin/activate; then
  echo "Error: couldn't activate venv."
  echo "Create venv or update this script's venv path."
  exit 1  # Exit with code 1 to indicate an error
fi

# Run update.py
python3 update.py

# Check the exit code of update.py
if [[ $? -eq 1 ]]; then
  echo "Update failed — ensure BeautifulSoup4 is installed."
fi

# Deactivate virtual environment
deactivate
