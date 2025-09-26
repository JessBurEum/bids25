#!/usr/bin/env bash
set -euo pipefail

# Name of the venv directory
VENV_DIR="venv"

# Path to the Python interpreter you want to use
PYTHON_BIN="/bin/python3.12"

# Check if the specified Python exists
if [ ! -x "$PYTHON_BIN" ]; then
    echo "Error: Python interpreter not found at $PYTHON_BIN"
    exit 1
fi

# Create the virtual environment without pip
$PYTHON_BIN -m venv --without-pip "${VENV_DIR}"

# Activate the virtual environment
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

# Bootstrap pip manually
curl -sS https://bootstrap.pypa.io/get-pip.py | python

# Install the OpenStack client package
pip install python-openstackclient pystac-client pystac destinelab python-dotenv geopandas tqdm

# Verify installation
echo "==== python version and packages ===="

python --version          # Should use Python 3.12
pip list                  # Should list python-openstackclient
# openstack --help          # Should display OpenStack CLI help

echo "Python Environment Setup successfully in virtual env: ${VENV_DIR}"


##### Run dedl_hda_pystac.py #####

# Run your Python file automatically
PYTHON_SCRIPT="dedl_hda_pystac.py"

if [ -f "$PYTHON_SCRIPT" ]; then
    echo "Running $PYTHON_SCRIPT..."
    python "$PYTHON_SCRIPT"
else
    echo "Warning: $PYTHON_SCRIPT not found, skipping execution."
fi

