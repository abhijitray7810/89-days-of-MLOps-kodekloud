cd /root/code

# Create virtual environment
python3 -m venv ml-env

# Activate virtual environment
source ml-env/bin/activate

# Install required ML libraries
pip install numpy pandas scikit-learn matplotlib

# Generate requirements.txt
pip freeze > /root/code/requirements.txt

# Verify
cat /root/code/requirements.txt
