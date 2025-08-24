#!/usr/bin/env python3
"""
Startup script for the Neural Network Receptive Field Calculator
"""

import os
import sys
import subprocess

def main():
    print("🧠 Neural Network Receptive Field Calculator")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found!")
        print("Please run this script from the project directory.")
        sys.exit(1)
    
    # Check if templates directory exists
    if not os.path.exists('templates'):
        print("❌ Error: templates directory not found!")
        print("Please make sure all files are in place.")
        sys.exit(1)
    
    print("✅ All files found!")
    print("\n🚀 Starting Flask application...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        # Run the Flask app
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error running application: {e}")

if __name__ == "__main__":
    main()
