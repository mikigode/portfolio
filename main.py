# importing libraries
import hashlib
import re
import uuid
import json  # for storing uster info
from aiogram import *
from aiogram.dispatcher.filters import Text
from aiogram.types import *
from text import *
from key import *

# creating bot object and dispatcher
bot = Bot(token='B5091028461:AAFriwOxp3FhUPV5XMqXt67ZjGt3PszGavo')
dp = Dispatcher(bot)

# creating reply keyboard buttons
bt1 = KeyboardButton('👤 Fresh man')
bt2 = KeyboardButton('👷🏽‍♂ 👷🏼‍♀️Engineering')
bt3 = KeyboardButton('Applied')
bt4 = KeyboardButton('🔍 Search courses')
# adding reply keyboard buttons
key1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(bt1, bt2, bt3, bt4)

# inline keyboard buttons
enrol1 = InlineKeyboardButton('Pre-Engineering', callback_data="physics")  # buttons for pre-engineering
enrol2 = InlineKeyboardButton('Pre-Science', callback_data="phys")  # buttons for pre-science
key2 = InlineKeyboardMarkup().add(enrol1, enrol2)

sbut1 = InlineKeyboardButton('sem 1', callback_data='call1')  # creating semester 1 for pre-engineering
sbut1p = InlineKeyboardButton('sem 1', callback_data='call1p')  # creating semester 1 for pre-science
sbute = InlineKeyboardButton('sem 1', callback_data='calle')  # creating semester 1 year 2 for cse
sbute3 = InlineKeyboardButton('sem 1', callback_data='calle3')  # creating semester 1 year 3 for cse
sbute4 = InlineKeyboardButton('sem 1', callback_data='calle4')  # creating semester 1 year 4 for cse
sbute5 = InlineKeyboardButton('sem 1', callback_data='calle5')  # creating semester 1 year 5 for cse

sbutec = InlineKeyboardButton('sem 1', callback_data='callec')  # creating semester 1 year 2 for ece
sbutec1 = InlineKeyboardButton('sem 1', callback_data='callec1')  # creating semester 1 year 3 for ece
sbutec14 = InlineKeyboardButton('sem 1', callback_data='callec14')  # creating semester 1 year 4 for ece
sbutec15 = InlineKeyboardButton('sem 1', callback_data='callec15')  # creating semester 1 year 5 for ece

sbutc2 = InlineKeyboardButton('sem 1', callback_data='callc2')  # creating semester 2 for year 2 epce
sbutc3 = InlineKeyboardButton('sem 1', callback_data='callc3')  # creating semester 2 for year 3 epce
sbutc4 = InlineKeyboardButton('sem 1', callback_data='callc4')  # creating semester 2 for year 4 epce
sbutc5 = InlineKeyboardButton('sem 1', callback_data='callc5')  # creating semester 2 for year 5 epce

sbut2 = InlineKeyboardButton('sem 2', callback_data='call2')  # creating semester 2 for pre-engineering
sbut2p = InlineKeyboardButton('sem 2', callback_data='call2p')  # creating semester 2 for pre-science

sbute2 = InlineKeyboardButton('sem 2', callback_data='calle2')  # creating semester 2 year 2 for cse
sbute23 = InlineKeyboardButton('sem 2', callback_data='calle23')  # creating semester 2 for year 3 cse
sbute42 = InlineKeyboardButton('sem 2', callback_data='calle42')  # creating semester 2 for year 4 cse
sbute52 = InlineKeyboardButton('sem 2', callback_data='calle52')  # creating semester 2 for year 5 cse

sbutec2 = InlineKeyboardButton('sem 2', callback_data='callec2')  # creating semester 2 for year 2 ece
sbutec3 = InlineKeyboardButton('sem 2', callback_data='callec3')  # creating semester 2 for year 3 ece
sbutec4 = InlineKeyboardButton('sem 2', callback_data='callec4')  # creating semester 2 for year 4 ece
sbutec5 = InlineKeyboardButton('sem 2', callback_data='callec5')  # creating semester 2 for year 5 ece

