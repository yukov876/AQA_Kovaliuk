adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer_t1 = adwentures_of_tom_sawer.replace("\n", " ")
print (adwentures_of_tom_sawer_t1)

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer_t2 = adwentures_of_tom_sawer_t1.replace("....", " ")
print (adwentures_of_tom_sawer_t2)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

import re

adwentures_of_tom_sawer_t3 = re.sub(r'\s+', ' ', adwentures_of_tom_sawer_t2)
print(adwentures_of_tom_sawer_t3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print ("Літера 'h' у тексті зустрічається", adwentures_of_tom_sawer_t3.count('h'), 'разів')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

big_letter = 0
for i in adwentures_of_tom_sawer_t3:
    if i.isupper():
        big_letter +=1
print("У тесті", big_letter, "слів починається з великої літери")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

word_to_find = "Tom"
index_1 = adwentures_of_tom_sawer_t3.find(word_to_find)
#sub_string = adwentures_of_tom_sawer_t3.[index_1:-1]
index_2 = adwentures_of_tom_sawer_t3.find(word_to_find, (index_1+1))
print("Вдруге слово 'Tom' зустрічається на", index_2, "позиції")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

split_times = adwentures_of_tom_sawer_t3.count('.')
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_t3.split('.', split_times-1)
#у завданні вказано лише зберегти, але я виведу для наглядності
print(adwentures_of_tom_sawer_sentences)



# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
print(fourth_sentence)
print(fourth_sentence.lower())



# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

find = 'By the time'
adwentures_of_tom_sawer_sentences_without_spaces = [i.strip() for i in adwentures_of_tom_sawer_sentences]
while i != i.startswith(find) in adwentures_of_tom_sawer_sentences_without_spaces:
    print("Це речення не починається на 'By the time'")
else:
    print("Речення, яке починається на 'By the tinme' присуєтнє в тексті")



# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1]
print("В останньому реченні", len(last_sentence.split()), "слів/ова")
