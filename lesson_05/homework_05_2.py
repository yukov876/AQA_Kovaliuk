# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

age_barier = 30

people_records.insert(0, ('Alex', 'Park', 37, 'Bussines Analyst', 'New York'))
print("Список з моїм записом на самому початку:", people_records)

people_records.insert(1, people_records.pop(5))
people_records.insert(5, people_records.pop(2))
print("У попередньому списку записи 2 та 6 змінено місцями", people_records)

if ((people_records[6])[2] >= age_barier) and ((people_records[10])[2] >= age_barier) and ((people_records[13])[2] >= age_barier):
    print(f'У людей зі списку під номером 7, 11 та 14 вік більше або рівний {age_barier}')
else:
    print(f'У людей зі списку під номером 7, 11 та 14 вік НЕ більше або рівний {age_barier}')

#для користувача індекси не мають значення, тому я вивела текстом порядковість у списку, який він бачить

