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


def calculate_angle(start: tuple, end: tuple):
    """
    Calculate angle in direction from 'start' to the 'end' point in degrees.
    :param start: tuple -- start point coordinates (x, y)
    :param end: tuple -- end point coordinates (x, y)
    :return: float -- degrees in range 0-360.
    """
    radians = -math.atan2(end[0] - start[0], end[1] - start[1])
    return math.degrees(radians) % 360


def quadrant(coordinates: tuple, center: tuple):
    """
    Check in which quadrant coordinates lie counted from upper-left to
    bottom-left (clockwise). Quadrants are placed by setting center point
    coordinate.
    :param coordinates: tuple -- coordinates of a point in format (x, y)
    :param center: tuple -- coordinates of center point of polygon
    :return: str -- name of quadrant ('UL', "UR', 'LL', "LR')
    """
    angle = calculate_angle(center, coordinates)
    if angle =< 90:
        return "LL"
    if angle =< 180:
        return "UL"
    if angle =< 270:
        return "UR"
    return "LR"