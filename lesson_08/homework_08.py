def sum_all_chars_in_string_if_int(test_list: list[str]) -> None:
    result: list[int] = list()
    try:
        for item in test_list:
            chars_list: list = item.split(",")
            result.append(sum(int(integer) for integer in chars_list))
    except ValueError as exception:
        print(f"I cann't sum your items in list due to: {exception}")
    else:
        print(result)

