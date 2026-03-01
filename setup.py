#!/usr/bin/env python3
"""
Setup script for ecoVAD_chirpR
Run this from within the cloned repository directory
"""
import os
from pathlib import Path
import subprocess

# Configuration
REPO_LOCAL = Path.cwd()  # Current directory (assumes you're already in the repo)
ASSETS_DIR = REPO_LOCAL / 'assets'

def setup_environment():
    """Setup environment for both Colab and local use"""
    try:
        from google.colab import drive
        print("Running in Google Colab")
        drive.mount('/content/drive')
    except ImportError:
        print("Running locally")

def main():
    setup_environment()
    print(f"Setting up: {REPO_LOCAL}")
    
    # Install requirements
    req_file = REPO_LOCAL / "requirements.txt"
    if req_file.exists():
        print("Installing requirements...")
        subprocess.run(["pip", "install", "-q", "-r", str(req_file)], check=True)
    else:
        print(f"Warning: {req_file} not found!")
    
    # Download assets
    if not ASSETS_DIR.exists():
        print("Downloading and extracting assets...")
        subprocess.run(
            'wget https://osf.io/yvdhf/download -O assets.zip && unzip assets.zip && rm assets.zip',
            shell=True,
            cwd=str(REPO_LOCAL),
            check=True
        )
    else:
        print("Assets already downloaded.")
    
    print("Setup complete!")

if __name__ == "__main__":
    main()
