print("Hello, this is a file for git repository")

print("These are new local changes")


def func(var_1: int) -> None:
    pass


def some_function(number: int | float) -> None:
    pass


def another_some_function(number: int | float | complex = 0) -> None:
    pass


# Пример 4. Функция get_tuple принимает список, в котором могут быть вещественные числа и/или булевы значения, а возвращает кортеж целых чисел.
def get_tuple(lst: list[float | bool]) -> tuple[int]:
    return (int(num) for num in lst)


# Пример 5. Функция do_something принимает словарь, ключами в котором являются целые числа, а значениями либо строки, либо булевы значения. Возвращает None.
def do_something(arg: dict[int, str | bool]) -> None:
    pass

