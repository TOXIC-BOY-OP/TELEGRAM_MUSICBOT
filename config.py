from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("𝐓𝐎𝐗𝐈𝐂 𝐌𝐔𝐒𝐈𝐂 𝐎𝐏")

API_ID = int(getenv("25374274"))
API_HASH = getenv("d0012f0876e6f9308eec2f474e7b9273")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("6109531260").split()))
