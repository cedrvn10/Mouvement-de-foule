from numpy import random

from constants import WINDOW, CROWD


def array_is_outside_screen(array_coordinates):
    if not array_coordinates[0] in range(0, WINDOW.width_crowds_screen) or \
            not array_coordinates[1] in range(0, WINDOW.height_crowds_screen):
        return True
    else:
        return False


def tuple_is_into_a_wall(array_coordinates):
    for i in range(0, len(WINDOW.walls_coordinates)):
        if array_coordinates[0] in range(WINDOW.walls_coordinates[i]['point1'][0],
                                         WINDOW.walls_coordinates[i]['point2'][0]) and \
                array_coordinates[1] in range(WINDOW.walls_coordinates[i]['point1'][1],
                                              WINDOW.walls_coordinates[i]['point2'][1]):
            return True
    return False


def bool_point_location_available(set_of_points, tuple_coordinates):
    if not tuple_coordinates[0] in range(0, WINDOW.width_crowds_screen) or \
            not tuple_coordinates[1] in range(0, WINDOW.height_crowds_screen):
        return False

    if tuple_is_into_a_wall(tuple_coordinates):
        return False

    if tuple_coordinates in set_of_points:
        return False

    return True


def init_a_new_valid_point(set_of_points):
    while True:
        new_point = tuple([random.randint(0, WINDOW.width_crowds_screen),
                           random.randint(0, WINDOW.height_crowds_screen)])
        if bool_point_location_available(set_of_points, new_point):
            break
    set_of_points.add(new_point)
    return set_of_points


def create_set_of_valid_points():
    set_of_points = set()
    for i in range(0, CROWD.number_individuals_in_crowd):
        set_of_points = init_a_new_valid_point(set_of_points)
    return set_of_points
