import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '11427887'))
API_HASH = environ.get('API_HASH', '317ea7bfc3dcbfb2a4aa7c866110074e')
BOT_TOKEN = environ.get('BOT_TOKEN', "5836040733:AAHqkrwOnU0tJYC0MfaH7X7c9WXOXwUt3S8")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/c607e2f75626c47449946.jpg https://graph.org/file/9b06d5dd3861f731272fb.jpg https://graph.org/file/a11a38a73e16bb804c3b7.jpg https://graph.org/file/e00f900ffa96eca694b46.jpg https://graph.org/file/bc7e4769fdebe4062b335.jpg https://graph.org/file/f4e8102f7cdc96a9f133b.jpg https://graph.org/file/d6658e838bfb821e7247f.jpg https://graph.org/file/1386506d9c9ed5568e898.jpg https://graph.org/file/d01a531687d2e684eb79b.jpg https://graph.org/file/78ea3afb4dc18cb0443a9.jpg https://graph.org/file/412114a824811c6897c60.jpg https://graph.org/file/ec32b716e26d9b475ec2e.jpg https://graph.org/file/06f78d966309aa76969d7.jpg https://graph.org/file/26f66a3a9efc9d9ebc7c5.jpg https://graph.org/file/d6658e838bfb821e7247f.jpg https://graph.org/file/1386506d9c9ed5568e898.jpg https://graph.org/file/d01a531687d2e684eb79b.jpg https://graph.org/file/78ea3afb4dc18cb0443a9.jpg https://graph.org/file/7c6ce56085d8262a1b5b6.jpg https://graph.org/file/412114a824811c6897c60.jpg https://graph.org/file/ec32b716e26d9b475ec2e.jpg https://graph.org/file/06f78d966309aa76969d7.jpg https://graph.org/file/26f66a3a9efc9d9ebc7c5.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e0770294280f17df23911.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/5f4126f0a68828857243f.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/f6466cc7f17f54ab0ff3e.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1044163529').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001520430666').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1044163529').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL','-1001666069456')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://qtmve:qtmve@cluster0.41lxnpf.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnshort.net')
SHORTLINK_API = environ.get('SHORTLINK_API', '02c93c55c4567035a37ffc32731d8f0e1c530f98')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+tPcOATDcE_cxMzZl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+6jgEtTUwjGwyMWM1')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Qtmve_link/3')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001870756864'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+tPcOATDcE_cxMzZl')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}") 
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001520430666')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
