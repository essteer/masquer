#!/bin/bash

# Activates venv and runs ./update.py 
# to get and save latest assets

source .venv/bin/activate

if ! source .venv/bin/activate; then
  echo "Error: couldn't activate venv."
  echo "Create venv or update this script's venv path."
  exit 1
fi

python3 update.py

if [[ $? -eq 1 ]]; then
  echo "Update failed — ensure BeautifulSoup4 is installed."
fi

deactivate
