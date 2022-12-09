import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29238889"))
    API_HASH = os.environ.get("API_HASH", "0c68821dabe8b48b0c48d649958ba7f2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5595939996:AAHlQaL7eskkbHlkqAg8R2c8Au4Qst_kRZs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCFsExXMgMLaDKjj7T6bJupWrqoTMyFthcDEglPxvC4y1uerMkzuNl6Xa8fpIp143QLajvUKwFIMaPLTZGo6gv3_0oflnyDE4oogo_2w3PZrg7nbGj6RIhnN29AonmeZhasURyYSObMV2JG5VkuDolS0dXYmv55_XSVrAZDGCJzPhrPriN-aWys0DQcO_FHKAIdBMsnJS_84F-Jb_5J7388UioM4DrkhuBWD-sZTdN9LeB0rOjRDq9wtEkKvLBFeLQpGqV2TYVhYiROqh1ZIkt4XPDEgH7mGRZs6XX_iO2kjWX30VQdrH74GL34Eibu8_scM1RTqQoa7hBjs6PS38L2AAAAAVBTYW0A")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "diya_music24_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5595939996")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
