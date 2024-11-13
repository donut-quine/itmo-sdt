import math


def area(r: float) -> float:
    """Рассчитывает площадь окружности из её радиуса.

    :param r: Радиус окружности
    :return: Площадь окружности
    """

    return math.pi * r * r


def perimeter(r: float) -> float:
    """Рассчитывает периметр окружности из её радиуса.

    :param r: Радиус окружности
    :return: Периметр окружности
    """

    return 2 * math.pi * r