sbutep2 = InlineKeyboardButton('sem 2', callback_data='callep2')  # creating semester 2 for year 2 epce
sbutep3 = InlineKeyboardButton('sem 2', callback_data='callep3')  # creating semester 2 for year 3 epce
sbutep4 = InlineKeyboardButton('sem 2', callback_data='callep4')  # creating semester 2 for year 4 epce
sbutep5 = InlineKeyboardButton('sem 2', callback_data='callep5')  # creating semester 2 for year 5 epce

sbut3x = InlineKeyboardButton('sem 3', callback_data='sem3x')  # creating semester 3 for soeec year 3 and 4
sbut3x4 = InlineKeyboardButton('sem 3', callback_data='sem34')  # creating semester 3 for soeec year 3 and 4

keye = InlineKeyboardMarkup().add(sbute, sbute2)  # adding buttons for pre-engineering
key3 = InlineKeyboardMarkup().add(sbut1, sbut2)

key3p = InlineKeyboardMarkup().add(sbut1p, sbut2p)  # adding buttons for pre-science

key3x = InlineKeyboardMarkup().add(sbute, sbute2, sbut3x)  # adding for cse
key3x3 = InlineKeyboardMarkup().add(sbute3, sbute23, sbut3x)  # adding for cse
key3x4 = InlineKeyboardMarkup().add(sbute4, sbute42, sbut3x4)  # adding for cse
key3x5 = InlineKeyboardMarkup().add(sbute5, sbute52)  # adding for cse

keyec2 = InlineKeyboardMarkup().add(sbutec, sbutec2)
keyec3 = InlineKeyboardMarkup().add(sbutec1, sbutec3)
keyec4 = InlineKeyboardMarkup().add(sbutec14, sbutec4)
keyec5 = InlineKeyboardMarkup().add(sbutec15, sbutec5)

keye2 = InlineKeyboardMarkup().add(sbutc2, sbutep2)
keye3 = InlineKeyboardMarkup().add(sbutc3, sbutep3)
keye4 = InlineKeyboardMarkup().add(sbutc4, sbutep4)
keye5 = InlineKeyboardMarkup().add(sbutc5, sbutep5)

sbut3 = InlineKeyboardButton('SoEEC', callback_data='call3x')  # creating school buttons
sbut4 = InlineKeyboardButton('SoMCE', callback_data='call4')
sbut5 = InlineKeyboardButton('SoCAE', callback_data='call5')
key4 = InlineKeyboardMarkup().add(sbut3, sbut4, sbut5)  # adding school buttons

dep1 = InlineKeyboardButton('CSE', callback_data='dep1')
dep2 = InlineKeyboardButton('ECE', callback_data='dep2')
dep3 = InlineKeyboardButton('EPCE', callback_data='dep3')
keyd = InlineKeyboardMarkup().add(dep1, dep2, dep3)

ynum1x = InlineKeyboardButton('year 2', callback_data='call6x')  # creating year button for cse
ynum2x = InlineKeyboardButton('year 3', callback_data='call7x')
ynum3x = InlineKeyboardButton('year 4', callback_data='call8x')
ynum4x = InlineKeyboardButton('year 5', callback_data='call9x')
key5x = InlineKeyboardMarkup().add(ynum1x, ynum2x, ynum3x, ynum4x)  # adding year button for cse

ynum1 = InlineKeyboardButton('year 2', callback_data='call6')  # creating year buttons for ece
ynum2 = InlineKeyboardButton('year 3', callback_data='call7')
ynum3 = InlineKeyboardButton('year 4', callback_data='call8')
ynum4 = InlineKeyboardButton('year 5', callback_data='call9')
key5 = InlineKeyboardMarkup().add(ynum1, ynum2, ynum3, ynum4)  # adding year button

ynume = InlineKeyboardButton('year 2', callback_data='call6e')  # creating year buttons for epce
ynum2e = InlineKeyboardButton('year 3', callback_data='call7e')
ynum3e = InlineKeyboardButton('year 4', callback_data='call8e')
ynum4e = InlineKeyboardButton('year 5', callback_data='call9e')
key5e = InlineKeyboardMarkup().add(ynume, ynum2e, ynum3e, ynum4e)  # adding year button

