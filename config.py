import os

# Environment Variables se data fetch karna
class Config:
    # my.telegram.org se lein
    API_ID = int(os.environ.get("API_ID", "20056632")) # Default value: 1234567
    API_HASH = os.environ.get("API_HASH", "7de392e5406c4eccbc031fc390481730")
    
    # @BotFather se lein
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6545533388:AAEMGYmu28Jkwz_P1VIIEkV3SZQotAf2TjM")
    
    # Aapki Telegram User ID
    OWNER_ID = int(os.environ.get("OWNER_ID", "1822182996"))

# Asaan access ke liye direct variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
OWNER_ID = Config.OWNER_ID
