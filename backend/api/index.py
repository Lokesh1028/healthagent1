import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# This is what Vercel will call
def handler(request):
    return app

# Alternative export
application = app
