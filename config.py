from dotenv import load_dotenv, find_dotenv
import os

# Find .env file with os variables
load_dotenv(find_dotenv())

# retrieve config variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_OWNER = int(os.getenv('BOT_OWNER'))