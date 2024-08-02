# Task 6.1

proposed_srirng: str = input("Please, provide your string: ")
uniq_counter: int = sum(1 for char in proposed_srirng if proposed_srirng.count(char) == 1)

if uniq_counter > 10:
    print(True)
else:
    print(False)


# Task 6.2

is_correct_word: bool = False

while not is_correct_word:
    provided_word: str = input("Please, provide word, which contain letter 'h' or 'H': ").lower()

    if provided_word.find('h') != -1:
        is_correct_word = True
        print("Your word contain letter 'h' or 'H'.")
    else:
        print("Your word doesn't contain letter 'h' or 'H', please try again.")


# Task 6.3

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

desired_list: list[str] = [element for element in lst1 if isinstance(element, str)]

print(desired_list)


# Task 6.4

provided_list: list[int] = [10, 5, 6, 17, 4, 19, 20]
result: int = sum([integer for integer in provided_list if integer % 2 == 0])
print(f"Сума усіх парних чисел, у заданому переліку = {result}.")



