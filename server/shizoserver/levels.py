from prompt_toolkit.styles import Style

levels_style = Style.from_dict({
    'code': 'bg:black bold',
    'keyword': 'fg:orange'
})

LEVELS = [
    {
        'name': 'circus',
        'visible': 'Волк слабее робота, но в цирке не выступает',
        'description': (
            "<b>- Привет, ты тут новенький?</b>\n"
            "<b>Я Ю. Дитский, приятно познакомиться.</b>\n"
            "<b>Очень удачно, что ты появился именно сейчас.</b>\n"
            "<b>Мне нужна твоя помощь. Сегодня на международный робототехнический</b>\n"
            "<b>форум в <u>Колково</u> приедет наш верховный лидер,</b>\n"
            "<b>а актёр, что должен был играть робота,</b>\n"
            "<b>слёг на больничный. Запрогаешь робота?</b>\n"
            "<b>Вот, кстати, записка от организаторов:</b>"
            "Задача твоей первой миссии - Проехать по кругу\n"
            "Для этого тебе понадобится написать код для твоего робота\n"
            "Роботы программируются на <b><u>ShizoSkript'е</u></b> однако он очень похож на <b><u>Pascal</u></b>\n"
            "Любая программа начинается с ее названия. Для этого используется фраза\n"
            "program имяПрограммы;\n"
            "Точка с запятой очень важна, т.к. она разделяет команды\n"
            "Далее ты должен указать роботу, какие модули следует использовать.\n" 
            "В первой задаче нам нужны только ноги для передвижения.\n"
            "Для подключения модулей пиши: "
            "<code><keyword>use</keyword> Модуль;</code>\n"
            "К примеру: "
            "<code><keyword>use</keyword> legs;</code>\n"
            "Затем, после того, как ты описал программу, \n"
            "следует указать начало действий, для этого можно использовать команду "
            "<code><keyword>begin</keyword></code>\n"
            "Точка с запятой здесь не нужна\n"
            "Чтобы управлять роботом есть ряд команд:\n"
            "<code>up();</code>, "
            "<code>right();</code>, "
            "<code>left();</code>, "
            "<code>down();</code>.\n"
            "Я думаю, что ты поймёшь, какая команда за что отвечает\n"
            "Вот еще несколько советов:\n"
            "В последней команде точка с запятой также не нужна. "
            "Программу нужно заканчивать командой "
            "<code><keyword>end</keyword>.</code>\n"
            "Точка после <code><keyword> end </keyword></code> тоже нужна\n"
            "Теперь попробуй что-нибудь написать.\n"
            "Если что-то пойдет не так - ты всегда можешь открыть эту справочку. Удачи)"
        )
    }
]
