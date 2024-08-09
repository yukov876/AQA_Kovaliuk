# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_two_integers(first_integer: int, second_integer: int):
    return first_integer + second_integer


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def avarage_of_integers(*args: int):
    return sum(args) / len(args)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def revert_string(my_string: str):
    return ''.join(reversed(my_string))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(my_words: list):
    return list(filter(lambda word: len(word) == (max(len(word) for word in my_words)), my_words))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    if str1.find(str2) == -1:
        return -1
    else:
        return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# Task7
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""


def sum_squares(s_black_sea, s_azov_sea):
    return f'Чорне та Азовське моря разом займають площу {s_black_sea + s_azov_sea} км2'


# Task 8
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""


def computer_price(period_payment, monthly_payment):
    return f"Вартість комп'ютера становить {monthly_payment * period_payment}грн."


# Task 9
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""


def reminder_from_devision(first_integer, second_integer):
    return f"Остача від ділення числа {first_integer} на число {second_integer} становить {first_integer % second_integer}"


# Task 10
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""


def calc_sheets(total_photos, photos_per_page):
    pages_needed = int(total_photos / photos_per_page)
    if total_photos % photos_per_page > 0:
        return f'Для вклеювання {total_photos} фотографій, Ігору знадобиться {pages_needed + 1} сторінок/ки в альбомі.'
    else:
        return f'Для вклеювання {total_photos} фотографій, Ігору знадобиться {pages_needed} сторінок/ки в альбомі.'
