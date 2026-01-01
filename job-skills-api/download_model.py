#!/usr/bin/env python3
"""
Download spaCy language model if not already present.
This script is run during Railway deployment.
"""
import subprocess
import sys

def download_spacy_model():
    """Download the en_core_web_lg model"""
    try:
        import spacy
        # Try to load the model
        try:
            spacy.load("en_core_web_lg")
            print("✅ spaCy model already downloaded")
        except OSError:
            # Model not found, download it
            print("📥 Downloading spaCy model (en_core_web_lg)...")
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_lg"
            ])
            print("✅ spaCy model downloaded successfully!")
    except Exception as e:
        print(f"❌ Error downloading spaCy model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_spacy_model()
