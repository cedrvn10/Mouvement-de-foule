from numpy import array, random
import numpy as np
from constants import WINDOW, CROWD


def tuple_which_are_coordinates_of_rectangle_containing_array(array_to_locate_in_grid):
    return (
        int(
            np.floor(
                array_to_locate_in_grid[0]
                / WINDOW.width_crowds_screen
                * WINDOW.number_subdivision_x_axis
            )
        ),
        int(
            np.floor(
                array_to_locate_in_grid[1]
                / WINDOW.height_crowds_screen
                * WINDOW.number_subdivision_y_axis
            )
        ),
    )


def bool_in_border_of_rectangle(array_location):
    tuple_axis_point = tuple_which_are_coordinates_of_rectangle_containing_array(
        array_location
    )
    return (
        array_location[0]
        / WINDOW.width_crowds_screen
        * WINDOW.number_subdivision_x_axis
        == tuple_axis_point[0]
        and tuple_axis_point[1]
        == array_location[1]
        / WINDOW.width_crowds_screen
        * WINDOW.number_subdivision_x_axis
    )


def array_is_into_a_wall(array_coordinates):  # (?)
    int_number_walls = len(WINDOW.walls_coordinates)
    for i in range(0, int_number_walls):
        if array_coordinates[0] in range(
            WINDOW.walls_coordinates[i]["point1"][0],
            WINDOW.walls_coordinates[i]["point2"][0],
        ) and array_coordinates[1] in range(
            WINDOW.walls_coordinates[i]["point1"][1],
            WINDOW.walls_coordinates[i]["point2"][1],
        ):
            return True
    return False


def set_already_contain_latter_array(list_of_points, array_coordinates):  # (?)
    tuple_which_rectangle_contains_point = (
        tuple_which_are_coordinates_of_rectangle_containing_array(array_coordinates)
    )
    bool_check_border_rectangle_or_not = bool_in_border_of_rectangle(array_coordinates)

    r0 = 0
    r1 = 1
    if bool_check_border_rectangle_or_not:
        r0 = -1
        r1 = 1
    for i in range(r0, r1):
        for j in range(r0, r1):
            if (
                tuple_which_rectangle_contains_point[0] + i
                >= WINDOW.number_subdivision_x_axis
                or tuple_which_rectangle_contains_point[1] + j
                >= WINDOW.number_subdivision_y_axis
                or tuple_which_rectangle_contains_point[0] + i < 0
                or tuple_which_rectangle_contains_point[1] + i < 0
            ):
                pass
            for array_point_into_subset in list_of_points[
                tuple_which_rectangle_contains_point[0] + i
            ][tuple_which_rectangle_contains_point[1] + j]:
                if np.array_equal(array_point_into_subset, array_coordinates):
                    return True
    return False


def array_point_location_available(set_of_points, array_coordinates):
    if not array_coordinates[0] in range(
        0, WINDOW.width_crowds_screen
    ) or not array_coordinates[1] in range(0, WINDOW.height_crowds_screen):
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
                random.randint(0, WINDOW.width_crowds_screen),
                random.randint(0, WINDOW.height_crowds_screen),
            ]
        )
        tuple_rectangle_location_point = (
            tuple_which_are_coordinates_of_rectangle_containing_array(new_point)
        )
        if array_point_location_available(set_of_points, new_point):
            break
    set_of_points[tuple_rectangle_location_point[0]][
        tuple_rectangle_location_point[1]
    ].append(new_point)
    return set_of_points


def create_empty_set_of_points():
    set_of_points = []

    for i in range(0, WINDOW.number_subdivision_x_axis):
        set_of_points.append([])
        for j in range(0, WINDOW.number_subdivision_y_axis):
            set_of_points[i].append([])
    return set_of_points


def create_set_of_valid_points():
    int_number_individuals = CROWD.number_individuals_in_crowd
    set_of_points = create_empty_set_of_points()

    for i in range(0, int_number_individuals):
        set_of_points = init_a_new_valid_point(set_of_points)
    return set_of_points