backse = InlineKeyboardButton('Back ↪️', callback_data='backe')
back = InlineKeyboardButton('Back ↪️', callback_data='back')  # back buttons
main = InlineKeyboardButton('main menu 🌐', callback_data='main')
key = InlineKeyboardMarkup().add(main, back)
keybe = InlineKeyboardMarkup().add(main, backse)
keya = InlineKeyboardMarkup().add(main)

ab = InlineKeyboardButton('Start Search', switch_inline_query_current_chat="")
keyab = InlineKeyboardMarkup().add(ab)


@dp.message_handler(commands=['start'])  # command for start
async def well(message: types.Message):
    users = json.load(open("users.json", "r"))  # to add user info when they click on start command
    users[message.from_user.id] = {
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "id": message.from_user.id,
        "username": message.from_user.username
    }
    with open("users.json", "w") as newFile:
        json.dump(users, newFile)
    await message.answer('Welcome To ASTU course online bot ',
                         reply_markup=key1)  # adding reply-keyboard buttons)


@dp.message_handler(Text(startswith="/course_"))  # to send document
async def well(message: types.Message):
    await bot.send_document(message.from_user.id,
                            document="BQACAgQAAxkBAAENhnth5WQuwdLSTA6RAAH9QvtMu1DnBBsAAqAJAAJXeyhTyHVidB5-KDYjBA")
    print(message.text)


@dp.message_handler()  # handling input messages form the reply keyboard buttons
async def first_answer(message: types.Message):
    if message.text == '👤 Fresh man':
        await message.answer('select your enrolment ', reply_markup=key2)
    elif message.text == "👷🏽‍♂ 👷🏼‍♀️Engineering":
        await message.answer('select your school', reply_markup=key4)
    elif message.text == "🔍 Search courses":
        await message.answer('you can search courses', reply_markup=keyab)
    elif message.text == "Applied":
        await message.answer('coming soon 😊', reply_markup=keya)


# handling callback for semesters to show courses
@dp.callback_query_handler(
    text=['call1', 'call2', 'calle', 'calle2', 'calle3', 'calle23', 'sem3x', 'calle4', 'calle42', 'sem34', 'calle5',
          'calle52'])
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'call1':
        await call.message.answer(TEXT, reply_markup=key)
    if call.data == 'call2':
        await call.message.answer(TEXT2, reply_markup=key)
    if call.data == 'calle':
        await call.message.answer(TEXT3, reply_markup=keybe)
    if call.data == 'calle2':
        await call.message.answer(TEXT4, reply_markup=keybe)
    if call.data == 'calle3':
        await call.message.answer(TEXT5, reply_markup=keybe)
    if call.data == 'calle23':
        await call.message.answer(TEXT6, reply_markup=keybe)
    if call.data == 'sem3x':
        await call.message.answer('SELECTIVE COURSES', reply_markup=keybe)
    if call.data == 'calle4':
        await call.message.answer(TEXT7, reply_markup=keybe)
    if call.data == 'calle42':
        await call.message.answer(TEXT8, reply_markup=keybe)
    if call.data == 'sem34':
        await call.message.answer('SELECTIVE COURSES', reply_markup=keybe)
    if call.data == 'calle5':
        await call.message.answer(TEXT9, reply_markup=keybe)
    if call.data == 'calle52':
        await call.message.answer(TEXT10, reply_markup=keybe)
    else:
        await call.answer()


@dp.callback_query_handler(text=['callec', 'callec2', 'callec1', 'callec3', 'callec14', 'callec4', 'callec15',
                                 'callec5', 'call4', 'call5'])  # handling callback data for cse semesters
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'callec':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callec2':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callec1':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callec3':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callec14':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callec4':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callec15':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callec5':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'call4':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'call5':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    else:
        await call.answer()


@dp.callback_query_handler(text=['callc2', 'callc3', 'callc4', 'callc5', 'callep2', 'callep3', 'callep4',
                                 'callep5', 'call1p', 'call2p'])  # handling callback data for cse semesters
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'callec2':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callc3':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callc4':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callc5':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callep2':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callep3':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callep4':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'callep5':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    if call.data == 'call1p':
        await call.message.answer('coming soon 😊 😊', reply_markup=keya)
    if call.data == 'call2p':
        await call.message.answer('coming soon 😊', reply_markup=keya)
    else:
        await call.answer()


