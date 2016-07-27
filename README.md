# morph

##Общее описание
Смысл решения проблемы состоит в том, что мы находим в предварительно составленном словаре наше слово, и определяем его начальную форму. Словарь можно не составлять каждый раз, но такой функционал предусмотрен. Чтобы поиск не занимал слишком много времени, к словарю составляется индекс - указатель по первым двум буквам. И словарь, и индекс хранятся в формате ``csv``.

Морфологическая нормализация текста производится с помощью функции ``morphNorm`` из файла ``main.py``.

Функция принимает на вход три параметра: ``text`` - текст, который нужно нормализовать, ``dictSource`` и ``indexSource``. Последние два аргумента - это имена файлов со словарём и его индексом. 

##Составления словаря и индекса
Словарь составляется из двух файлов - изначального словаря начальных форм (файл ``ru_RU_1251_UTF8.dic``) файла с таблицой аффиксов (``ru_RU_1251_UTF8.aff``).

Таблица аффиксов определяет правила, по которым из начальных форм слов из словаря строятся все остальные формы. Она состоит из строчек вида
```
SFX I ка к [аеиоуыюя]ка
```
Здесь ``SFX`` - служебное слово, `I` - код, `ка` - подстрока, которую нужно удалить (если ничего удалять не нужно, то стоит `0`), `к` - подстрока, которую нужно добавить вместо удалённой (если ничего не нужно добавлять, то стоит `0`), `[аеиоуыюя]ка` - шаблон строки.

Шаблон строки устроен так: вначале стоит (или не стоит) последовательность букв в квадратных скобках, возможно предварённая символом ``^``. Затем идёт ещё последовательность букв.

Чтобы приенить аффикс к слову, нужно проверить, подходит ли слово под шаблон, и если да, то удалить то, что нужно удалить и добавить то, что нужно добавить. 

Словарь начальных форм содержит начальные формы слов, после которых идёт `/` и последовательность заглавных латинских букв - кодов. 

Составление большого словаря происходит так: мы идём по словар начальных форм, и применяем к каждому слову все аффиксы с подходящими кодами (если подходит шаблон). В большой словарь мы записываем словоформу и начальную форму. Всё это отправляется в файл `csv`. Параллельно составляем индекс по первым двум буквам, в котором каждой комбинации из двух букв соответствует номер первого вхождения слова с таким началом в большой словарь.

##Слабые места
Большой словарь надо ещё отсортировать по первым двум буквам, иначе могут произойти проблемы. Например, у слова `гнать` есть форма `гонит`, которая будет записана в индексе как первое вхождение `го`. В результате все слова на `го` будут искаться в этом месте, и это неправильно.

##Пример работы
Вход:
```
Аня с Леной приглядывали за хорошенькими собачками и смеялись
```
выход
```
Аня с Лена приглядывать за хорошенький собачка и смеяться
```

