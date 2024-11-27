from .exceptions import NotPositiveLengthException, TriangleInequalityNotSatisfiedException


def area(a: float, h: float) -> float:
    """Рассчитывает площадь треугольника из высоты и стороны, на которую эта высота падает.

    :param a: Сторона, на которую падает высота
    :param h: Высота треугольника
    :return: Площадь треугольника
    """

    if a <= 0:
        raise NotPositiveLengthException(a)

    if h <= 0:
        raise NotPositiveLengthException(h)

    return a * h / 2


def perimeter(a: float, b: float, c: float) -> float:
    """Рассчитывает площадь треугольника, используя три стороны треугольника.

    :param a: 1ая сторона треугольника
    :param b: 2ая сторона треугольника
    :param c: 3ья сторона треугольника
    :return: Периметр треугольника
    """

    if a <= 0:
        raise NotPositiveLengthException(a)

    if b <= 0:
        raise NotPositiveLengthException(b)
    
    if c <= 0:
        raise NotPositiveLengthException(c)
    
    # Преобразованное неравенство треугольника
    if a + b + c <= 2 * max(a, b, c):
        raise TriangleInequalityNotSatisfiedException(f"Triangle inequality not satisfied. Side lengths: {a}, {b}, {c}")

    return a + b + c
