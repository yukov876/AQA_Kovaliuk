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
    reverted_string = ""
    for char in my_string:
        reverted_string = char + reverted_string
    return reverted_string


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(my_words: list):
    which_word_is_longest = list(filter(lambda word: len(word) == (max(len(word) for word in my_words)), my_words))
    return which_word_is_longest


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    index = str1.find(str2)
    if index != -1:
        return index
    else:
        return -1


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
first_integer = int(input("Введіть, будь ласка, перше число: "))
second_integer = int(input("Введіть, будь ласка, друге число: "))


def sum_two_integers(first_integer: int, second_integer: int):
    sum = first_integer + second_integer
    return sum


print(f"Сума чисел {first_integer} та {second_integer} становить {sum_two_integers(first_integer, second_integer)}")

# Task 8
my_string = input("Введіть, будь ласка, рядок: ")


def revert_string(my_string: str):
    reverted_string = ""
    for char in my_string:
        reverted_string = char + reverted_string
    return reverted_string


print(f"Ваш рядок, який перевернули буде виглядати - '{revert_string(my_string)}'.")

# Task 9
entered_words = input("Введіть, будь ласка, декілька слів, розділяючи їх комою: ")
my_words = entered_words.split(',')


def longest_word(my_words: list):
    which_word_is_longest = list(filter(lambda word: len(word) == (max(len(word) for word in my_words)), my_words))
    return which_word_is_longest


print(f"Найдовше слово з введених Вами - '{longest_word(my_words)}.")

# Task 10
str1 = input("Введіть, будь ласка, перший рядок: ")
str2 = input("Введіть, будь ласка, другий рядок: ")


def find_substring(str1, str2):
    index = str1.find(str2)
    if index != -1:
        return index
    else:
        return -1


result = find_substring(str1, str2)
if result != -1:
    print(f"Ваш другий рядок '{str2}' починається у першому '{str1}' з {result + 1} знака.")
else:
    print(f"Ваш другий рядок '{str2}' не містить у першому '{str1}'.")
