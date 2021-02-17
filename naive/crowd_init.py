from numpy import array, random
import numpy as np
from naive.constants import WINDOW, CROWD


def array_is_outside_screen(array_coordinates):
    if not array_coordinates[0] in range(
        0, WINDOW.int_width_crowds_screen
    ) or not array_coordinates[1] in range(0, WINDOW.int_height_crowds_screen):
        return True
    else:
        return False


def array_is_into_a_wall(array_coordinates):
    for i in range(0, len(WINDOW.dict_dict_walls_coordinates)):
        if array_coordinates[0] in range(
            WINDOW.dict_dict_walls_coordinates[i]["point1"][0],
            WINDOW.dict_dict_walls_coordinates[i]["point2"][0],
        ) and array_coordinates[1] in range(
            WINDOW.dict_dict_walls_coordinates[i]["point1"][1],
            WINDOW.dict_dict_walls_coordinates[i]["point2"][1],
        ):
            return True
    return False


def set_already_contain_latter_array(set_of_points, array_coordinates):
    for i in range(0, len(set_of_points)):
        if np.array_equal(set_of_points[i], array_coordinates):
            return True
    return False


def point_location_available(set_of_points, array_coordinates):
    if array_is_outside_screen(array_coordinates):
        return False

    if array_is_into_a_wall(array_coordinates):
        return False

    if set_already_contain_latter_array(set_of_points, array_coordinates):
        return False

    return True


def init_a_new_valid_point(set_of_points):
    while True:
        new_point = array(
            [
                random.randint(0, WINDOW.int_width_crowds_screen),
                random.randint(0, WINDOW.int_height_crowds_screen),
            ]
        )
        if point_location_available(set_of_points, new_point):
            break
    set_of_points.append(new_point)
    return set_of_points


def create_set_of_valid_points():
    set_of_points = []
    for i in range(0, CROWD.int_number_individuals_in_crowd):
        set_of_points = init_a_new_valid_point(set_of_points)
    return set_of_points
