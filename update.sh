#!/bin/bash
set -eu

# 'update.sh' activates a virtual environment and runs 'update.py' 
# to get and save the latest user-agent and referer assets from
# external sources, then deactivates the virtual environment.

# Usage:
# "$ bash update.sh"

this_script=$(basename "$0")
python_script="update.py"
log_filepath="logs/app.log"
venv_path=".venv/bin/activate"

function timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

if [[ ! -f "${log_filepath}" ]]; then
  mkdir -p logs
  touch logs/app.log
  echo "$(timestamp) - INFO - ${this_script} - Log file created at ${log_filepath}" | tee -a "${log_filepath}"
fi
  
if [[ ! -f "${venv_path}" ]]; then
  echo "$(timestamp) - ERROR - ${this_script} - Virtual environment not found at ${venv_path}" | tee -a "${log_filepath}"
  echo "  create a new virtual environment or update 'venv_path' in ${this_script}"
  exit 1
fi

source "${venv_path}"

if [[ ! -f "${python_script}" ]]; then
  echo "$(timestamp) - ERROR - ${this_script} - ${python_script} not found" | tee -a "${log_filepath}"
  deactivate
  exit 1
fi

python3 "${python_script}"
exit_code=$?

case ${exit_code} in
  0)
    echo "$(timestamp) - INFO - ${this_script} - Asset update OK" | tee -a "${log_filepath}"
    ;;
  2)
    echo "$(timestamp) - ERROR - ${this_script} - Asset update failed: check file paths in ${python_script}" | tee -a "${log_filepath}"
    ;;
  3)
    echo "$(timestamp) - ERROR - ${this_script} - Asset update failed: ensure BeautifulSoup4 is installed and check source URLs in ${python_script} are live" | tee -a "${log_filepath}"
    ;;
  *)
    echo "$(timestamp) - ERROR - ${this_script} - Asset update failed with unexpected exit code ${exit_code}" | tee -a "${log_filepath}"
    ;;
esac

deactivate
exit "${exit_code}"
