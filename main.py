# ------------------------------------------------------------------------------------------------------
# 1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список,
# содержащий только уникальные элементы из исходного списка.
# ------------------------------------------------------------------------------------------------------


# Можно реализовать по простому,через конвертацию список во множество, а потом обратно в сисок.
def get_only_unique(numbers: list[int]) -> list[int]:
    return list(set(numbers))


# Можно через перебор всех элементов в исходном списке с проверкой нахождения элемента в ответе.
def get_only_unique(numbers: list[int]) -> list[int]:
    result = []
    for element in numbers:
        if not element in result:
            result.append(element)
    return result


# ------------------------------------------------------------------------------------------------------
# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
# и возвращает список всех простых чисел в заданном диапазоне.
# ------------------------------------------------------------------------------------------------------


def get_primes(min_number: int, max_number: int) -> list[int]:
    """
    Обычное решето Эратосфена с дополнением.

    Да, считаем много лишнего, но все равно быстро.
    """
    primes = [True] * (max_number + 1)
    primes[0], primes[1] = False, False
    for i in range(2, max_number):
        if primes[i]:
            for j in range(i * i, max_number + 1, i):
                primes[j] = False

    primes = ([False] * min_number) + primes[min_number:]
    return [i for i in range(max_number + 1) if primes[i]]


# ------------------------------------------------------------------------------------------------------
# 3. Создать класс Point, который представляет собой точку в двумерном пространстве.
# Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки,
# а также для получения и изменения координат.
# ------------------------------------------------------------------------------------------------------


class Point:
    """
    Представляет точку в двухмерном пространстве с координатами x и y
    """

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """
        Инициализируем класс и задаем значения координат.

        Сеттеры и геттеры уже работают.
        """
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        """
        Возвращает значение координаты x точки
        """
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        """
        Устанавливает новое значение координаты x точки
        """
        self._x = x

    @property
    def y(self) -> int:
        """
        Возвращает значение координаты y точки
        """
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        """
        Устанавливает новое значение координаты y точки
        """
        self._y = y

    def get_distance(self, point: "Point") -> int | float:
        """
        Возвражает растояние до другой точки
        """
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5


# Проверки оставлю на всякий случай.
point1 = Point()
assert point1.x == 0
assert point1.y == 0
point1.x = -(1)
point1.y = 3
assert point1.x == -1
assert point1._x == -1
assert point1.y == 3
assert point1._y == 3

point2 = Point(6, 2)
assert point2.x == 6
assert point2.y == 2

print(point1.get_distance(point2))  # Тут получается пять квадратных корней из 2


# ------------------------------------------------------------------------------------------------------
# 4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
# ------------------------------------------------------------------------------------------------------

list_of_strings = ["строк", "лист", "Это"]

print(sorted(list_of_strings, key=lambda x: len(x)))
print(sorted(list_of_strings, key=lambda x: len(x), reverse=True))

# Или можно через метод списка, если сохранение изначального порядка элементов не имеет значения.
list_of_strings.sort(key=lambda x: len(x))
print(list_of_strings)

list_of_strings.sort(key=lambda x: len(x), reverse=True)
print(list_of_strings)
