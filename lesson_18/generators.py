def my_generator(n):
    digit = 2

    while digit < n:
        if digit % 2 == 0:
            yield digit

        digit += 1


for value in my_generator(13):
    print(value)


def fibonacci_generator(n):
    a, b = 0, 1
    while b < n:
        yield a
        a, b = b, a + b


for valueN in fibonacci_generator(11):
    print(valueN)
