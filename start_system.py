#!/usr/bin/env python3
"""
Startup script for the Speech Emotion Recognition System
This script will:
1. Check if models are trained
2. Start the Flask backend server
3. Provide instructions for starting the frontend
"""

import os
import sys
import subprocess
import time
import requests
from pathlib import Path

def check_models():
    """Check if trained models exist"""
    models_dir = Path("backend/models")
    required_files = ["best_model.pkl", "scaler.pkl", "label_encoder.pkl"]
    
    for file in required_files:
        if not (models_dir / file).exists():
            return False
    return True

def train_models():
    """Train models if they don't exist"""
    print("🔧 Models not found. Training models...")
    print("⚠️  This will take several minutes...")
    
    # Check if dataset exists
    dataset_dir = "Audio_Speech_Actors_01-24"
    if not os.path.exists(dataset_dir):
        print(f"❌ Dataset directory '{dataset_dir}' not found!")
        print("Please download the RAVDESS dataset and place it in the current directory.")
        return False
    
    try:
        # Run the model training script
        result = subprocess.run([sys.executable, "backend/save_models.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Models trained successfully!")
            return True
        else:
            print(f"❌ Error training models: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running model training: {e}")
        return False

def start_backend():
    """Start the Flask backend server"""
    print("🚀 Starting Flask backend server...")
    
    try:
        # Change to backend directory and start Flask app
        os.chdir("backend")
        subprocess.Popen([sys.executable, "app.py"])
        os.chdir("..")
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Check if server is running
        try:
            response = requests.get("http://localhost:5000/api/health", timeout=5)
            if response.status_code == 200:
                print("✅ Backend server started successfully!")
                return True
        except requests.exceptions.RequestException:
            pass
        
        print("⚠️  Backend server may still be starting...")
        return True
        
    except Exception as e:
        print(f"❌ Error starting backend server: {e}")
        return False

def main():
    """Main startup function"""
    print("🎙️  Speech Emotion Recognition System")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("backend") or not os.path.exists("client"):
        print("❌ Please run this script from the project root directory")
        print("   (the directory containing 'backend' and 'client' folders)")
        sys.exit(1)
    
    # Check and train models if needed
    if not check_models():
        if not train_models():
            print("❌ Failed to train models. Exiting.")
            sys.exit(1)
    else:
        print("✅ Trained models found!")
    
    # Start backend server
    if not start_backend():
        print("❌ Failed to start backend server. Exiting.")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 System is ready!")
    print("\n📋 Next steps:")
    print("1. Open a new terminal/command prompt")
    print("2. Navigate to the 'client' directory")
    print("3. Run: npm install (if not already done)")
    print("4. Run: npm run dev")
    print("5. Open your browser to the URL shown (usually http://localhost:5173)")
    print("\n🎯 How to use:")
    print("- Click the microphone button to start recording")
    print("- Speak for a few seconds")
    print("- Click the microphone button again to stop and get results")
    print("\n🔧 Backend API running at: http://localhost:5000")
    print("📱 Frontend will run at: http://localhost:5173")
    print("\nPress Ctrl+C to stop the backend server")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
        sys.exit(0)
