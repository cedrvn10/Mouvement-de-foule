from numpy import array, random
import numpy as np
from constants import WINDOW, CROWD


def tuple_which_are_coordinates_of_rectangle_containing_array(array_to_locate_in_grid):
    return np.floor(array_to_locate_in_grid[0] / WINDOW.width_crowds_screen * WINDOW.number_subdivision_x_axis), \
           np.floor(array_to_locate_in_grid[1] / WINDOW.height_crowds_screen * WINDOW.number_subdivision_y_axis)


def tuple_in_border_of_rectangle(array_location):
    tuple_axis_point = tuple_which_are_coordinates_of_rectangle_containing_array(array_location)
    return int(tuple_axis_point[0]) == tuple_axis_point[0] and int(tuple_axis_point[1]) == tuple_axis_point[1]


def array_is_outside_screen(array_coordinates):  # (?)
    if not array_coordinates[0] in range(0, WINDOW.width_crowds_screen) or \
            not array_coordinates[1] in range(0, WINDOW.height_crowds_screen):
        return True
    else:
        return False


def array_is_into_a_wall(array_coordinates):  # (?)
    int_number_walls = len(WINDOW.walls_coordinates)
    for i in range(0, int_number_walls):
        if array_coordinates[0] in range(WINDOW.walls_coordinates[i]['point1'][0],
                                         WINDOW.walls_coordinates[i]['point2'][0]) and \
                array_coordinates[1] in range(WINDOW.walls_coordinates[i]['point1'][1],
                                              WINDOW.walls_coordinates[i]['point2'][1]):
            return True
    return False


def set_already_contain_latter_array(set_of_points, array_coordinates):  # (?)
    int_len_set_of_points = len(set_of_points)
    for i in range(0, int_len_set_of_points):
        if np.array_equal(set_of_points[i], array_coordinates):
            return True
    return False


def array_point_location_available(set_of_points, array_coordinates):
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
            [random.randint(0, WINDOW.width_crowds_screen), random.randint(0, WINDOW.height_crowds_screen)])
        tuple = tuple_which_are_coordinates_of_rectangle_containing_array(new_point)
        if array_point_location_available(set_of_points, new_point):
            break
    set_of_points.append(new_point)
    return set_of_points


def create_set_of_valid_points():
    set_of_points = []
    int_number_individuals = CROWD.number_individuals_in_crowd
    for i in range(0, int_number_individuals):
        set_of_points = init_a_new_valid_point(set_of_points)
    return set_of_points
