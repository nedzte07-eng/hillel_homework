alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("\nЗадача 04")
azov_sea_area = 436402
balck_sea_area = 37800
print(f"Зазом площа двох морів буде {azov_sea_area + balck_sea_area} км2\nЦе сума полощі Азовського моря {azov_sea_area} км2 і Чорного моря {balck_sea_area} км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("\nЗадача 05")
full_amount = 375291
first_and_second_amount = 259449
second_and_third_amount = 222950

second_amount = first_and_second_amount + second_and_third_amount - full_amount
first_amount = first_and_second_amount - second_amount
third_amount = second_and_third_amount - second_amount

print(f"Знайдемо кількість товару на другому складі\n"
      f"Це буде від суми на першому та другому складах і на другому та третьому {first_and_second_amount + second_and_third_amount} відняти весь товар {full_amount}")

second_amount = first_and_second_amount + second_and_third_amount - full_amount

print( f"Тобто на другому складі буде {second_amount} товару")
print(f"Далі легко порахувати кількість товару для першого складу {first_amount}\n"
      f"Це різниця товару на першому та другому складах {first_and_second_amount} і на другому складі {second_amount}")
print(f"Так само на третьому складі {third_amount}\n"
      f"Це різниця товару на другому та третьому складах {second_and_third_amount} і на другому складі {second_amount} ")




# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("\nЗадача 06")
year_and_a_half = 18
price_per_month = 1179
full_price = year_and_a_half * price_per_month
print(f"Вартість комп\'ютера буде кількість місяців {year_and_a_half} помножено на місячний платіж {price_per_month},\n"
      f"тобто {full_price} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("\nЗадача 07")
a = 8019 % 8
b =9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"""Остача від ділення буде
a) {a}  d) {d}
b) {b}  e) {e}
c) {c}  f) {f}
""")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("\nЗадача 08")
big_pizza = (4, 274)
middle_pizza = (2, 218)
juice = (4, 35)
pie = (1, 350)
water = (3, 21)

full_big_pizza = big_pizza[0] * big_pizza[1]
full_middle_pizza = middle_pizza[0] * middle_pizza[1]
full_juice = juice[0] * juice[1]
full_pie = pie[0] * pie[1]
full_water = water[0] * water[1]

full_amount = full_big_pizza + full_middle_pizza + full_juice + full_pie + full_water


print(f"""Для того щоб порахувати кільки грошей знадобиться для Іринкиного замовлення
треба помножити кількість кожного пункту на його ціну і скласти для всіх пунктів
Піца велика {big_pizza[0]} * {big_pizza[1]} = {full_big_pizza}
Піца середня {middle_pizza[0]} * {middle_pizza[1]} = {full_middle_pizza}
Сік {juice[0]} * {juice[1]} = {full_juice}
Торт {pie[0]} * {pie[1]} = {full_pie}
Вода {water[0]} * {water[1]} = {full_water}
Загальна кількість грошей {full_big_pizza} + {full_middle_pizza} + {full_juice} + {full_pie} + {full_water} = {full_amount} грн
""")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("\nЗадача 09")
full_photo_amount = 232
page_photo_amount = 8
if full_photo_amount % page_photo_amount == 0:
    page_amount = full_photo_amount // page_photo_amount
else:
    page_amount = full_photo_amount // page_photo_amount + 1

print(f"Кількість сторінок альбому буде {page_amount}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("\nЗадача 10")
distance = 1600
fuel_consumption = 9
fuel_tank_capacity = 48

fuel_amount = (distance // 100) * fuel_consumption
number_of_fuel_stops = fuel_amount // fuel_tank_capacity

print(f"""Для подорожі з Харкова в Будапешт буде потрібно
({distance} / 100) * 9, тобто {fuel_amount} літрів бензину.
З цього можна вирахувати що потрібно {number_of_fuel_stops} що дорівнює {fuel_amount} літрів / {fuel_tank_capacity} літрів
""")


