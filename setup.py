#!/usr/bin/env python3
"""
Setup script for ecoVAD_chirpR
Intended to be placed in project directory. ecoVAD will be added as a subdirectory.
"""
import os
from pathlib import Path
import subprocess

# Configuration
PROJ = Path('/content/drive/MyDrive/laridae')
REPO_URL = 'https://github.com/joetric/ecoVAD_chirpR'
REPO_LOCAL = PROJ / 'ecoVAD_chirpR'
ASSETS_DIR = REPO_LOCAL / 'assets'

def setup_environment():
    """Setup environment for both Colab and local use"""
    try:
        from google.colab import drive
        print("Running in Google Colab")
        drive.mount('/content/drive')
        return PROJ
    except ImportError:
        print("Running locally")
        return Path(__file__).parent.absolute()

def main():
    base_path = setup_environment()
    print(f"Working directory: {base_path}")
    
    # Clone repo (ignore if exists)
    print("Cloning repository...")
    os.chdir(PROJ)
    subprocess.run(["git", "clone", REPO_URL], capture_output=True)
    os.chdir(REPO_LOCAL)
    
    # Install requirements
    print("Installing requirements...")
    subprocess.run(["pip", "install", "-q", "-r", "requirements.txt"], check=True)
    
    # Download assets
    if not ASSETS_DIR.exists():
        print("Downloading and extracting assets...")
        subprocess.run(
            'wget https://osf.io/yvdhf/download -O assets.zip && unzip assets.zip && rm assets.zip',
            shell=True,
            check=True
        )
    else:
        print("Assets already downloaded. If there's an issue, redownload manually.")
    
    print("Setup complete!")

if __name__ == "__main__":
    main()
