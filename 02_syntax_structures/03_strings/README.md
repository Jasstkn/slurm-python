Текстовый вариант видеоурока с предыдущего шага.

Привет. В этом уроке поговорим о строках, и их методах и что эти слова значат.

В предыдущих уроках мы работали с числами. Но как быть в ситуациях, когда наша программа должна работать, например, с именами? Для этого существует такой тип данных, как строки. Строки записываются в двойных или одинарных кавычках. Никакой разницы нет. Даже популярные линтеры - программы для проверки соответствия кода принятым стандартам - расходятся в этом вопросе. Единственное, что действительно важно - придерживаться одного стиля и не смешивать использование двойных и одинарных кавычек. Я лично предпочитаю двойные, потому что в других языках именно они используются для определения строки, а одинарные используются для типа данных “символ”. Но в Python такого типа данных нет. Строка даже из одного символа все равно строка.

Чтобы убедиться, давайте присвоим в переменную свое имя и профессию. В первом случае используем двойные кавычки, во втором одинарные:


```python
name = "Денис"
job = 'R&D разработчик'
```
А теперь мы захотели вывести на экран нашу профессию и имя. И все это одной строкой. Как это сделать? И здесь на помощь приходит так называемая склейка строк. Хотя научнее называть эту операцию конкатенацией, но звучит как-то сложно. Конкатенации соответствует оператор “+”. И снова интерпретатор сам угадывает что именно нужно сделать, исходя из типов данных. Собственно за этим они и нужны в нетипизированном языке - чтобы мы могли явно сообщать о своих намерениях, а интерпретатор делал то, что хотим мы, а не то, что вздумается. Давайте пробовать.


```python
print(job + name)
```
Склеилось в прямом смысле. Слова слепились друг с другом. Выглядит не очень солидно. Можно было бы дописать пробелы в объявлении переменных, но что если в следующей строке нам понадобится поменять переменные местами и вывести результат? Давайте попробуем решить эту проблему вводом в выражение еще одной строки.

```python
print(job + " " + name)
```

Выглядит намного лучше. А так как строки, как и числа являются неизменяемым типом данных, поэтому такие операции ничем не угрожают исходным значениям. Давайте введем еще одну переменную с нашей почтой.

```python
email = "d.naumov@slurm.io"
```
И распечатаем строку “Меня зовут <имя>, я <профессия>, связаться со мной можно через почту <email>”.

Желание распечатывать такую строку сразу отпадает так как придется использовать несколько склеек. К счастью в Python есть методы строк - встроенные в тип данных функции, которые реализуют самые частые операции над строками. Одна из таких операций как раз интерполяция и форматированный вывод. Интерполяцией называется встраивание переменных в строку. Рассмотрим как она выглядит.
```python
print("Меня зовут {}, я {}, связаться со мной можно через почту {}".format(name, job, email))
```
Мы обозначили фигурными скобками места для встраивания переменных, а сами переменные мы передали в аргументы методу строки format. Соответственно в первое место для встраивания был встроен первый по порядку аргумент, во второе - второй, в третье - третий. Можно хитрее: дать местам для встривания и аргументам имена.
```python
print("Меня зовут {job_var}, я {email}, связаться со мной можно через почту {name_var}".format(name_var=name, job_var=job, email=email))
```
Интерпретатор соотнесет их и встроит в нужные места вне зависимости от порядка следования аргументов. Они могут совпадать с переменной, а могут и не совпадать - все как вы решите. Я предпочитаю, чтобы совпадали. Почему не возникает конфликтов имен мы рассмотрим в лекции о функциях. Она будет уже в этом блоке.

Но вернемся к интерполяции. Если вы используете Python версии 3.6 или выше, то вам доступен еще более удобный синтаксис:

```python
print(f”Меня зовут {name}, я {job}, связаться со мной можно через почту {email}").
```
Все дело в букве f перед строкой: при её наличии интерпретатор понимает, что в фигурных скобках помещается код, а не символы строки. Соответственно, этот код будет выполнен, а все что вне скобок будет считаться символами строки. Эта конструкция так и называется f-string или f-строка, если использовать локализованную терминологию.

Появляется резонный вопрос: а как нам записать фигурную скобку как символ строки. Здесь все тоже несложно: нужно написать две одинаковых фигурных скобки подряд и первая будет экранировать другую. Возьмем для примера в скобки слово “почту” и специально перепутаем скобки местами, чтобы показать, что порядок здесь не имеет значения, а результат будет символом строки.
```python
print(f”Меня зовут {name}, я {job}, связаться со мной можно через }}почту{{ {email}").
```
С выводом разобрались, самое время решить бизнес-кейс. Нам нужно вывести все ту же строку, но с некоторыми ограничениями.

