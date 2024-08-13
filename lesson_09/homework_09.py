# function 01
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""


def total_trees(apples):
    pears = apples + 5
    plumps = apples - 2
    return apples + pears + plumps


# function 02
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""


def total_books_sum(book_first):
    book_second = book_first + 2
    book_third = (book_first + book_second) / 2
    return book_first + book_second + book_third


# function 03
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def revert_string(my_string: str):
    return ''.join(reversed(my_string))


# function 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""


def sum_squares(s_black_sea, s_azov_sea):
    return s_black_sea + s_azov_sea


# function 05
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""


def computer_price(period_payment, monthly_payment):
    return monthly_payment * period_payment

