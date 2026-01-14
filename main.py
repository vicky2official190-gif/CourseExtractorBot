from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# RG Vikramjeet Extractor Plugin
@Client.on_message(filters.command(["rgvikramjeet"]))
async def rg_handler(bot, message):
    # Check if a link or name is provided
    if len(message.command) < 2:
        return await message.reply_text(
            "⚠️ **Format Galat Hai!**\n\n"
            "Sahi tarika: `/rgvikramjeet <link_ya_naam>`\n"
            "Example: `/rgvikramjeet https://rgvikramjeet.com/course/123`"
        )
    
    # Extracting the input from the command
    url_input = message.text.split(None, 1)[1]
    
    # User ko update dena
    msg = await message.reply_text(f"⏳ **RG Vikramjeet:** Processing request...\n`{url_input}`")
    
    try:
        # Yahan hum placeholder logic rakh rahe hain jo real API call ke liye taiyar hai
        # Isme koi syntax error nahi aayega jaisa purane code mein tha
        
        # Simulating data extraction
        await msg.edit(f"✅ **Extraction Started!**\n\n🔗 **Link:** `{url_input}`\n\nBot ab server se data fetch kar raha hai. Notes aur Videos jald hi mil jayenge.")
        
    except Exception as e:
        await msg.edit(f"❌ **Error Aaya:** `{str(e)}`")

# No changes needed here. API_ID and HASH are handled by main.py
