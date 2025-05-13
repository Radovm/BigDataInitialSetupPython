#!/bin/bash

# Update package list and install dependencies
sudo apt update
sudo apt install -y \
  make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm \
  libncurses5-dev libncursesw5-dev xz-utils tk-dev \
  libffi-dev liblzma-dev git \
  libgdbm-dev libgdbm-compat-dev libdb-dev \
  libnss3-dev libexpat1-dev libxml2-dev libxmlsec1-dev \
  tcl-dev unzip default-jre

# Install pyenv
curl https://pyenv.run | bash

# Define pyenv environment variables
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# Initialize pyenv
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Install Python 3.10.17
pyenv install 3.10.17

# Set Python 3.10.17 as the global default
pyenv global 3.10.17

# Verify the installation
python --version

echo "🔧 Creating virtual environment..."
python3 -m venv venv || { echo "❌ Failed to create virtualenv"; exit 1; }

echo "✅ Virtual environment created at ./venv"

echo "📦 Activating virtual environment and installing requirements..."
source venv/bin/activate

# Create requirements.txt if it doesn't exist
if [ ! -f requirements.txt ]; then
  echo "flask" > requirements.txt
  echo "opencv-python-headless" >> requirements.txt
fi

pip install --upgrade pip
pip install -r requirements.txt || { echo "❌ Failed to install packages"; exit 1; }

echo "✅ All packages installed."
echo "🎥 You can now run: source venv/bin/activate && python stream_server.py"
