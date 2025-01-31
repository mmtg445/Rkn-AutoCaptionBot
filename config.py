# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    
    # Rkn client config  ( required.. 😥)
    API_ID = os.environ.get("API_ID", "26649585")
    API_HASH = os.environ.get("API_HASH", "588a3ea6fd01ae88bd2e10fed7d55b2c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7462631479:AAG5KRfuCC0Xer2naUsiHQAWHV8G2v0pkBw")

    # start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/OAz.jpg")

    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = os.environ.get("FORCE_SUB", "RM_Movie_Flix") 
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption_V05_Bot")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")

    # default caption 
    DEF_CAP = os.environ.get("DEF_CAP", "<b><a href='https//:t.me/Rm_Movie_Flix'>{file_name}\n\n<blockquote>Join Backup Channel: @RM_Movi<\blockquote></a></b>",
    )

    # sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE")

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7822720438').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
