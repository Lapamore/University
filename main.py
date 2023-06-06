# -*- coding: utf-8 -*-

import telebot
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    token = os.getenv('TOKEN')
    bot = telebot.TeleBot(token = token)

    @bot.message_handler(commands = ["start"])
    def main(message):
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}!\n1. Чтобы посмотреть гайд на своего персонажа введи его имя: Пример: Slark\n2. Чтобы узнать тайминги игры введи: тайминги\n3. Чтобы узнать скорость передвижения персонажей введи: Cкорость передвижения\n4. Чтобы узнать броню героев на первом уровне введи: График брони")
    @bot.message_handler()
    def info(message):
        if message.text.lower() == "привет":
            bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}! Введи название своего персонажа")

        elif message.text.lower() in ("techies ","течес"):
            bot.send_message(message.chat.id, '''Пошел вон со своим течесом. Не буду я тебе ничего присылать''')

        elif message.text.lower() == "скорость передвижения":
            bot.send_message(message.chat.id, '''Скорость передвижения каждого персонажа:''')
            bot.send_photo(message.chat.id, photo=open('Pictures//speed.jpg', 'rb'))

        elif message.text.lower() == "график брони":
            bot.send_message(message.chat.id, '''График брони персонажей на первом уровне, от самого маленького до самого большего:''')
            bot.send_photo(message.chat.id, photo=open('Pictures//armor.jpg', 'rb'))

        elif message.text.lower() == "тайминги":
            bot.send_message(message.chat.id, '''Тайминги патча 7.33c:''')
            bot.send_photo(message.chat.id, photo=open('Pictures//Timings.jpg', 'rb'))

        elif message.text.lower() in ("earthshaker ","шейкер"):
            bot.send_message(message.chat.id, '''Вариант 1:''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Earthshaker//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Earthshaker//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Earthshaker//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Disruptor\n2.Silencer\n3.Death Prophet\n4.Night Stalker\n5.Rubick")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Lina\n2.Gyrocopter\n3.Leshrac\n4.Lion\n5.Dark Seer\n6.Puck")

        elif message.text.lower() in ("enigma","энигма"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант подойдет для тех ситуаций, когда вы видите, что игра развивается очень медленно или когда в начале игры вам удается сделать парочку удачных выходов из леса. В этом случае можно купить ранний Мидас Hand of Midas и затем начать максимально быстро покупать все необходимые артефакты. Само собой Мидас можно не использовать, а просто планомерно покупать ключевые артефакты.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Enigma//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант вариант включает в себя все необходимые артефакты и в принципе может использоваться в большинстве ситуаций. Если вы точно знаете, что сможете постоянно реализовывать ульт очень рано и никто его сбить не сможет, то в этом случае лучше сперва купить Аганим, а с покупкой БКБ немного подождать.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Enigma//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Enigma//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Nature's Prophet\n2.Spectre\n3.Zeus\n4.Beastmaster\n5.Bounty Hunter\n6.Riki\n7.Nyx Assassin")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Tidehunter\n2.Magnus\n3.Axe\n4.Slardar\n5.Axe\n6.Disruptor")

        elif message.text.lower() in ("sniper","снайпер"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант хорошо использовать для центральной линии. В итоге мы получаем Снайпера с хорошим уроном и очень хорошей выживаемостью. В этом варианте не используется невидимость, но хорошая выживаемость доистигается за счет сразу нескольких соответствующих предметов.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Sniper//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант Также можно использовать для центральной линии и для легкой линии. Здесь уже выживаемость достигается за счет невидимости и вампиризма.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Sniper//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Sniper//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Leshrac\n2.Lina\n3.Puck\n4.Pugna\n5.Outworld Devourer\n6.Death Prophet\n7.Invoker\n8.Magnus\n9.Razor\n10.Templar Assassin")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Tidehunter\n2.Enigma\n3.Earthshaker\n4.Faceless Void\n5.Axe\n6.Clockwerk")

        elif message.text.lower() in ("batrider","батрайдер"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант позволяет получить Батрайдера с невероятно хорошей мобильностью и более менее нормальной выживаемостью. Данный вариант хорошо использовать для сложной линии, поэтому в начале и берется сапог.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Batrider//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант также хорошо подойдет для игры на сложной линии, но здесь уже нету Еула и Аганима, а используются Барабаны и Линза.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Batrider//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nТретий вариант можно использовать для средней линии, поэтому он предусматривает покупку бутылки.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Batrider//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Batrider//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Meepo\n2.Broodmother\n3.Enchantress\n4.Visage\n5.Templar Assassin\n6.Tusk\n7.Treant Protector\n8.Terrorblade\n9.Earth Spirit\n10.Necrophos")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Io\n2.Enigma\n3.Tinker\n4.Zeus\n5.Ursa\n6.Mirana")

        elif message.text.lower() in ("windranger","вр","виндрейнжер"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант можно назвать более менее классическим. Основная часть артефактов из этой сборки может быть использована в большинстве игр. В конечном итоге мы получаем очень мобильного героя с хорошим уроном. В некоторых случаях такой ранний Даггер может и не понадобиться, так что его можно покупать после того, как у вас появится Аганим. Вариант хорошо подойдет для центральной линии и в принципе может быть использован даже для легкой линии.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Windranger//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант очень сильно похож на прошлый, но я бы его советовал для сложной линии. Также он включает в себя покупку Дезолятора, который при необходимости может быть заменен другим артефактом на урон.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Windranger//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Windranger//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Dragon Knight\n2.Tiny\n3.Pudge\n4.Ember Spirit\n5.Magnus\n6.Ursa\n7.Lifestealer\n8.Lycan\n9.Sven\n10.Alchemist")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Lion\n2.Shadow Shaman")

        elif message.text.lower() in ("huskar","хускар"):
            bot.send_message(message.chat.id, '''Данный вариант является своего рода классическим, если можно так выразиться. В конечном итоге мы получаем героя с очень хорошим уроном и отличной выживаемостью. Стоит понимать, что артефакты могут покупать в разном порядке. Самое главное следить за тем, что вам требуется именно в текущий момент.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Huskar//first_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Huskar//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Lina\n2.Omniknight\n3.Queen of Pain\n4.Tinker\n5.Enigma\n6.Bane\n7.Outworld Devourer")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Nature's Prophet\n2.Ancient Apparition\n3.Dazzle\n4.Shadow Demon\n5.Necrophos")

        elif message.text.lower() in ("magnus","магнус"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант является наиболее стандартным и используется в основном для центральной линии. Сначала покупаются предметы для того, чтобы комфортно фармить на линии, ну или хотя бы для того, чтобы умирать. К этим предметам относятся артефакты на реген и восстановления здоровья и маны. Далее уже очень важно максимально быстро выфармить Blink Dagger, так как Даггер позволит очень эффективно инициировать сражение и даст Магнусу превосходную мобильность. Затем покупаются предметы на выживаемость и обязательно Рефрешер, чтобы иметь возможность дважды использовать ульт.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Magnus//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант представляет из себя сборку для Магнуса, который выполняет роль второстепенного керри героя и способен нанести огромный урон в сочетании со своим ультом и другими способностями. Стоит понимать, что Магнус конечно наносит хороший урон, но есть огромное количество героев, которые при хорошей сборке будут более эффективными в роли керри героя, по этому для Магнуса очень важно играть максимально агрессивно и не затягивать игру. После 25 минут эффективность такого Магнуса будет постепенно падать, так как враги будут покупать все больше и больше артефактов. Само собой удачный врыв и пара хороших ударов могут привести к тому, что вы убьете сразу нескольких врагов даже без помощи своих союзников, но получаться этот будет далеко не всегда.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Magnus//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nТретий вариант сборки лучше всего подойдет для Магнуса, который начинает свою игру на сложной линии. В целом сборка очень похожа на первый вариант. Различие в том, что на сложной линии Магнус не сможет так хорошо фармить как на центре, а значит и сборка для него будет немного скуднее.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Magnus//third_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 4:\nПоследний вариант сборки подойдет для Магнуса, который максимально специализирован на помощи своей команде. Основная идея состоит в том, чтобы бы собрать раннюю Меку и вместе со своими союзниками начать активно пушить линии и разводить врага на крупные сражения. При таком варианте игра может закончиться значительно быстрее, особенно если ваша команда обладает хорошим потенциалом для ранних драк и способна быстро сносить строения врага.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Magnus//fourth_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Magnus//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Nature's Prophet\n2.Spectre\n3.Zeus\n4.Clockwerk\n5.Beastmaster\n6.Bounty Hunter\n7.Nyx Assassin")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Sand King\n2.Tidehunter\n3.Queen of Pain\n4.Shadow Fiend\n5.Kunkka")

        elif message.text.lower() in ("tinker","тинкер"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант позволяет получить мобильного Тинкера, с отличным уроном и хорошей выживаемостью, которая обеспечивается большим запасом здоровья и броней.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Tinker//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВо втором варианте используется Дагон, который значительно увеличит разовый урон Тинкера.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Tinker//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Tinker//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Viper\n2.Death Prophet\n3.Batrider\n4.Templar Assassin\n5.Storm Spirit\n6.Pugna\n7.Nyx Assassin\n8.Anti-Mage\n9.Spectre\n10.Ember Spirit")
            bot.send_message(message.chat.id,"Cоюзники:\nТинкер является самостоятельным героем, которому в общем-то не требуются какие-то особенные союзники. Если в команде будут хорошие инициаторы, с мощным АОЕ контролем, то это конечно здорово, так как в бою Тинкер сможет хорошо раскастоваться. Если же подобных героев нету, то ничего страшного. Тинкер может очень хорошо приспособиться к текущей ситуации игры и этому герою всегда есть чем заняться.")


        elif message.text.lower() in ("arc warden","зет","арк"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант включает в себя покупку предметов на контроль и урон. В итоге мы будем иметь героя с одинаково хорошим магическим и физическим уроном. Данная сборка позволяет осуществлять эффективные ганги и быстро убивать одиночные цели.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Arc_warden//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВо втором варианте мне хотелось привести не просто сборку для Нюкера, а вариант который может быть использован при игре на легкой линии в роли сапорта. То есть мы не идем стандартно на центр, отправляемся на легкую линию и зарабатываем там золото на отводах и помощи в убийствах. После покупки Мидаса начинаем быстро зарабатывать золото и одновременно с этим ищем возможности для ганга. Если рассматривать вариант классического нюкера, то само собой никаких курьеров не будет. То есть мы просто отправляемся например на центр, быстро фармим на Мидас и далее уже покупаем Дагон со всеми последующими предметами.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Arc_warden//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nПоследний вариант в целом очень похож на первый, но здесь в начале игры мы покупаем Shadow Blade и устраиваем ганги за счет невидимости и использования Orchid Malevolence.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Arc_warden//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Arc_warden//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Lycan\n2.Chaos Knight\n3.Phantom Lancer\n4.Naga Siren\n5.Meepo\n6.Clinkz\n7.Riki\n8.Clinkz\n9.Bounty Hunter\n10.Slark")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Oracle\n2.Witch Doctor\n3.Slardar\n4.Omniknight")

        elif message.text.lower() in ("lion","лион"):
            bot.send_message(message.chat.id, '''Вариант 1(саппорт):\nДанный вариант является наиболее популярным для Лиона. Само собой все предметы могут покупаться в разной последовательности, а также в сборку можно внести огромное количество изменений, нов целом вы можете спокойно опираться на примерно такой итем билд. С такими предметами мы получаем очень мобильного Лиона, способного сеять панику и ужас в сердца врагов по всей карте.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Lion//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2(соло центр):\nСразу хочу сказать, что вариант игры Лиона на центральной линии это очень редкий и ситуационный выбор, но если же вам выпала такая честь, то можно опираться на следующую сборку предметов.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Lion//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3(нюкер):\nЕсли вашей команде требуется не просто сапорт, а герой способный убивать врагов буквально с прокаста, то данный вариант будет наиболее оптимальным.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Lion//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Lion//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Visage\n2.Pugna\n3.Bane\n4.Chen\n5.Enchantress\n6.Nature's Prophet\n7.Oracle\n8.Clinkz\n9.Nyx Assassin\n10.Clockwerk")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Chen\n2.Enchantress\n3.Lina\n4.Slardar\n5.Enchantress\n6.Centaur Warrunner\n7.Phantom Assassin\n8.Ursa")

        elif message.text.lower() in ("slark","сларк"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант предусматривает покупку Мидаса.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Slark//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант это своего рода универсальная сборка, которую можно использовать для большинства ситуаций.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Slark//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nПоследний вариант подойдет для очень агрессивной игры.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Slark//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Slark//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Drow Ranger\n2.Sniper\n3.Luna\n4.Medusa\n5.Warlock\n6.Venomancer\n7.Witch Doctor\n8.Keeper of the Light\n9.Anti-Mage\n10.Juggernaut")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Ogre Magi\n2.Omniknight\n3.Magnus\n4.Ancient Apparition")

        elif message.text.lower() in ("juggernaut","джага", "юрнеро",'джагер'):
            bot.send_message(message.chat.id, '''Вариант 1:\nДанный вариант используется при спокойной игре на легкой линии.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Juggernaut//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант также подойдет для ситуации, когда в команде противника есть жесткие дамагеры, но он предусматривает покупку Манты в сочетании с Дифузами. Таким образом сборка будет очень эффективна против героев, зависимых от маны.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Juggernaut//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nТретий вариант позволяет получить Джаггера с очень хорошим уроном. В этом варианте нету Даггера, но присутствует Monkey King Bar, то есть предусматривается, что в команде противника есть герои с уворотом (например Phantom Assassin). Если таких героев нету и никто не собирается покупать бабочку, то МКБ лучше не брать, а взять что-то более подходящее.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Juggernaut//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Juggernaut//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Wraith King\n2.Ursa\n3.Sven\n4.Lifestealer\n5.Slark\n6.Chaos Knight\n7.Night Stalker\n8.Omniknight\n9.Abaddon\n10.Necrophos")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Crystal Maiden\n2.Lion\n3.Rubick\n4.Shadow Shaman\n5.Witch Doctor\n6.Vengeful Spirit\n7.Venomancer")

        elif message.text.lower() in ("зевс","zeus"):
            bot.send_message(message.chat.id, '''Вариант 1:\nУспеть собрать линзу в начале игры будет конечно сложно, но это можно сделать и в середине игры. Учтите, что в данном варианте Аганим покупается очень рано и это должно быть оправданно. То есть нужно очень хорошо следить за другими линиями и участками карты и вовремя использовать грозовое облако. Даггер здесь использован для повышения мобильности. В место него можно купить Eul's Scepter of Divinity. Также хочу обратить ваше внимание на очень раннюю покупку Boots of Travel. Делать это не обязательно и сапоги могут быть взяты ближе к концу игры (примерно 5 слотом). Вместо Дагона может быть использован другой артефакт, например Рефрешер.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Zeus//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nОтличительной особенность второго варианта является покупка Veil of Discord. Такой вариант особенно хорошо использовать в том случае, если помимо Зевса в вашей команде есть другие серьезные герои с магическим уроном.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Zeus//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nПоследний вариант это более спокойная сборка, которая включает в себя все самые необходимые артефакты и может подойти для огромного количества ситуаций.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Zeus//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Zeus//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Axe\n2.Enigma\n3.Earthshaker\n4.Slardar\n5.Sand King\n6.Enchantress\n7.Crystal Maiden\n8.Luna\n9.Venomancer\n10.Windranger")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Crystal Maiden\n2.Bloodseeker\n3.Enigma")

        elif message.text.lower() in ("пудж","мясник","pudge"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант сборки является одним из самых популярных. Он позволяет с самого начала игры действовать более менее агрессивно и начать активно гангать разные линии. За счет хороших танковых качеств Пудж сможет пушить линии, принимая урон башен на себя, а также сможет легко переносить разного рода магические способности врага. По сути это золотая середина. Стоит понимать, что при таком вариант в вашей команде обязательно должен быть как минимум один мощный дамагер, который будет легко убивать врагов на позднем этапе игры, так как Пудж в данном случае выступает больше в роли инициатора и основную угрозу будет представлять в первую половину игры.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Pudge//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант закупа дает Пуджу максимальный урон в кратчайшие сроки. Данный вариант подойдет в том случае, если вы с самого начала играете очень агрессивно и ваша активная игра приносит доход в виде золота. По сути до самого конца игры Пудж будет постоянно наращивать свою мощь и всегда оставаться мощным комбо нюкером. Также сборка будет очень эффективна против героев, которые играют разрозненно. В этом случае Пудж сможет спокойно в соло расправляться с врагами и быстро покупать все необходимые артефакты.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Pudge//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nСразу хочу оговорится, что Пудж не является полноценным керри героем и он выступает на втором плане. Обычно роль керри героя выбирается по ходу игры, когда вы видите, что урона в вашей команде недостаточно и вам придется играть в роли дополнительного керри. Стоит также понимать, что в данном случае основная полезность Пуджа будет в конце игры, но гангать он все же спокойно может. По сути в конце игры Пудж будет выполнять роль полу-танка полу-дамагера.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Pudge//third_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 4:\nДанный вид сборки является очень ситуационным. В первую очередь он направлен на то, чтобы получить максимально мобильного Пуджа, который быстро перемещается между линиями и часто гангает вражеских героев. За счет хорошего регена маны и здоровья, возвращаться на базу Пудж будет гораздо реже, а различные комбинации использования артефактов не оставят врагам и малейшего шанса на побег. Покупка БКБ позволит инициировать бой сразу с применения ульта, а также повысит выживаемость Пуджа.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Pudge//fourth_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Pudge//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Centaur Warrunner\n2.Clockwerk\n3.Slardar\n4.Doom\n5.Wraith King\n6.Dragon Knight\n7.Puck\n8.Storm Spirit\n9.Queen of Pain\n10.Weaver")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Omniknight\n2.Dark Seer\n3.Io\n4.Oracle\n5.EarthShaker")

        elif message.text.lower() in ("ио","висп","io"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант включает в себя покупку всех самых необходимых предметов и одним из ключевых артефактов здесь является Guardian Greaves.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Io//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВторой вариант практически идентичен первому, но здесь в начале игры мы не покупаем предметов, а быстро приносим себе бутылку.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Io//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Io//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Beastmaster\n2.Lycan\n3.Chen\n4.Terrorblade\n5.Lone Druid\n6.Gyrocopter\n7.Luna\n8.Spectre\n9.Ancient Apparition\n10.Disruptor")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Tiny\n2.Chaos Knight\n3.Sven\n4.Dragon Knight\n5.Wraith King\n6.Alchemist\n7.Legion Commander\n8.Lifestealer")

        elif message.text.lower() in ("цм","crystal maiden"):
            bot.send_message(message.chat.id, '''Вариант 1:\nПервый вариант позволяет получить очень мобильную Кристалку, способную быстро перемещаться по карте и помогать своим союзникам. Стоит понимать, что в данной сборке нет БУБ или Глимера, то есть этот вариант подойдет в тех случаях, когда в команде противника мало умений контроля и у вас есть возможность более спокойно использовать свой ульт. Конечно в самом конце один из этих артефактов можно будет спокойно добавить в сборку. Соответственно вместо Владмира может быть любой другой артефакт на защиту.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Crystal_maiden//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2:\nВо втором варианте не используется Даггер, но за счет БКБ и Глимера мы получим Кристалку с хорошей выживаемостью и возможностью более менее спокойно применять свой ульт. Мобильности тут конечно будет значительно меньше.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Crystal_maiden//second_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 3:\nПоследний вариант является также сбалансированным и включает в себя покупку всех необходимых артефактов. В итоге мы получаем более менее мобильного героя с хорошей выживаемостью.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Crystal_maiden//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Crystal_maiden//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Troll Warlord\n2.Phantom Assassin\n3.Bounty Hunter\n4.Dragon Knight\n5.Lycan\n6.Alchemist\n7.Templar Assassin\n8.Night Stalker\n9.Ursa\n10.Viper")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Juggernaut\n2.Phantom Assassin\n3.Sven\n4.Spectre\n5.Anti-Mage\n6.Slark\n7.Lifestealer\n8.Chaos Knight")

        elif message.text.lower() in ("никс","nyx assassin"):
            bot.send_message(message.chat.id, '''Вариант 1 (для ганга):\nДанный вариант лучше всего подойдет для Никса, который начинает игру с центра и планирует быть очень эффективным героем во время гангов. Сразу после покупки бутылки, волшебной палочки и сапогов, стоит стремится к тому, чтобы как можно скорее нафармить денег на первый Дагон. Можно не улучшать ботинки в Arcane Boots, так как за счет бутылки и остальных предметов у Никса будет хороший реген. Конечно если вам крайне не хватает маны, то в последствии можно взять сапоги, но не стоит улучшать их до покупки Дагона, чтобы не тратить деньги и соответственно время. В последствии также покупается Ethereal Blade, чтобы еще сильнее повысить нюк потенциал. Улучшать Дагон можно до покупки Ethereal Blade или после. Если допустим вы не видите угрозы со стороны героев с физическим уроном, то можно улучшить Дагон сразу. Если же угроза есть и сильная, то лучше начать улучшать Дагон после покупки Ethereal Blade или хотя бы Ghost Scepter В конце уже докупаются ботинки с телепортом, чтобы иметь возможность быстро перемещаться по карте и выслеживать отбившихся врагов.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Nyx_Assassin//first_buy.png', 'rb'))
            bot.send_message(message.chat.id, '''Вариант 2 (для сапорта):\nВ этом варианте для Никса является приоритетной задачей в начале максимально быстро получить сапоги Arcane Boots. Это позволит восстанавливать ману себе и рядом стоящим союзникам. Далее уже есть смысл купить урну и начать активные действия по карте. Затем уже покупаются Force Staff и Eul's Scepter of Divinity. Оба артефакта повысят мобильность, выживаемость героя и будут очень хорошо помогать вашим союзникам. В заключении можно приобрести Scythe of Vyse, что бы получить в свой арсенал жесткое умение контроля.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Nyx_Assassin//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Nyx_Assassin//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Dragon Knight\n2.Centaur Warrunner\n3.Tidehunter\n4.Bristleback\n5.Night Stalker\n6.Death Prophet\n7.Silencer\n8.Juggernaut\n9.Lifestealer\n10.Omniknight")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Spirit Breaker\n2.Storm Spirit\n3.Clockwerk\n4.Night Stalker\n5.Queen of Pain\n6.Nature's Prophet\n7.Zeus\n8.Spectre")

        elif message.text.lower() in ("тини","tiny"):
            bot.send_message(message.chat.id,'''Вариант 1:\nПервый вариант хорошо использовать для центральной линии. Он включает в себя одновременную покупку Blink Dagger и Shadow Blade. Это дает возможность постоянно нападать на врагов и убивать их максимально быстро''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Tiny//first_buy.png', 'rb'))
            bot.send_message(message.chat.id,'''Вариант 2\nВторой вариант больше подойдет для тех ситуаций, когда необходимо большое количество здоровья и защита.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Tiny//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,'''Вариант 3:\nПоследний вариант позволяет получить Тини с очень мощной разовой автоатакой.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Tiny//third_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Tiny//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Necrophos\n2.Omniknight\n3.Lifestealer\n4.Zeus\n5.Doom\n6.Bristleback")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Tidehunter\n2.Enigma\n3.Earthshaker\n4.Beastmaster\n5.Axe\n6.Magnus\n7.Отдельно стоит выделить связку Tiny + Io. Благодаря ульту Виспа можно постоянно нападать на разные линии. Ко всему прочему Висп увеличит скорость атаки и скорость передвижения")

        elif message.text.lower() in ("вивер","weawer"):
            bot.send_message(message.chat.id,'''Вариант 1 (быстрая линка):\nЕсли вы решили закупаться по данному варианту, то начинать стоит с кольца на защиту, которое в последствии улучшается в базилку прямо на линии. Затем вы можете купить кольцо регенерации в том же боковом магазине и уже более комфортно чувствовать себя на линии. Далее уже вы фармите на линку и тем самым значительно повышаете выживаемость Вивера. Затем стоит задуматься о повышении урона и в этом случае может хорошо подойти Daedalus. Затем вы снова инвестируете деньги в выживаемость и покупаете Heart of Tarrasque, после чего снова повышаете свой урон за счет новых артефактов. Вместо Heart of Tarrasque можно также использовать БКБ.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Weawer//first_buy.png', 'rb'))
            bot.send_message(message.chat.id,'''Вариант 2 (быстрый БКБ):\nВторой вариант предназначен для более агрессивной игры, которая подразумевает, что вы начнете очень активно харасить врага с самого начала игры и начнете очень рано передвигаться по карте и искать возможности для убийства врага. В командных сражениях БКБ будет более актальной покупкой чем линка, а значит и стремится мы будем к этому артефакту. Само собой это не означает, что данный предмет покупается в первую очередь, просто БКБ будет первым значимым предметом в нашем инвентаре. Сборка включает в себя покупку медальона и дезолятора. В сочетании с жуками это позволит моментально снижать броню врага и очень быстро его убивать.''')
            bot.send_photo(message.chat.id, photo=open('Heroes//Weawer//second_buy.png', 'rb'))
            bot.send_message(message.chat.id,"Прокачивание скилов:")
            bot.send_photo(message.chat.id, photo=open('Heroes//Weawer//skills.png', 'rb'))
            bot.send_message(message.chat.id,"Враги:\n1.Bane\n2.Death Prophet\n3.Puck\n4.Night Stalker\n5.Silencer\n6.Beastmaster\n7.Dragon Knight\n8.Lone Druid\n9.Gyrocopter\n10.Viper\n11.Phantom Lancer\n12.Naga Siren\n13Terrorblade\n14.Chaos Knight\n15.Chen\n16.Lycan")
            bot.send_message(message.chat.id,"Cоюзники:\n1.Shadow Fiend\n2.Slardar\n3.Dazzle\n4.Templar Assassin\n5.Naga Siren\n6.Vengeful Spirit\n7.Ancient Apparition")

    bot.polling(none_stop = True)

if __name__ == "__main__":
    main()