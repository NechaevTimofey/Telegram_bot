import telebot
from telebot import types
from glob import glob
from random import choice
import time

bot = telebot.TeleBot('5141327489:AAHgbCRlvE3_oy6x0hpvFrdS2tUEPPwkWps')

topic = ''


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b> \n' \
           '\n' \
           'Если вы хотите подобрать игру себе по вкусу, напишите команду /choosegame\n' \
           '\n' \
           'Чтобы узнать список всех команд, воспользуйтесь командой /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    mess = '<b>Все команды</b>: \n' \
           '\n' \
           '/start - Приветствие \n' \
           '/help - Список команд \n' \
           '/choosegame - Подобрать игру под себя \n' \
           '/top - Список лучших игр\n' \
           '/avatar - Заставка из произвольно любой игры (топ 50)\n' \
           '/favourite - Избранные игры \n' \
           '/themes - Значение разных тем у игр'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['choosegame'])
def choosegame(message):
    global topic
    topic = ''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    topic1 = types.KeyboardButton('Выживание')
    topic2 = types.KeyboardButton('Открытый мир')
    topic3 = types.KeyboardButton('Тайны и детективы')
    topic4 = types.KeyboardButton('Хоррор')
    markup.add(topic1, topic2, topic3, topic4)
    bot.send_message(message.chat.id, '<b>Выберите тему</b>', reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['top'])
def top(message):
    mess = 'Список самых лучших игр за последние 10 лет, по статистике <b>METACRITIC</b>\n' \
           '<b>Топ</b> <u><b>50</b></u>:\n' \
           '<b>1</b>. Super Mario Galaxy 2\n' \
           '<b>2</b>. The Legend of Zelda: Breath of the Wild\n' \
           '<b>3</b>. Red Dead Redemption 2\n' \
           '<b>4</b>. Grand Theft Auto V\n' \
           '<b>5</b>. Super Mario Odyssey\n' \
           '<b>6</b>. Mass Effect 2\n' \
           '<b>7</b>. The Elder Scrolls V: Skyrim\n' \
           '<b>8</b>. The Last of Us\n' \
           '<b>9</b>. The Last of Us Remastered\n' \
           '<b>10</b>. Red Dead Redemption\n' \
           '<b>11</b>. Portal 2\n' \
           '<b>12</b>. God of War\n' \
           '<b>13</b>. Batman: Arkham City\n' \
           '<b>14</b>. The Legend of Zelda: Ocarina of Time 3D\n' \
           '<b>15</b>. BioShock Infinite\n' \
           '<b>16</b>. Pac-Man Championship Edition DX\n' \
           '<b>17</b>. Divinity: Original Sin II\n' \
           '<b>18</b>. Super Mario 3D World\n' \
           '<b>19</b>. StarCraft II: Wings of Liberty\n' \
           '<b>20</b>. Persona 4 Golden\n' \
           '<b>21</b>. Persona 5\n' \
           '<b>22</b>. Mass Effect 3\n' \
           '<b>23</b>. Metal Gear Solid V: The Phantom Pain\n' \
           '<b>24</b>. The Legend of Zelda: Skyward Sword\n' \
           '<b>25</b>. Rock Band 3\n' \
           "<b>26</b>. Uncharted 4: A Thief's End\n" \
           '<b>27</b>. Super Smash Bros. Ultimate\n' \
           '<b>28</b>. INSIDE\n' \
           '<b>29</b>. Forza Horizon 4\n' \
           '<b>30</b>. God of War III\n' \
           "<b>31</b>. Uncharted 3: Drake's Deception\n" \
           '<b>32</b>. Bloodborne\n' \
           '<b>33</b>. Celeste\n' \
           '<b>34</b>. Super Street Fighter IV\n' \
           '<b>35</b>. The Witcher 3: Wild Hunt\n' \
           '<b>36</b>. Undertale\n' \
           '<b>37</b>. Fire Emblem: Awakening\n' \
           '<b>38</b>. Divinity: Original Sin II — Definitive Edition\n' \
           '<b>39</b>. Super Smash Bros. for Wii U\n' \
           '<b>40</b>. Journey\n' \
            '<b>41</b>. Xenoblade Chronicles\n' \
            "<b>42</b>. Mario Kart 8 Deluxe\n" \
            '<b>43</b>. The ICO & Shadow of the Colossus Collection\n' \
            '<b>44</b>. The Witcher 3: Wild Hunt — Blood and Wine\n' \
            '<b>45</b>. LittleBigPlanet 2\n' \
            '<b>46</b>. Overwatch\n' \
            '<b>47</b>. Bayonetta 2\n' \
            '<b>48</b>. Forza Horizon 3\n' \
            '<b>49</b>. Final Fantasy XIV: Shadowbringers\n' \
            '<b>50</b>. Dragon Quest XI S: Echoes of an Elusive Age — Definitive Edition\n' \
            '\n' \
            'Чтобы узнать список всех команд, воспользуйтесь командой /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['themes'])
def themes(message):
    mess = '<b>Все темы</b>: \n' \
           '\n' \
           '<u><b>Выживание</b></u> - жанр, где главной задачей игрока является сохранение жизни своего персонажа ' \
            'в сложных условиях. Обязательным атрибутом «Выживания» является крафт и открытый ' \
            'мир (по крайней мере, на данный момент). \n' \
           '<u><b>Открытый мир</b></u> - жанр, обозначающий виртуальный мир, который игрок может свободно исследовать ' \
           'и свободно ' \
           'достигать в нем своих целей. Обычно противопоставляется играм с более линейным геймплеем. Геймдизайн игр ' \
           'c возможностью свободного перемещения, как правило, не содержит так называемых «невидимых стен» ' \
           'и экранов загрузки, являющихся обычными при линейном дизайне уровней. \n' \
           '<u><b>Тайны и детективы</b></u> - жанр ролевых игр, основанных на литературном и ' \
           'кинематографическом жанре. ' \
           'Произведения в детективном стиле обычно описывают процесс исследования загадочного происшествия с целью ' \
           'выяснения его обстоятельств и раскрытия загадки. \n' \
           '<u><b>Хоррор</b></u> - жанр компьютерных игр, для которого характерными являются упор на выживание ' \
           'игрового персонажа и ' \
           'нагнетание атмосферы страха и тревоги, подобно литературе и фильмам ужасов.'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['avatar'])
