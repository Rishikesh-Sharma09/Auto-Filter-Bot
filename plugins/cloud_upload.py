#use code with proper credit 
# stealing code and mark itas own doesn't make you developer You fool.
#use & customise as per your requirement but with giving proper credit.
#©Rkbotz.t.me ©@infinity_botz.t.me
import os, asyncio, requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def upload_image_requests(image_path):
    upload_url = "https://envs.sh"

    try:
        with open(image_path, 'rb') as file:
            files = {'file': file} 
            response = requests.post(upload_url, files=files)

            if response.status_code == 200:
                return response.text.strip() 
            else:
                raise Exception(f"Upload failed with status code {response.status_code}")

    except Exception as e:
        print(f"Error during upload: {e}")
        return None
@Client.on_message(filters.command("upload") & filters.private)
async def upload_command(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ (ᴘʜᴏᴛᴏ/ᴠɪᴅᴇᴏ) ᴜɴᴅᴇʀ 5ᴍʙ")
        return

    if replied.media and hasattr(replied, 'file_size'):
        if replied.file_size > 5242880: #5mb
            await message.reply_text("File size is greater than 512 MB.")
            return

    infinity_path = await replied.download()

    uploading_message = await message.reply_text("<code>ᴜᴘʟᴏᴀᴅɪɴɢ...</code>")

    try:
        infinity_url = upload_image_requests(infinity_path)
        if not infinity_url:
            raise Exception("Failed to upload file.")
    except Exception as error:
        await uploading_message.edit_text(f"Upload failed: {error}")
        return

    try:
        os.remove(infinity_path)
    except Exception as error:
        print(f"Error removing file: {error}")
        
    await uploading_message.delete()
    await message.reply_photo(
        photo=f'{infinity_url}',
        caption=f"<b>ʏᴏᴜʀ ᴄʟᴏᴜᴅ ʟɪɴᴋ ᴄᴏᴍᴘʟᴇᴛᴇᴅ 👇</b>\n\n𝑳𝒊𝒏𝒌 :-\n\n<code>{infinity_url}</code> <𝚃𝙰𝙿 𝚃𝙾 𝙲𝙾𝙿𝚈>\n\n<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ - @Rkbotz</b>",
        #disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(text="• ᴏᴘᴇɴ ʟɪɴᴋ •", url=infinity_url),
            InlineKeyboardButton(text="• sʜᴀʀᴇ ʟɪɴᴋ •", url=f"https://telegram.me/share/url?url={infinity_url}")
        ], [
            InlineKeyboardButton(text="🗑️ ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ 🗑️", callback_data="close_data")
        ]])
  )

#make you aware again 😏 
# stealing code without credit makes you thief 😂 not developer 
