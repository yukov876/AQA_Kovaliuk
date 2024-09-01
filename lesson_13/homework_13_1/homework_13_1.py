
with open('result_kovaliuk.csv', 'w') as response_file:
    with open('rmc.csv') as csvfile1:
        row_from_first_file = set(csvfile1.readlines())

    with open('r-m-c.csv') as csvfile2:
        row_from_second_file = set(csvfile2.readlines())

    dif_lines = row_from_first_file.difference(row_from_second_file)

    for line in dif_lines:
        response_file.write(line)