В качестве входных данных мы имеем следующие значения:
```python
name = "       ~~~денис~~     "
job = "R&D рAзРаБоТчИк"
email = "d.naumov@slurm.io"
```
По правилам русского языка, имя должно быть записано с большой буквы и без лишних символов в начале и конце. А заказчик требует, чтобы профессия была записана маленькими буквами, а в адресе электронной почты символ “@” должен быть заменен на предлог “at”.

Для начала декомпозируем кейс на подзадачи. Это хорошая практика в разработке, сразу становится видно с чего можно начать и какие ключевые точки необходимо пройти. В данном примере такая методология может казатсья притянутой за уши, но по мере приобретения опыта в разработке можно дробить задачи крупнее и получать те же бонусы.

Итак, запишем наши задачи в комментарии к коду:
```python
# TODO: Вывести строку с интерполированными переменными
# TODO: Убрать пробелы в начале и конце имени
# TODO: Убрать символы “~” в начале и конце имени
# TODO: Сделать первую букву имени заглавной
# TODO: Привести профессию к нижнему регистру
# TODO: Заменить в адресе электронной почты символ “@ на предлог “at”
```
Кстати, при такой записи, в PyCharm можно посмотреть список задач из кода.

Код для решения первой задачи у нас уже есть:

```python
print(f”Меня зовут {name}, я {job}, связаться со мной можно через почту {email}")
```
Уберем выполненный TODO-комментарий и перейдем к следующему. Пробелы в начале и конце строки вполне могут быть регулярным явлением. Например, данные из форм не всегда валидируются и могут приходить в весьма странных форматах. А мы уже знаем, что решать такие частые задачи помогают методы строк. И для этого случая в Python есть метод строки strip. Применим его.
```python
print(f"Меня зовут {name.strip()}, я {job}, связаться со мной можно через почту {email}")
```
Стало чуть лучше. Но как убрать не только пробелы, а еще и символ “~”? Все просто: метод strip может принимать в качеству аргумента строку, символы которой он будет убирать из начала и конца строки. Здесь нам помогут одинарные кавычки, так как двойные уже используются в объявлении основной строки

```python
print(f"Меня зовут {name.strip(' ~')}, я {job}, связаться со мной можно через почту {email}")
```
То, что надо. Если бы нам было нужно убрать ненужные символы только слева или только справа у метода strip есть вариации lstrip (от left strip) и rstrip (от right strip).

А еще мы поняли, что как метод `strip` работает, и что в качестве результата применения он возвращает также строку. Это значит, что к полученному результату можно применить еще один метод строки. Такой подход называется чейнингом или цепочками методов.

Управление регистром - тоже частая задача. А это значит, что и для нее наверняка есть свой метод строки. И это правда, для этого служат такие методы как upper, lower, capitalize, swapcase и title.

`upper` приводит символы строки к заглавным
`lower` приводит символы строки к строчным
`capitalize` делает первую букву строки заглавной
`swapcase` меняет регистр на противоположный
`title` приводит первую букву каждого слова в верхний регистр, а все остальные в нижний
Кажется, что в имени нам нужен метод `capitalize`.

```python
print(f"Меня зовут {name.strip(' ~').capitalize()}, я {job}, связаться со мной можно через почту {email}")
```
Убираем TODO, и сразу же делаем следующий. Здесь кажется применимым метод lower.

```python
print(f"Меня зовут {name.strip(' ~').capitalize()}, я {job.lower()}, связаться со мной можно через почту {email}")
```
И последняя TODO: Заменить в адресе электронной почты символ “@ на предлог “at”. Что может быть более регулярным при работе со строками, чем замена одной части на другую? И реализует эту возможность метод replace. В качестве первого параметра он принимает подстроку, которая будет заменена в исходной строке. В качестве второго - строку, на которую будет заменена подстрока в исходной строка. А в качестве третьего - максимальное количество замен, по умолчанию метод заменяет все вхождения.

Нам нужно заменить  символ “@ на предлог “at”. Вспомним самое начало урока и то, что нам приходилось расставлять пробелы, с предлогом наверняка будет то же самое. Давайте сразу укажем пробелы слева и справа от предлога. В конечном счете все выглядит так:

```python
print(f"Меня зовут {name.strip(' ~').capitalize()}, я {job.lower()}, связаться со мной можно через почту {email.replace(‘@’ , ‘ at ‘)}")
```
А теперь давайте выведем исходные переменные

```python
print(name)
print(job)
print(email)
```
Видно, что методы строк также не нарушают принципа неизменяемости строк.

А наше последнее TODO убрано, кейс решен, на этом видео подходит к концу, это значит, что мы увидимся в видео о срезах строк.