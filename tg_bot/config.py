# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1362939750:AAGWAKfbkzzDQFlmQgPAAF5NXp4oglJgSuQ"
    OWNER_ID = "1180249738"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "I_AM_AN_PRINCES"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://hixcgohzcigfpn:b81f8eeda4a52905e50cbf65d80c621744e94dcdf1b843ea01cf4bd8afdb4f34@ec2-23-21-236-249.compute-1.amazonaws.com:5432/d6epqfks5skq9a'  # needed for any database modules
    MESSAGE_DUMP = '-1001410340369'  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = []
    WEBHOOK = False
    URL = "https://estella-robots.herokuapp.com/"

    # OPTIONAL
    SUDO_USERS = '1399308798 1229419906 1358136299'  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = '784606914'  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = '1399308798 1229419906 1358136299 784606914'  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = "https://t.me/I_AM_AN_PRINCES"  # EG, paypal
    CERT_PATH = None
    PORT = 5432
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = ''  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    AI_API_KEY = "3ca02d5dc8795c9073825f2bb1fc02d415c19e44bec07d3fe5e48471185acab3bd44f04dd791ad605b4cbe85394e0a8fad16032d7710ad27de1c41149baeee42"
    ENV = "ANYTHING"

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
