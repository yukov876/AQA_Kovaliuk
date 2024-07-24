alice_in_wonderland = '''\'"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don\'t much care where ——" said Alice.\n
"Then it doesn\'t matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\''''
print (alice_in_wonderland)

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

a_black_sea = 436402
a_azov_sea = 37800
print (f'Чорне та Азовське моря разом займають площу {a_black_sea+a_azov_sea} км2')



# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items = 375291
first_and_second_storage = 250449
second_and_third_storage = 222950
first_storage = total_items - second_and_third_storage
second_storage = first_and_second_storage - first_storage
third_storage = total_items - first_and_second_storage
print(f'''На першому складі знаходиться {first_storage} товарів,
на другому склад знаходиться {second_storage} товарів,
на третьому складі знаходиться {third_storage} товарів.''')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
period_payment = 18
print (f"Вартість комп'ютера становить {monthly_payment*period_payment}грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f'''Остача від ділення в дії а) 8019 : 8 становить {8019%8}
остача від ділення в дії b) 9907 : 9 становить {9907%9}
остача від ділення в дії c) 2789 : 5 становить {2789%5}
остача від ділення в дії d) 7248 : 6 становить {7248%6}
остача від ділення в дії e) 7128 : 5 становить {7128%5}
остача від ділення в дії f) 19224 : 9 становить {19224%9}''')

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
pizza_big_quantity = 4
pizza_big_price = 274
pizza_middle_quantity = 2
pizza_middle_price = 218
juice_quantity = 4
juice_price = 35
cake_quantity = 1
cake_price = 350
water_quantity = 3
water_price = 21
print(f'Для замовлення Іринки на день народження потрібно {(pizza_big_quantity * pizza_big_price)+
                                                          (pizza_middle_quantity * pizza_middle_price)+
                                                          (juice_quantity * juice_price)+
                                                          (cake_quantity*cake_price)+
                                                          (water_quantity * water_price)}грн.')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8
pages_needed = int(total_photos / photos_per_page)
if total_photos % photos_per_page > 0:
    print (f'Для вклеювання {total_photos} фотографій, Ігору знадобиться {pages_needed+1} сторінок в альбомі.')
else:
    print (f'Для вклеювання {total_photos} фотографій, Ігору знадобиться {pages_needed} сторінок в альбомі.')


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
distance = 1600
gasoline_consumption = 9
tank_capacity = 48
gasoline_needed = (distance/100)*gasoline_consumption
station_visitings = int(gasoline_needed / tank_capacity)
print (f'Для подорожі з Харкова у Будапешт родині знадобиться {gasoline_needed} літри/ів бензину')
if gasoline_needed % tank_capacity > 0:
    print (f'Для подорожі з Харкова у Будапешт родині необхідно буде заїхати на заправну станцію {station_visitings+1} рази/ів, щоразу заправляючи повний бак.')
else:
    print (f'Для подорожі з Харкова у Будапешт родині необхідно буде заїхати на заправну станцію {station_visitings} рази/ів, щоразу заправляючи повний бак.')