# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = ""
    OWNER_ID = "YOUR ID HERE"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "YOUR USERNAME HERE"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = '-1001410340369'  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 8443
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = ''  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True