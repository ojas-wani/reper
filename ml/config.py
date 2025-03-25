import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application settings
APP_NAME = "Research Literature Review"
APP_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# API settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

# Database settings
DATABASE_FOLDER = "database"
MAX_RESULTS_CACHE = 10

# Request handling settings
MAX_WORKERS = 4
REQUEST_TIMEOUT = 300  # 5 minutes
MAX_CONCURRENT_REQUESTS = 10

# Logging settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "app.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Cache settings
CACHE_TTL = 3600  # 1 hour
MAX_CACHE_SIZE = 100  # Maximum number of items to cache

# Security settings
ENABLE_RATE_LIMITING = True
RATE_LIMIT_REQUESTS = 100  # requests per hour
RATE_LIMIT_WINDOW = 3600  # 1 hour in seconds

# UI settings
PAGE_TITLE = "Research Literature Review"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Error messages
ERROR_MESSAGES = {
    "api_error": "An error occurred while processing your request. Please try again later.",
    "timeout": "Request timed out. Please try again with a smaller dataset.",
    "rate_limit": "Too many requests. Please try again later.",
    "validation": "Invalid input. Please check your parameters and try again.",
} 