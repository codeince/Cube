# СВОЯ НАСТРОЙКА КУБА

Если вы хотели создать свою версию Куба, будь-то с ненормативной лексикой или более весёлыми ответами, то эта документация для вас

После создания ресурс-пака нужно изменить переменную в файле `src/__main__.py`, где написано **resource_pack = 'имя ресурс-пака'**

# Структура Ресурс-пака

Ресурс-пак должен содержать следующие файлы:

1. Языковой(`/langs/язык.json`): там описывается основное представление действий в Шаре
2. Ответный(`/langs/answer_files/answers_язык.json`): там находится справочник Куба, где расписано всё то, как и на что Шар должен реагировать

# Языковой Файл

Пока языковой файл имеет не так уж и много настроек, но имеются следующие:

1. "lang": язык файла

2. "text": настройки отображения текста:

    1. "init_text": текст, что пишется при запуске модели

    2. "answer_formatting": формат текста

        {answer} - ответ

        {question}" - вопрос пользователя

    3. "type_text": текст при вводе вопроса к Шару

    4. "model_text": формат отображения модели Куба

        {seed} - текущая "личность"

    5. "custom_model_text": формат отображения текста для выбора своей модели

    6. "stop_words": слова для остановки Куба

    7. "war_and_piece_warning": текст, который покажется, если длина вопроса равна или длиннее, чем "war_and_piece_warning_len"

# Ответный Файл

Что логично, в этом файле ооочень много разных настроек, ну,  групп:

1. "lang": язык файла

2. "answers": группы ответов
    добавляйте группу default по стандарту

    "тестовая группа ответов": группа ответов по-английски

        1. "masks": фрагменты текста в вопросе пользователя для определения текущей группы(первую маску лучше сделать названием группы на текущем языке с "#")

        2. "answers": ответы на вопросы группы
        
            %rand% для генерации в этом месте рандомного числа

# И помните...
Если что-то не понятно, то пишите мне
