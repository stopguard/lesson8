r"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
        def type_logger...
        ...


        @type_logger
        def calc_cube(x):
           return x ** 3


        >> a = calc_cube(5)
        5: <class 'int'>
    если аргументов несколько - выводить данные о каждом через запятую
    вывести тип значения функции
    решить задачу для именованных аргументов
    замаскировать работу декоратора
    вывести имя функции, например, в виде:
        >> a = calc_cube(5)
        calc_cube(5: <class 'int'>)
"""
from functools import wraps


def function_for_function(func):
    """Внутренний декоратор"""
    @wraps(func)                                    # маскируем декоратор
    def _fff(*args, **kwargs):
        """Функция ради функции. Вызывает декорируемую функцию"""
        return func(*args, **kwargs)
    return _fff


def type_logger(func):
    """Внешний декоратор"""
    def _logger(*args, **kwargs):
        """Проверялка типов ввода"""
        print(f'Аргументы функции:\t\t\t', end='')
        print(*map((lambda i: f'{i}: {type(i)}'), args),
              *map((lambda i: f'{i[0]}={i[1]}: {type(i[1])}'), kwargs.items()), sep=', ')  # выводим аргументы и их типы
        result = func(*args, **kwargs)                                                   # вызываем внутренний декоратор
        print(f'Имя функции и переменная:\t{func.__name__}({args[0]}: {type(args[0])})')     # выводим данные по функции
        return result
    return _logger


@type_logger
@function_for_function
def calc_cube(*args, **kwargs):
    """Вычисляет куб нулевого аргумента"""
    return args[0] ** 3


cube = calc_cube(6, '1', [1], a=15, s=(), d='f')                            # вычисляем куб числа 6
print(f'Результат работы функции:\t{cube}, тип результата: {type(cube)}.')  # выводим результат и его тип
