from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""**- مرحـبـًا عـزيـزي 🙋** {msg.from_user.mention},
في {me2},
**- لبـدء استخـراج الجلسة اختـر بـدء استخـراج الجلسـة .**
**- إذا كنـت تريـد أن يكون حسـابك في أمـان تام فاختر بايروجـرام أمـا إذا كـان رقمك حقيقـي فاختر تيرمـكس .**
** - ملاحظـة :**
**- احـذر مشاركـة الكود لأحـد لأنه يستطيـع اختراق حسـابك ⚠️ .**
[الـمـطـور](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="إضغط لبدا استخراج الكود", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("قناة المطور", url="https://t.me/Q1IIQ"),
                    InlineKeyboardButton("المطور", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