def avatar(message):
    bot.send_message(message.chat.id, 'Заставка из произвольно любой игры:')
    lists = glob('images/*')
    picture = choice(lists)
    bot.send_photo(message.chat.id, open(picture, 'rb'))


@bot.message_handler(commands=['favourite'])
def favourite(message):
    global topic
    ms = 'Что вы хотите сделать со списком избранных игр:'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    topic1 = types.KeyboardButton('Добавить')
    topic2 = types.KeyboardButton('Посмотреть список')
    topic3 = types.KeyboardButton('Удалить')
    markup.add(topic1, topic2, topic3)
    bot.send_message(message.chat.id, ms, reply_markup=markup, parse_mode='html')


def show_gamelist(message):
    with open('gamelist.txt', 'r', encoding='utf-8') as file:
        games = file.readlines()
        if games:
            bot.send_message(message.chat.id, ''.join(games))
        else:
            bot.send_message(message.chat.id, 'Список избранных игр пуст.')


def check_game_in_list(name, function):
    with open('gamelist.txt', 'r', encoding='utf-8') as file:
        games = file.readlines()
        for i in range(len(games) - 1):
            games[i] = games[i][:-1]
        if name in games:
            if function == 'add':
                return False
            else:
                return True
        else:
            if function == 'add':
                return True
            else:
                return False


def add_game_to_list(message):
    with open('gamelist.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{message.text}')
    bot.send_message(message.chat.id, f'<b>{message.text}</b> добавлена.', parse_mode='html')


