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
side_first = 1
side_second = 2
side_third = 3
side_fourth = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side_first + side_second + side_third + side_fourth
print("Периметр становить", perimeter)


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
apples = 4
pears = apples + 5
plumps = apples - 2
total_trees = apples + pears + plumps
print("Всього в саду посадили", total_trees, "дерев")


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_morning = 5
temp_afternoon = temp_morning - 10
temp_evening = temp_afternoon + 4
print ("Надвечір температура повітря становила", temp_evening, "градусів")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys/2
boys_today = boys - 1
girls_today = girls - 2
total_today = boys_today + girls_today
print ("Сьогодні на театрольному гуртку було", int(total_today), "дітей")


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_first = 8
book_second = book_first + 2
book_third = (book_first + book_second)/2
total_sum = book_first + book_second + book_third
print("Якщо купити по одному примірнику книг, то коштувати вони будуть", total_sum, "грн.")
