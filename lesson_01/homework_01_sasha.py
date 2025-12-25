# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f'Perimeter is {perimetery}')


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print()
apples = 4
pears = apples + 5
plums = apples - 2
all_trees = apples + pears + plums
print(f'Яблунь {apples}, груш буде {apples} + 5 = {pears}, слив буде {apples} - 2 = {plums}')
print(f'Всього дерев {apples} + {pears} + {plums} = {all_trees}')

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print()
zero = 0
am_temperature = zero + 5
pm_temperature = am_temperature - 10
evening_temperature = pm_temperature + 4
print(f'Температура до обіду {am_temperature}')
print(f'Температура після обіду буде температура до обіду - 10 і дорівнює {pm_temperature}')
print(f'Температура надвечір буде температура після обіду + 4 тобто {pm_temperature} + 4 = {evening_temperature}')


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print()
boys_total = 24
girls_total = boys_total // 2
boys_today = boys_total - 1
girls_today = girls_total - 2
children_today = boys_today + girls_today
print(f'Хлопців взагалі {boys_total} а дівчаток в два рази меньше {boys_total} / 2 тобто {girls_total}')
print(f'Сьогодні прийшло хлопців {boys_total} - 1 тобто {boys_today}')
print(f'Сьогодні прийшло дівчаток {girls_total} - 2 тобто {girls_today}')
print(f'Всього сьогодні прийшло дітей {boys_today} + {girls_today} тобто {children_today}')

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print()
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) // 2
all_books = first_book + second_book + third_book
print(f'Перша книга коштує {first_book} грн. Друга книга {first_book} + 2 грн, тобто {second_book} грн')
print(f'Третя книга коштує {first_book} + {second_book} поділено на 2, тобто {third_book} грн')
print(f'Всі книги разои коштують {first_book} + {second_book} + {third_book} тобто {all_books}')


