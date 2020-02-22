# https://github.com/akapkotel/light_raycasting/blob/master/geometry.py

import math


def distance(coord_a: tuple or list, coord_b: tuple or list):
    """
    Calculate distance between two ponits in 2D space.
    :param coord_a: tuple -- (x, y) coords of first point
    :param coord_b: tuple -- (x, y) coords of second p
    :return: float -- 2-dimensional distance between points
    """
    return math.hypot(coord_b[0] - coord_a[0], coord_b[1] - coord_a[1])


def is_close(coord_a: tuple, coord_b: tuple, mindist: float):
    """
    Calculate distance between two segment in 2D space and find if distance
    is less than minimum distance.
    :param coord_a: tuple -- (x, y) coords of first point
    :param coord_b: tuple -- (x, y) coords of second point
    :param mindist: float -- minimal distance to check against
    :return: bool -- if distance is less than
    """
    return distance(coord_a, coord_b) <= mindist


def polar_to_cart(angle: float, scalar: float):
    """
    Convert polar coordinates with cartesian coordinates
    :param angle: float -- angle of the vector
    :param scalar: float -- scalar value of the vector (e.g. speed)
    :return: tuple -- x and y parts of the vector in format: (float, float)
    """
    radians = math.radians(angle)
    change_y = math.cos(radians)
    change_x = math.sin(radians)
    return change_x * scalar, change_y * scalar