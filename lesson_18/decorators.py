import functools


def logging_args_and_results(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Виклик функції '{func.__name__}' з аргументами: {args} та ключовими аргументами: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Результат функції '{func.__name__}': {result}")

        return result

    return wrapper


def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка при виконанні функції '{func.__name__}': {e}")
            return None

    return wrapper