def remove_game_from_list(message):
    with open('gamelist.txt', 'r', encoding='utf-8') as file:
        games = file.readlines()
        for i in range(len(games) - 1):
            games[i] = games[i][:-1]
        ind = games.index(message.text)
        games.pop(ind)
    with open('gamelist.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(games))
    bot.send_message(message.chat.id, f'<b>{message.text}</b> удалена.', parse_mode='html')


def button_handle(message):
    global topic
    if topic == 'Выживание':
        if message.text == 'Экшен':
            mess1 = 'Список игр <b>Выживание</b> Экшен: \n' \
                    '\n' \
                    'Dread Hunger\n' \
                    'Badlanders\n' \
                    'Longvinter\n' \
                    'Ed-0: Zombie Uprising\n' \
                    'Deadburg\n' \
                    'Rust\n' \
                    'Conan Exiles\n' \
                    'ARK:Survival Evolved\n' \
                    'Astroneer\n' \
                    'Long Dark\n' \
                    'The Forest\n' \
                    'This War of Mine\n' \
                    'RimWorld\n' \
                    'Frostpunk\n' \
                    'Subnautica\n' \
                    'Minecraft\n' \
                    'Terraria\n' \
                    'Dying Light\n' \
                    "No Man's Sky"
            bot.send_message(message.chat.id, mess1, parse_mode='html')
        elif message.text == 'Открытый мир':
            mess2 = 'Список игр <b>Выживание</b> Открытый мир: \n' \
                    '\n' \
                    'The Long Dark\n' \
                    'Alien Shooter 2\n' \
                    'The Evil Within 2\n' \
                    'Darkwood\n' \
                    'Minecraft\n' \
                    'Mutant Year Zero: Road to Eden\n' \
                    'The Wild Eight\n' \
                    'Wild Terra 2: New Lands\n' \
                    'Subnautica\n' \
                    'Alien Shooter: Revisited\n' \
                    'Metro Exodus\n' \
                    'Miasmata\n' \
                    'The Harvest\n' \
                    'No Mans Sky\n' \
                    'Fallen Earth\n' \
                    'Aliens vs. Predator\n' \
                    '35MM\n' \
                    'Pathologic 2\n' \
                    "Dying Light"
            bot.send_message(message.chat.id, mess2, parse_mode='html')
        elif message.text == 'Приключения':
            mess3 = 'Список игр <b>Выживание</b> Приключения: \n' \
                    '\n' \
                    'The Last of Us\n' \
                    'F.E.A.R.\n' \
                    'Resident evil 4\n' \
                    'Resident Evil 2\n' \
                    'The Long Dark\n' \
                    'Terraria\n' \
                    'This War of Mine\n' \
                    'Danganronpa: Trigger Happy Havoc\n' \
                    'Darkwood\n' \
                    "Don't Starve\n" \
                    'Penumbra: Black Plague\n' \
                    'Minecraft\n' \
                    'The Walking Dead: The Game\n' \
                    'The Silent Age\n' \
                    'Sunless Skies\n' \
                    'Mutant Year Zero: Road to Eden\n' \
                    'The Wild Eight\n' \
                    'Rogue Legacy\n' \
                    'The Void'
            bot.send_message(message.chat.id, mess3, parse_mode='html')
        elif message.text == 'Хоррор':
            mess4 = 'Список игр <b>Выживание</b> Хоррор: \n' \
                    '\n' \
                    'The Last of Us\n' \
                    'F.E.A.R.\n' \
                    'Resident evil 4\n' \
                    'Friday the 13th: Killer Puzzle\n' \
                    'Resident Evil 2\n' \
                    'Dead Space 2\n' \
                    'SOMA\n' \
                    'Dead Space\n' \
                    'Silent Hill 3\n' \
                    "The Evil Within 2\n" \
                    'Darkwood\n' \
                    "Don't Starve\n" \
                    'Penumbra: Black Plague\n' \
                    'Teleglitch: Die More Edition\n' \
                    'Mutant Year Zero: Road to Eden\n' \
                    'Silent Hill: Origins\n' \
                    'Dead Nation\n' \
                    'Layers of Fear\n' \
                    'Five Nights at Freddy’s 4'
            bot.send_message(message.chat.id, mess4, parse_mode='html')
        elif message.text == 'От первого лица':
            mess5 = 'Список игр <b>Выживание</b> От первого лица: \n' \
                    '\n' \
                    'Dying Light 2 Stay Human\n' \
                    'Dying Light\n' \
                    'Rust\n' \
                    'DayZ\n' \
                    'Subnautica\n' \
                    '7 Days To Die\n' \
                    'ARK: Survival Evolved\n' \
                    'Resident Evil 7: Biohazard\n' \
                    'Hunt: Showdown\n' \
                    "Stranded Deep\n" \
                    'TheHunter: Call of the Wild\n' \
                    "Left 4 Dead 2\n" \
                    'Long Dark\n' \
                    'Unturned\n' \
                    'Alien: Isolation\n' \
                    'Prey\n' \
                    'Outlast 2\n' \
                    'Will To Live Online\n' \
                    'Deceit'
            bot.send_message(message.chat.id, mess5, parse_mode='html')
        elif message.text == 'Симулятор':
            mess6 = 'Список игр <b>Выживание</b> Симулятор: \n' \
                    '\n' \
                    'The Long Dark\n' \
                    'Rebuild 3: Gangs of Deadsville\n' \
                    'Minecraft\n' \
                    'The Wild Eight\n' \
                    'Subnautica\n' \
                    'Creeper World 3: Arc Eternal\n' \
                    'Minecraft: Story Mode - Season 2\n' \
                    'Dont Starve: Reign of Giants\n' \
                    'No Mans Sky\n' \
                    "Bomber Crew\n" \
                    'The Curious Expedition\n' \
                    "Motorcycle Club\n" \
                    'DayZ\n' \
                    'Running With Rifles\n' \
                    'Dont Starve: Shipwrecked\n' \
                    'Narcosis\n' \
                    'Kingdoms and Castles\n' \
                    'As Far As The Eye\n' \
                    'Rust'
            bot.send_message(message.chat.id, mess6, parse_mode='html')
        elif message.text == 'Исследования':
            mess7 = 'Список игр <b>Выживание</b> Исследования: \n' \
                    '\n' \
                    'The Planet Crafter\n' \
                    'Longvinter\n' \
                    'Dead Man´s Diary\n' \
                    'Ikai\n' \
                    'Expedition Zero\n' \
                    'Deadly Flare\n' \
                    'Arctico\n' \
                    'Lost Scavenger\n' \
                    'The Red Hood\n' \
                    "Frigore\n" \
                    'Desaturation Point\n' \
                    "INTERASTRA\n" \
                    'Parasite\n' \
                    'Canyon\n' \
                    'The WILDS\n' \
                    'Zone Of War\n' \
                    'No Lights 2\n' \
                    'Aquamarine\n' \
                    'Outerverse'
            bot.send_message(message.chat.id, mess7, parse_mode='html')
        elif message.text == 'Атмосферная':
            mess8 = 'Список игр <b>Выживание</b> Атмосферная: \n' \
                    '\n' \
                    'Chromosome Evil\n' \
                    'Ikai\n' \
                    'Expedition Zero\n' \
                    'Office Elevator\n' \
                    'Wild Adventures\n' \
                    'Arctico\n' \
                    'Winter\n' \
                    'Invention 3\n' \
                    'No Lights 2\n' \
                    "Isles of Yore\n" \
                    'They Die Tomorrow\n' \
                    "Wayward Harbor\n" \
                    'Dark Haunting\n' \
                    'Shadow of Egypt\n' \
                    'Phobyark\n' \
                    'GEHENA\n' \
                    'Project XMAS\n' \
                    'Gordon Streaman 2\n' \
                    'Aquamarine'
            bot.send_message(message.chat.id, mess8, parse_mode='html')
        else:
            r = '<b>Я тебя не понимаю</b>'
            bot.send_message(message.chat.id, r, parse_mode='html')
    elif topic == 'Открытый мир':
        if message.text == 'Экшен':
            mess1 = 'Список игр <b>Открытый мир</b> Экшен: \n' \
                    '\n' \
                    'Ведьмак 3: Дикая Охота\n' \
                    'Red Dead Redemption\n' \
                    'Grand Theft Auto V\n' \
                    'Gothic 2: Ночь Ворона\n' \
                    'Batman: Arkham City\n' \
                    'Dragon Age: Origins\n' \
                    'Deus Ex: Human Revolution\n' \
                    'The Long Dark\n' \
                    'Dishonored\n' \
                    'Mafia: The City of Lost Heaven\n' \
                    'The Legend of Zelda: Breath of the Wild\n' \
                    'Horizon: Zero Dawn\n' \
                    'World of Warcraft: The Burning Crusade\n' \
                    'Sekiro: Shadows Die Twice\n' \
                    'Fallout: New Vegas\n' \
                    'DARK SOULS III\n' \
                    'The Elder Scrolls 3: Morrowind\n' \
                    'The Elder Scrolls 5: Skyrim\n' \
                    "Far cry 3"
            bot.send_message(message.chat.id, mess1, parse_mode='html')
        elif message.text == 'Инди':
            mess2 = 'Список игр <b>Открытый мир</b> Инди: \n' \
                    '\n' \
                    'The Long Dark\n' \
                    'Beyond Blue\n' \
                    'Alba: A Wildlife Adventure\n' \
                    'Bright Memory\n' \
                    'Dominions 4: Thrones of Ascension\n' \
                    'Paradise Killer\n' \
                    'Darkwood\n' \
                    'Universe Sandbox 2\n' \
                    'Firewatch\n' \
                    'Dark Souls 3: The Ringed City\n' \
                    'Lords of Xulima\n' \
                    'Minecraft\n' \
                    'Assetto Corsa\n' \
                    'The Wild Eight\n' \
                    'Subnautica\n' \
                    'West of Loathing\n' \
                    'Slime Rancher\n' \
                    'Dont Starve: Reign of Giants\n' \
                    "Rodina"
            bot.send_message(message.chat.id, mess2, parse_mode='html')
        elif message.text == 'Приключения':
            mess3 = 'Список игр <b>Открытый мир</b> Приключения: \n' \
                    '\n' \
                    'Ведьмак 3: Дикая Охота\n' \
                    'Red Dead Redemption\n' \
                    'Grand Theft Auto V\n' \
                    'Gothic 2: Ночь Ворона\n' \
                    'Batman: Arkham City\n' \
                    'The Long Dark\n' \
                    'Dishonored\n' \
                    'Mafia: The City of Lost Heaven\n' \
                    'The Legend of Zelda: Breath of the Wild\n' \
                    'Horizon: Zero Dawn\n' \
                    'Sekiro: Shadows Die Twice\n' \
                    'Fallout: New Vegas\n' \
                    'Beyond Blue\n' \
                    'DARK SOULS III\n' \
                    'The Elder Scrolls 3: Morrowind\n' \
                    'The Elder Scrolls 5: Skyrim\n' \
                    'Lost Ark\n' \
                    'Black Desert Online\n' \
                    "Alba: A Wildlife Adventure"
            bot.send_message(message.chat.id, mess3, parse_mode='html')
        elif message.text == 'Ролевая игра':
            mess4 = 'Список игр <b>Открытый мир</b> Ролевая игра: \n' \
                    '\n' \
                    'Ведьмак 3: Дикая Охота\n' \
                    'Gothic 2: Ночь Ворона\n' \
                    'Space Rangers 2\n' \
                    'Divinity: Original Sin\n' \
                    'Dragon Age: Origins\n' \
                    'Deus Ex: Human Revolution\n' \
                    'Neverwinter online\n' \
                    'Star Stable\n' \
                    'The Legend of Zelda: Breath of the Wild\n' \
                    'Horizon: Zero Dawn\n' \
                    'Sekiro: Shadows Die Twice\n' \
                    'Fallout: New Vegas\n' \
                    'DARK SOULS III\n' \
                    'The Elder Scrolls 3: Morrowind\n' \
                    'The Elder Scrolls 5: Skyrim\n' \
                    'Pillars of Eternity\n' \
                    'Mount & Blade: Warband Napoleonic Wars\n' \
                    'Lost Ark\n' \
                    "Path of Exile"
            bot.send_message(message.chat.id, mess4, parse_mode='html')
        elif message.text == 'От первого лица':
            mess5 = 'Список игр <b>Открытый мир</b> От первого лица: \n' \
                    '\n' \
                    'Star Conflict\n' \
                    'Deus Ex: Human Revolution\n' \
                    'The Long Dark\n' \
                    'Dishonored\n' \
                    'Fallout: New Vegas\n' \
                    'Far cry 3\n' \
                    'Bright Memory\n' \
                    'Titanfall 2\n' \
                    'Need For Speed: Most Wanted\n' \
                    'Paradise Killer\n' \
                    'Fallout 3\n' \
                    'The Evil Within 2\n' \
                    'Borderlands 2\n' \
                    'Red Orchestra: Ostfront 41-45\n' \
                    'Far Cry 3. Blood Dragon\n' \
                    'Firewatch\n' \
                    'Enlisted\n' \
                    'Far cry 4\n' \
                    "Red Dead Online"
            bot.send_message(message.chat.id, mess5, parse_mode='html')
        elif message.text == 'Глубокий сюжет':
            mess6 = 'Список игр <b>Открытый мир</b> Глубокий сюжет: \n' \
                    '\n' \
                    "DEATH STRANDING DIRECTOR'S CUT\n" \
                    'Syberia: The World Before\n' \
                    'Ikai\n' \
                    'ANNO: Mutationem\n' \
                    'FixFox\n' \
                    'Seal World\n' \
                    'Black Geyser: Couriers of Darkness\n' \
                    'Island of the Ancients\n' \
                    'One Of The Victims\n' \
                    'Imp of the Sun\n' \
                    'Lucky Tlhalerwa - Zombie Rampage\n' \
                    'Hidden Deep\n' \
                    'Will You Snail?\n' \
                    'The Tribe Game\n' \
                    'The Upturned\n' \
                    'Strange Horticulture\n' \
                    'Hyperbolica\n' \
                    'Fears to Fathom - Norwood Hitchhike\n' \
                    "Class Escape"
            bot.send_message(message.chat.id, mess6, parse_mode='html')
        elif message.text == '3D':
            mess7 = 'Список игр <b>Открытый мир</b> 3D: \n' \
                    '\n' \
                    "Ведьмак 3: Дикая Охота\n" \
                    'Red Dead Redemption\n' \
                    'Medieval 2: Total War\n' \
                    'Grand Theft Auto V\n' \
                    'Gothic 2: Ночь Ворона\n' \
                    'Batman: Arkham City\n' \
                    'Space Rangers 2\n' \
                    'Divinity: Original Sin\n' \
                    'Dragon Age: Origins\n' \
                    'Star Conflict\n' \
                    'Deus Ex: Human Revolution\n' \
                    'The Long Dark\n' \
                    'Neverwinter online\n' \
                    'Star Stable\n' \
                    'Dishonored\n' \
                    'Mafia: The City of Lost Heaven\n' \
                    'The Legend of Zelda: Breath of the Wild\n' \
                    'Horizon: Zero Dawn\n' \
                    "World of Warcraft: The Burning Crusade"
            bot.send_message(message.chat.id, mess7, parse_mode='html')
        elif message.text == 'Атмосферная':
            mess8 = 'Список игр <b>Открытый мир</b> Атмосферная: \n' \
                    '\n' \
                    "DEATH STRANDING DIRECTOR'S CUT\n" \
                    'Core Keeper\n' \
                    'Ikai\n' \
                    'ELEX II\n' \
                    'Internet Cafe Simulator 2\n' \
                    'Zemblanity\n' \
                    'Tree Simulator 2023\n' \
                    'Easter Bunny\n' \
                    'Glitchhikers: The Spaces Between\n' \
                    'FixFox\n' \
                    'Shadow Fate\n' \
                    'Imp of the Sun\n' \
                    "A Butterfly's Dream\n" \
                    'One Of The Victims\n' \
                    'Mare\n' \
                    'Karisvale\n' \
                    'Submerged: Hidden Depths\n' \
                    'Spaceflight Simulator\n' \
                    "Dead Man´s Diary"
            bot.send_message(message.chat.id, mess8, parse_mode='html')
        else:
            r = '<b>Я тебя не понимаю</b>'
            bot.send_message(message.chat.id, r, parse_mode='html')
    elif topic == 'Тайны и детективы':
        if message.text == 'Приключения':
            mess1 = 'Список игр <b>Тайны и детективы</b> Приключения: \n' \
                    '\n' \
                    'Her Story\n' \
                    'The Wolf Among Us\n' \
                    'Return of the Obra Dinn\n' \
                    'Danganronpa: Trigger Happy Havoc\n' \
                    'Paradise Killer\n' \
                    'Heavy Rain\n' \
                    'Alan Wake\n' \
                    'Falcon City\n' \
                    'Delores: A Thimbleweed Park Mini-Adventure\n' \
                    'Архивы НКВД: Охота на фюрера – Операция “Валькирия”\n' \
                    'Blade Runner\n' \
                    'The Detail Episode 1\n' \
                    'Bright Paw\n' \
                    'Sherlock Holmes: Crimes & Punishments\n' \
                    'Call of the Sea\n' \
                    'The Council\n' \
                    'Gray Matter\n' \
                    'The Raven - Legacy of a Master Thief\n' \
                    "Memoranda"
            bot.send_message(message.chat.id, mess1, parse_mode='html')
        elif message.text == 'Для одного игрока':
            mess2 = 'Список игр <b>Тайны и детективы</b> Для одного игрока: \n' \
                    '\n' \
                    'Her Story\n' \
                    'The Wolf Among Us\n' \
                    'Return of the Obra Dinn\n' \
                    'Danganronpa: Trigger Happy Havoc\n' \
                    'Paradise Killer\n' \
                    'Heavy Rain\n' \
                    'Alan Wake\n' \
                    'Falcon City\n' \
                    'Delores: A Thimbleweed Park Mini-Adventure\n' \
                    'Архивы НКВД: Охота на фюрера – Операция “Валькирия”\n' \
                    'Blade Runner\n' \
                    'The Detail Episode 1\n' \
                    'Bright Paw\n' \
                    'Sherlock Holmes: Crimes & Punishments\n' \
                    'Call of the Sea\n' \
                    'The Council\n' \
                    'Gray Matter\n' \
                    'The Raven - Legacy of a Master Thief\n' \
                    "Sherlock Holmes versus Jack the Ripper"
            bot.send_message(message.chat.id, mess2, parse_mode='html')
        elif message.text == 'Инди':
            mess3 = 'Список игр <b>Тайны и детективы</b> Инди: \n' \
                    '\n' \
                    'Her Story\n' \
                    'Return of the Obra Dinn\n' \
                    'Paradise Killer\n' \
                    'Falcon City\n' \
                    'Delores: A Thimbleweed Park Mini-Adventure\n' \
                    'The Detail Episode 1\n' \
                    'Bright Paw\n' \
                    'Memoranda\n' \
                    'Gemini Rue\n' \
                    'The Painscreek Killings\n' \
                    'This Is the Police\n' \
                    'Enigmatis: The Ghosts of Maple Creek\n' \
                    'Tesla Effect: A Tex Murphy Adventure\n' \
                    'Enigmatis 2: The Mists of Ravenwood\n' \
                    'Vampire: The Masquerade - Shadows of New York\n' \
                    'Thimbleweed Park\n' \
                    'Contrast\n' \
                    'The Blackwell Legacy\n' \
                    "Blameless"
            bot.send_message(message.chat.id, mess3, parse_mode='html')
        elif message.text == 'Глубокий сюжет':
            mess4 = 'Список игр <b>Тайны и детективы</b> Глубокий сюжет: \n' \
                    '\n' \
                    'Disco Elysium - The Final Cut\n' \
                    'Escape Simulator\n' \
                    'Heavy Rain\n' \
                    'Syberia: The World Before\n' \
                    'Sherlock Holmes Chapter One\n' \
                    "Café Stella and the Reaper's Butterflies\n" \
                    'Neverwinter online\n' \
                    'This Is the Police\n' \
                    'Martha Is Dead\n' \
                    'Outer Wilds\n' \
                    'We Were Here Together\n' \
                    'The Dark Pictures Anthology: House of Ashes\n' \
                    'Sherlock Holmes: Crimes and Punishments\n' \
                    'The Wolf Among Us\n' \
                    'Hidden Deep\n' \
                    'The Forgotten City\n' \
                    'SCP: Pandemic\n' \
                    "Five Nights at Freddy's 2\n" \
                    "Cyber Manhunt"
            bot.send_message(message.chat.id, mess4, parse_mode='html')
        elif message.text == 'Атмосферная':
            mess5 = 'Список игр <b>Тайны и детективы</b> Атмосферная: \n' \
                    '\n' \
                    'Alan Wake\n' \
                    'Gray Matter\n' \
                    'Werewolf: The Apocalypse - Heart of the Forest\n' \
                    'Get Even\n' \
                    'Thimbleweed Park\n' \
                    'Black Sails - The Ghost Ship\n' \
                    'Murdered: Soul Suspect\n' \
                    'Blameless\n' \
                    'Parasite Eve\n' \
                    'Remothered: Tormented Fathers\n' \
                    'Danganronpa Another Episode: Ultra Despair Girls\n' \
                    'Husk\n' \
                    'Luci:Horror Story\n' \
                    'Fake Happy End\n' \
                    '1166\n' \
                    'Disco Elysium - The Final Cut\n' \
                    'Sherlock Holmes Chapter One\n' \
                    'Strange Horticulture\n' \
                    "Ghost Exorcism INC."
            bot.send_message(message.chat.id, mess5, parse_mode='html')
        elif message.text == 'Головоломка':
            mess6 = 'Список игр <b>Тайны и детективы</b> Головоломка: \n' \
                    '\n' \
                    "Her Story\n" \
                    'Return of the Obra Dinn\n' \
                    'Danganronpa: Trigger Happy Havoc\n' \
                    'Delores: A Thimbleweed Park Mini-Adventure\n' \
                    'Архивы НКВД: Охота на фюрера – Операция “Валькирия”\n' \
                    'Bright Paw\n' \
                    'Call of the Sea\n' \
                    'The Council\n' \
                    'Gray Matter\n' \
                    'The Raven - Legacy of a Master Thief\n' \
                    'Sherlock Holmes versus Jack the Ripper\n' \
                    'Sherlock Holmes: The Awakened - Remastered Edition\n' \
                    'Sherlock Holmes - Nemesis\n' \
                    'The Painscreek Killings\n' \
                    'Enigmatis: The Ghosts of Maple Creek\n' \
                    'Tesla Effect: A Tex Murphy Adventure\n' \
                    'Still Life 2\n' \
                    'Enigmatis 2: The Mists of Ravenwood\n' \
                    "Puzzle Agent 2"
            bot.send_message(message.chat.id, mess6, parse_mode='html')
        elif message.text == 'Исследования':
            mess7 = 'Список игр <b>Тайны и детективы</b> Исследования: \n' \
                    '\n' \
                    "Syberia: The World Before\n" \
                    'Disco Elysium - The Final Cut\n' \
                    'Escape Simulator\n' \
                    'Police Simulator: Patrol Officers\n' \
                    'Sherlock Holmes Chapter One\n' \
                    'Outer Wilds\n' \
                    'Contraband Police: Prologue\n' \
                    'We Were Here\n' \
                    'Strange Horticulture\n' \
                    'We Were Here Together\n' \
                    "Conrad Stevenson's Paranormal P.I.\n" \
                    'SOMA\n' \
                    'Paradise Killer\n' \
                    'Agatha Christie - Hercule Poirot: The First Cases\n' \
                    'The Sinking City\n' \
                    'The Witness\n' \
                    'What Remains of Edith Finch\n' \
                    'Dear Esther: Landmark Edition\n' \
                    "Firewatch"
            bot.send_message(message.chat.id, mess7, parse_mode='html')
        elif message.text == '2D':
            mess8 = 'Список игр <b>Тайны и детективы</b> 2D: \n' \
                    '\n' \
                    "The Wolf Among Us\n" \
                    'Danganronpa: Trigger Happy Havoc\n' \
                    'Falcon City\n' \
                    'Delores: A Thimbleweed Park Mini-Adventure\n' \
                    'The Detail Episode 1\n' \
                    'Memoranda\n' \
                    'Werewolf: The Apocalypse - Heart of the Forest\n' \
                    'Gemini Rue\n' \
                    'Fetch\n' \
                    'This Is the Police\n' \
                    'Enigmatis: The Ghosts of Maple Creek\n' \
                    'Enigmatis 2: The Mists of Ravenwood\n' \
                    "Vampire: The Masquerade - Shadows of New York\n" \
                    'Gabriel Knight: Sins of the Fathers 20th Anniversary Edition\n' \
                    'Цена свободы: Тайна Кукловода\n' \
                    'Puzzle Agent 2\n' \
                    'Thimbleweed Park\n' \
                    'Contrast\n' \
                    "The Blackwell Legacy"
            bot.send_message(message.chat.id, mess8, parse_mode='html')
        else:
            r = '<b>Я тебя не понимаю</b>'
            bot.send_message(message.chat.id, r, parse_mode='html')
    elif topic == 'Хоррор':
        if message.text == 'Инди':
            mess1 = 'Список игр <b>Хоррор</b> Инди: \n' \
                    '\n' \
                    'Friday the 13th: Killer Puzzle\n' \
                    'The Cat Lady\n' \
                    'INSIDE\n' \
                    'Return of the Obra Dinn\n' \
                    'Beyond Blue\n' \
                    'SOMA\n' \
                    'Amnesia: The Dark Descent\n' \
                    'Darkwood\n' \
                    "Don't Starve\n" \
                    'Firewatch\n' \
                    'Devolverland Expo\n' \
                    'Teleglitch: Die More Edition\n' \
                    'The Void\n' \
                    'Layers of Fear\n' \
                    'DISTRAINT\n' \
                    'Oxenfree\n' \
                    'Project Zomboid\n' \
                    'The Fall\n' \
                    "Bridge Constructor: The Walking Dead"
            bot.send_message(message.chat.id, mess1, parse_mode='html')
        elif message.text == 'Приключения':
            mess2 = 'Список игр <b>Хоррор</b> Приключения: \n' \
                    '\n' \
                    'The Last of Us\n' \
                    'F.E.A.R.\n' \
                    'Resident evil 4\n' \
                    'BioShock\n' \
                    'BioShock Infinite\n' \
                    'Resident Evil 2\n' \
                    'The Cat Lady\n' \
                    'INSIDE\n' \
                    'Return of the Obra Dinn\n' \
                    'Beyond Blue\n' \
                    'DARK SOULS III\n' \
                    'Amnesia: The Dark Descent\n' \
                    'Darkwood\n' \
                    "Don't Starve\n" \
                    'Firewatch\n' \
                    'Red Dead Redemption 2\n' \
                    'Alan Wake\n' \
                    'BioShock 2\n' \
                    "Penumbra: Black Plague"
            bot.send_message(message.chat.id, mess2, parse_mode='html')
        elif message.text == 'Экшен':
            mess3 = 'Список игр <b>Хоррор</b> Экшен: \n' \
                    '\n' \
                    'The Last of Us\n' \
                    'Left 4 Dead\n' \
                    'F.E.A.R.\n' \
                    'Resident evil 4\n' \
                    'BioShock\n' \
                    'BioShock Infinite\n' \
                    'Friday the 13th: Killer Puzzle\n' \
                    'Resident Evil 2\n' \
                    'DARK SOULS III\n' \
                    'Dead Space 2\n' \
                    'Dead Space\n' \
                    'Silent Hill 3\n' \
                    'The Evil Within 2\n' \
                    'Doom 4\n' \
                    'Darkwood\n' \
                    'S.T.A.L.K.E.R.: Зов Припяти\n' \
                    'Red Dead Redemption 2\n' \
                    'Alan Wake\n' \
                    "Outlast"
            bot.send_message(message.chat.id, mess3, parse_mode='html')
        elif message.text == 'Атмосферная':
            mess4 = 'Список игр <b>Хоррор</b> Атмосферная: \n' \
                    '\n' \
                    'Hunt: Showdown\n' \
                    'The Forest\n' \
                    'DEVOUR\n' \
                    'Half-Life: Alyx\n' \
                    'Subnautica\n' \
                    'Vampyr\n' \
                    'Martha Is Dead\n' \
                    'Deceit\n' \
                    'The Beast Inside\n' \
                    'Killing Floor 2\n' \
                    'Black Mesa\n' \
                    'Tiny Bunny\n' \
                    'Little Nightmares II\n' \
                    'OMORI\n' \
                    'Inscryption\n' \
                    'Ghost Exile\n' \
                    'The Dark Pictures Anthology: House of Ashes\n' \
                    'Outlast 2\n' \
                    "Friday the 13th: The Game"
            bot.send_message(message.chat.id, mess4, parse_mode='html')
        elif message.text == 'От первого лица':
            mess5 = 'Список игр <b>Хоррор</b> От первого лица: \n' \
                    '\n' \
                    'Resident Evil 7: Biohazard\n' \
                    'Left 4 Dead 2\n' \
                    'Dead Island\n' \
                    'Outlast\n' \
                    'Wolfenstein: The New Order\n' \
                    'Chernobylite\n' \
                    'Prey\n' \
                    'BioShock\n' \
                    'Outlast 2\n' \
                    'Killing Floor 2\n' \
                    'Evil Within 2\n' \
                    'Dead Island: Riptide\n' \
                    'Singularity\n' \
                    'Мор\n' \
                    'SOMA\n' \
                    'F.E.A.R.\n' \
                    'F.E.A.R. 3\n' \
                    'BioShock 2\n' \
                    "Darkness 2"
            bot.send_message(message.chat.id, mess5, parse_mode='html')
        elif message.text == 'Глубокий сюжет':
            mess6 = 'Список игр <b>Хоррор</b> Глубокий сюжет: \n' \
                    '\n' \
                    "Weird West\n" \
                    'Half-Life: Alyx\n' \
                    "Five Nights at Freddy's: Security Breach\n" \
                    'Vampyr\n' \
                    'ELEX\n' \
                    'Inscryption\n' \
                    'The Dark Pictures Anthology: House of Ashes\n' \
                    'The Beast Inside\n' \
                    'Martha Is Dead\n' \
                    'Black Mesa\n' \
                    'Tiny Bunny\n' \
                    'Little Nightmares II\n' \
                    'OMORI\n' \
                    'Outlast 2\n' \
                    'Gothic 1\n' \
                    'Control Ultimate Edition\n' \
                    'Outer Wilds\n' \
                    "FIVE NIGHTS AT FREDDY'S: HELP WANTED\n" \
                    "Yuppie Psycho: Executive Edition"
            bot.send_message(message.chat.id, mess6, parse_mode='html')
        elif message.text == '3D':
            mess7 = 'Список игр <b>Хоррор</b> 3D: \n' \
                    '\n' \
                    "Doom 4\n" \
                    'S.T.A.L.K.E.R.: Зов Припяти\n' \
                    'Firewatch\n' \
                    'Red Dead Redemption 2\n' \
                    'Alan Wake\n' \
                    'Outlast\n' \
                    'BioShock 2\n' \
                    'Penumbra: Black Plague\n' \
                    'S.T.A.L.K.E.R.: Тень Чернобыля\n' \
                    'Devolverland Expo\n' \
                    'Prey\n' \
                    'Silent Hill: Origins\n' \
                    'Resident Evil 7 biohazard\n' \
                    'Condemned: Criminal Origins\n' \
                    'Dead Nation\n' \
                    'The Void\n' \
                    'System Shock 2\n' \
                    'Resident Evil: Revelations\n' \
                    "Silent Hill 2"
            bot.send_message(message.chat.id, mess7, parse_mode='html')
        elif message.text == 'Мрачная':
            mess8 = 'Список игр <b>Хоррор</b> Мрачная: \n' \
                    '\n' \
                    "Phasmophobia\n" \
                    'Hunt: Showdown\n' \
                    'DEVOUR\n' \
                    'Vampyr\n' \
                    'Inscryption\n' \
                    'Pacify\n' \
                    'Martha Is Dead\n' \
                    'Shadow Warrior 3\n' \
                    'Poppy Playtime\n' \
                    'Tiny Bunny\n' \
                    'Little Nightmares II\n' \
                    'Sally Face - Episode One\n' \
                    "Outlast 2\n" \
                    'Darkest Dungeon\n' \
                    'Friday the 13th: The Game\n' \
                    'Ghost Exorcism INC.\n' \
                    'Blood West\n' \
                    'Outlast\n' \
                    "Occult"
            bot.send_message(message.chat.id, mess8, parse_mode='html')
        else:
            r = '<b>Я тебя не понимаю</b>'
            bot.send_message(message.chat.id, r, parse_mode='html')

    elif topic == 'Добавить':
        correct = check_game_in_list(message.text, 'add')
        if correct:
            add_game_to_list(message)
        else:
            bot.send_message(message.chat.id, f'<b>{message.text}</b> уже есть в списке', parse_mode='html')
        topic = ''
    elif topic == 'Удалить':
        correct = check_game_in_list(message.text, 'delete')
        if correct:
            remove_game_from_list(message)
        else:
            bot.send_message(message.chat.id, f'<b>{message.text}</b> нет в списке', parse_mode='html')
        topic = ''


@bot.message_handler()
def get_topic(message):
    global topic
    if topic:
        button_handle(message)
    else:
        if message.text == 'Выживание':
            topic = 'Выживание'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            genre1 = types.KeyboardButton('Экшен')
            genre2 = types.KeyboardButton('Открытый мир')
            genre3 = types.KeyboardButton('Приключения')
            genre4 = types.KeyboardButton('Хоррор')
            genre5 = types.KeyboardButton('От первого лица')
            genre6 = types.KeyboardButton('Симулятор')
            genre7 = types.KeyboardButton('Исследования')
            genre8 = types.KeyboardButton('Атмосферная')
            markup.add(genre1, genre2, genre3, genre4, genre5, genre6, genre7, genre8)
            bot.send_message(message.chat.id, '<b>Выберите жанр</b>', reply_markup=markup, parse_mode='html')
        elif message.text == 'Открытый мир':
            topic = 'Открытый мир'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            genre1 = types.KeyboardButton('Экшен')
            genre2 = types.KeyboardButton('Инди')
            genre3 = types.KeyboardButton('Приключения')
            genre4 = types.KeyboardButton('Ролевая игра')
            genre5 = types.KeyboardButton('От первого лица')
            genre6 = types.KeyboardButton('Глубокий сюжет')
            genre7 = types.KeyboardButton('3D')
            genre8 = types.KeyboardButton('Атмосферная')
            markup.add(genre1, genre2, genre3, genre4, genre5, genre6, genre7, genre8)
            bot.send_message(message.chat.id, '<b>Выберите жанр</b>', reply_markup=markup, parse_mode='html')
        elif message.text == 'Тайны и детективы':
            topic = 'Тайны и детективы'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            genre1 = types.KeyboardButton('Приключения')
            genre2 = types.KeyboardButton('Для одного игрока')
            genre3 = types.KeyboardButton('Инди')
            genre4 = types.KeyboardButton('Глубокий сюжет')
            genre5 = types.KeyboardButton('Атмосферная')
            genre6 = types.KeyboardButton('Головоломка')
            genre7 = types.KeyboardButton('Исследования')
            genre8 = types.KeyboardButton('2D')
            markup.add(genre1, genre2, genre3, genre4, genre5, genre6, genre7, genre8)
            bot.send_message(message.chat.id, '<b>Выберите жанр</b>', reply_markup=markup, parse_mode='html')
        elif message.text == 'Хоррор':
            topic = 'Хоррор'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            genre1 = types.KeyboardButton('Инди')
            genre2 = types.KeyboardButton('Приключения')
            genre3 = types.KeyboardButton('Экшен')
            genre4 = types.KeyboardButton('Атмосферная')
            genre5 = types.KeyboardButton('От первого лица')
            genre6 = types.KeyboardButton('Глубокий сюжет')
            genre7 = types.KeyboardButton('3D')
            genre8 = types.KeyboardButton('Мрачная')
            markup.add(genre1, genre2, genre3, genre4, genre5, genre6, genre7, genre8)
            bot.send_message(message.chat.id, '<b>Выберите жанр</b>', reply_markup=markup, parse_mode='html')

        elif message.text == 'Добавить':
            topic = 'Добавить'
            bot.send_message(message.chat.id, '<b>Напишите игру которую хотите добавить</b>.', parse_mode='html')
        elif message.text == 'Посмотреть список':
            show_gamelist(message)
        elif message.text == 'Удалить':
            topic = 'Удалить'
            bot.send_message(message.chat.id, '<b>Напишите игру которую хотите удалить</b>.', parse_mode='html')
        else:
            mess = 'Я тебя не понимаю \n' \
                 '\n' \
                 'Воспользуйся /help'
            bot.send_message(message.chat.id, mess, parse_mode='html')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)