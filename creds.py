import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred:
    BOT_NAME = os.getenv("UozEcpQ7aAGGEJwjDCMIw7WXp0")
    BOT_TOKEN = os.getenv("1958750043:AAEjjcZP-UozEcpQ7aAGGEJwjDCMIw7WXp0")  # From botfather
    API_ID = os.getenv(
        "1087031"
    )  # "Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv(
        "bb081cad2785a8b8cbc98cdd7be26cca"
    )  # "Get this value from my.telegram.org! Please do not steal"
    DB_URL = os.getenv("https://trans-ed69c-default-rtdb.firebaseio.com/")  # From Firebase database