# handling callback data for pre-engineering and pre-science
@dp.callback_query_handler(text=['physics', 'phys'])
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'physics':
        await call.message.answer('choose the semester for pre-engineering', reply_markup=key3)
    if call.data == 'phys':
        await call.message.answer('choose the semester for pre-science', reply_markup=key3p)
    else:
        await call.answer()


# handling callback data for back and main meanu buttons
@dp.callback_query_handler(text=['main', 'back'])
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'back':
        await call.message.answer('choose your enrolment', reply_markup=key2)
    if call.data == 'main':
        await call.message.answer('Welcome To ASTU course online bot ', reply_markup=key1)


# handling callback data for back and main menu buttons for cse
@dp.callback_query_handler(text=['main', 'backe'])
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'backe':
        await call.message.answer('select your school', reply_markup=key4)
    if call.data == 'main':
        await call.message.answer('Welcome To ASTU course online bot ', reply_markup=key1)


# handling callback data for schools
@dp.callback_query_handler(text=['call3x'])  # call 3x is for cse
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'call3x':
        await call.message.answer('select department',
                                  reply_markup=keyd)  # key 5x is inline keyboard button for cse


@dp.callback_query_handler(text=['dep1', 'dep2', 'dep3'])  # call 3x is for cse
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'dep1':
        await call.message.answer('choose your year', reply_markup=key5x)  # key 5x is inline keyboard button for soeec
    if call.data == 'dep2':
        await call.message.answer('choose your year', reply_markup=key5)
    if call.data == 'dep3':
        await call.message.answer('choose year', reply_markup=key5e)
    else:
        await call.answer()


# handling callback data for years of ECE dep
@dp.callback_query_handler(text=['call6', 'call7', 'call8', 'call9'])
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'call6':
        await call.message.answer('choose the semester for year 2', reply_markup=keyec2)
    if call.data == 'call7':
        await call.message.answer('choose the semester for year 3', reply_markup=keyec3)
    if call.data == 'call8':
        await call.message.answer('choose the semester for year 4', reply_markup=keyec4)
    if call.data == 'call9':
        await call.message.answer('choose the semester for year 5', reply_markup=keyec5)

    else:
        await call.answer()


# handling callback data for years of EPCE dep
@dp.callback_query_handler(text=['call6e', 'call7e', 'call8e', 'call9e'])
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'call6e':
        await call.message.answer('choose the semester for year 2', reply_markup=keye2)
    if call.data == 'call7e':
        await call.message.answer('choose the semester for year 3', reply_markup=keye3)
    if call.data == 'call8e':
        await call.message.answer('choose the semester for year 4', reply_markup=keye4)
    if call.data == 'call9e':
        await call.message.answer('choose the semester for year 5', reply_markup=keye5)

    else:
        await call.answer()


# handling callback data for years of cse
@dp.callback_query_handler(text=['call6x', 'call7x', 'call8x', 'call9x'])
async def call(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == 'call6x':
        await call.message.answer('choose the semester for year 2', reply_markup=keye)
    if call.data == 'call7x':
        await call.message.answer('choose the semester for year 3',
                                  reply_markup=key3x3)  # key3x3 is for adding the 3d semester
    if call.data == 'call8x':
        await call.message.answer('choose the semester for year 4',
                                  reply_markup=key3x4)  # key3x4 is for adding the 3d semester
    if call.data == 'call9x':
        await call.message.answer('choose the semester for year 5', reply_markup=key3x5)

    else:
        await call.answer()


# handler for search
@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or 'opps notting found'

    item = li
    items = []
    i = 0
    for x in item:
        if i > 20:
            break
        if re.search(text.lower(), x.lower()):
            items.append(
                InlineQueryResultCachedDocument(
                    id=str(uuid.uuid4()),
                    title=x,
                    document_file_id="BQACAgQAAxkBAAENhnth5WQuwdLSTA6RAAH9QvtMu1DnBBsAAqAJAAJXeyhTyHVidB5-KDYjBA",
                    caption=x,
                    description=x
                )
            )
            i += 1

    await bot.answer_inline_query(inline_query.id, results=items, cache_time=1)


# to run the code at all times
executor.start_polling(dp)