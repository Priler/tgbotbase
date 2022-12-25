from dotenv import load_dotenv
import os

# Find .env file with os variables
load_dotenv("dev.env")

# retrieve config variables
try:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    BOT_OWNER = int(os.getenv('BOT_OWNER'))
except (TypeError, ValueError) as ex:
    print("Error while reading config:", ex)