# Add these imports at the top
import os
from pathlib import Path

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']

# Add this for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Update DEBUG
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Update SECRET_KEY
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key-for-dev')

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')