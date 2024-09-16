#!/bin/bash
set -eu

# 'update.sh' activates a virtual environment and runs 'update.py' 
# to get and save the latest user-agent and referer assets from
# external sources, then deactivates the virtual environment.

# Usage:
# "$ bash update.sh"

this_script=$(basename "$0")
python_script="update.py"
venv_path=".venv/bin/activate"

if [[ ! -f "${venv_path}" ]]; then
  echo "${this_script}: error — virtual environment not found at ${venv_path}"
  echo "  create a new virtual environment or update 'venv_path' in ${this_script}"
  exit 1
fi

source "${venv_path}"

if [[ ! -f "${python_script}" ]]; then
  echo "${this_script}: error — ${python_script} not found"
  deactivate
  exit 1
fi

python3 "${python_script}"
exit_code=$?

case ${exit_code} in
  0)
    echo "${this_script}: asset update successful"
    ;;
  2)
    echo "${this_script}: asset update failed — check file paths in ${python_script}"
    ;;
  3)
    echo "${this_script}: asset update failed — ensure BeautifulSoup4 is"
    echo "  installed and check source URLs in ${python_script} are live"
    ;;
  *)
    echo "${this_script}: asset update failed with unexpected exit code ${exit_code}"
    ;;
esac

deactivate
exit "${exit_code}"
