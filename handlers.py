from main import bot, dp
from aiogram.types import Message
import colorsys
from config import ADMIN_ID

"""async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text="Бот запущен")"""

def to_rgb(color_hex):
    color = color_hex[1:]
    r = int(color[:2], 16)
    g = (int(color[2:4], 16))
    b = (int(color[4:6], 16))

    return r, g, b


def to_hex(matching_colors_rgb):
    res = []
    for i in matching_colors_rgb:
        hex_color = f"#{hex(int(list(i)[0]))[2:]}{hex(round(list(i)[1]))[2:]}{hex(round(list(i)[2]))[2:]}"
        res.append(hex_color)
        # res = [(f"#{hex(int(list(x)[0]))[2:]}{hex(round(list(x)[1]))[2:]}{hex(round(list(x)[2]))[2:]}") for x in matching_colors_rgb]

    return res



def search_color(color: str):
    r, g, b = to_rgb(color)
    h,l,s = colorsys.rgb_to_hls(r, g, b)
    if not(r==g==b):
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        matching_colors_rgb = [colorsys.hls_to_rgb(h+0.0138, l, s),colorsys.hls_to_rgb(h-0.0138, l, s),colorsys.hls_to_rgb(h+0.0276, l, s),colorsys.hls_to_rgb(h-0.0276, l, s),colorsys.hls_to_rgb(h-0.0414, l, s)]
        matching_colors_hex = to_hex(matching_colors_rgb)
    else:
        matching_colors_rgb = [[abs((r+25)-255), abs((r+25)-255), abs((r+25)-255)], [abs((r+50)-255), abs((r+50)-255), abs((r+50)-255)], [(r), (r), (r)], [(r-25), (r-25), (r-25)], [(r-50), (r-50), (r-50)]]
        matching_colors_hex = to_hex(matching_colors_rgb)





    return ", ".join(matching_colors_hex)


@dp.message_handler()
async def echo(message: Message):
    im_text = message.text.lower()
    color = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if len(im_text) == 7 and im_text[0] == "#":
        for i in im_text[1:]:
            if not(i in color):
                await message.answer(text='Такого цвета нет')
                break
        else:
            await message.answer(text=search_color(im_text))


    else:
        await message.answer(text='Такого цвета нет(1)')


    #text = f"Привет, ты написал: {message.text}"
