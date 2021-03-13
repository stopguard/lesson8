r"""
Написать декоратор с аргументом-функцией (callback),
    позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
        def val_checker...
            ...


        @val_checker(lambda x: x > 0)
        def calc_cube(x):
           return x ** 3


        >> a = calc_cube(5)
        125
        >> a = calc_cube(-5)
        Traceback (most recent call last):
            ...
            raise ValueError(msg)
        ValueError: wrong val -5
    замаскировать работу декоратора
"""
import re


def val_checker(verify):
    """Сравнение с нулём"""
    def _cube(func):
        """Получаем функцию"""
        def cube(number):
            """Получаем аргументы и вызываем декорируемую функцию"""
            print(f'Возводим в куб число: {number}')        # выводим последствия работы регулярки
            if not verify(number):                              # если число не больше нуля
                raise ValueError(f'wrong val {number}')             # вызываем исключение
            return func(number)                                 # возвращаем результат работы калк_куба
        return cube
    return _cube


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Вычисляем куб числа"""
    return x ** 3


_value = int(''.join(re.findall(r'[-+]?[0-9]+',
                                input('Введите положительное число для возведения в куб'
                                      '(лишние символы будут удалены): '))[0]))  # получаем число и фильтруем от мусора
result = calc_cube(_value)          # получаем результат
print(f'{_value}^3 = {result}')     # выводим
