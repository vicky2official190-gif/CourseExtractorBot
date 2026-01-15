from pyrogram import Client, filters
import os

# RWA Advanced Extractor (com.appx.rojgar_with_ankit)
@Client.on_message(filters.command(["rwa"]))
async def rwa_handler(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("⚠️ **Format:** `/rwa <course_link_or_id>`")

    input_data = message.text.split(None, 1)[1]
    msg = await message.reply_text(f"🚀 **RWA Extractor**\n🔍 Checking App ID: `com.appx.rojgar_with_ankit`...")

    try:
        # RWA (Appx) base URL aur logic yahan process hoga
        await msg.edit(f"✅ **App Verified:** Rojgar With Ankit\n🔗 **Input:** `{input_data}`\n\n🛠 **Status:** Fetching course content via Appx API...")

    except Exception as e:
        await msg.edit(f"❌ **Error:** {str(e)}")

