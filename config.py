# Module for discord bot configuration.

from dotenv import load_dotenv
import os


load_dotenv()
config = {
    "prefix": os.getenv("TUTORBOT_PREFIX"),
    "token": os.getenv("TUTORBOT_TOKEN"),
}
