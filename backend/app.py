"""
Vercel-compatible entry point for AI Health Buddy Backend
"""

import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(__file__))

# Import the FastAPI app from main.py
from main import app

# This is what Vercel will use
if __name__ == "__main__":
    # For local development
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
