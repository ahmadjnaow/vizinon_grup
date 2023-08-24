from aiogram import Bot, Dispatcher, types, executor
import logging
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

buttons = [
    types.KeyboardButton('о нас'),
    types.KeyboardButton('объекты'),
    types.KeyboardButton('номера')
]
direction_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply(f"Уважаемый {message.from_user.full_name}, вас приветствует менеджер компании Vizion Group. "
                        "Ахмаджанов Хикматилло. Я готов дать вам информацию о нашей компании.",
                        reply_markup=direction_keyboard)

@dp.message_handler(text='о нас')
async def about_us(message: types.Message):
    await message.reply("""СТРОИТЕЛЬНАЯ КОМПАНИЯ

ОсОО «Визион Групп»
Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в объектах расположенных во всех наиболее привлекательных районах городов Ош и Джалал-Абад. У нас максимально выгодные условия, гибкий (индивидуальный) подход при реализации жилой и коммерческой недвижимости. Мы занимаем лидирующие позиции по количеству объектов по югу Кыргызстана. Наша миссия: Мы обеспечиваем население удобным жильем для всей семьи, проявляя лояльность и индивидуальный подход и обеспечивая высокий уровень обслуживания. Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и опыт профессионалов своего дела.""")

@dp.message_handler(text='объекты')
async def about_objects(message: types.Message):
    with open('obJ_1.jpeg', 'rb') as photo1, open('obj_2.jpg', 'rb') as photo2, \
            open('obj_3.jpeg', 'rb') as photo3, open('obj_4.jpeg', 'rb') as photo4:

        await message.answer("ЖК <<< Млиана Лаф >>> \n г.Ош ул.Мулинова 19")
        await message.answer_photo(  
            photo1,)

        await message.answer("ЖК <<< Томирст >>> \n г.Ош ул.Аматова 1(ориентир-Драм.театр)")
        await message.answer_photo(
            photo2,)
        
        await message.answer("ЖК <<< Черемушки >>> \n г.Ош ул.Урицкого 15б")
        await message.answer_photo(
            photo3, )
        
        await message.answer("ЖК <<< Фрунзу >>> \n г.Ош, Ленина 170")
        await message.answer_photo(
            photo4,)
        
@dp.message_handler(text='номера')
async def contact_numbers(message: types.Message):
    await message.reply("Наши номера:\n+996 709 62-00-88\n+996 772 62-00-88\n+996 550 62-00-88")

executor.start_polling(dp)

