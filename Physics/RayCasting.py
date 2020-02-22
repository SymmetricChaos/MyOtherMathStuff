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


def close_enough(coord_a: tuple, coord_b: tuple, distance: float):
    """
    Calculate distance between two segment in 2D space and find if distance
    is less than minimum distance.
    :param coord_a: tuple -- (x, y) coords of first point
    :param coord_b: tuple -- (x, y) coords of second point
    :param distance_: float -- minimal distance to check against
    :return: bool -- if distance is less than
    """
    return distance(coord_a, coord_b) <= distance