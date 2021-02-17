from constants import *
from crowd_init import (
    array_point_location_available,
    create_empty_set_of_points,
    tuple_which_are_coordinates_of_rectangle_containing_array,
)
import numpy as np


def array_prefered_point_to_quit(array_individuals_position):
    unit_vector_door = VECTORS.unit_vectors_tkinter[
        WINDOW.door_coordinates["direction"]
    ]
    projection_outdoor_point = unit_vector_door * np.dot(
        unit_vector_door, array_individuals_position
    )

    int_not_null_coordinate = max(
        projection_outdoor_point[0], projection_outdoor_point[1]
    )
    if (
        int_not_null_coordinate > WINDOW.door_coordinates["max"]
        and int_not_null_coordinate > 0
    ):
        return (
            projection_outdoor_point
            / int_not_null_coordinate
            * WINDOW.door_coordinates["max"]
        )
    if WINDOW.door_coordinates["min"] > int_not_null_coordinate > 0:
        return (
            projection_outdoor_point
            / int_not_null_coordinate
            * WINDOW.door_coordinates["min"]
        )
    return projection_outdoor_point


def array_square_norm_gradient(array_point):
    norm = np.sqrt(array_point[0] ** 2 + array_point[1] ** 2)
    if norm == 0:
        return False  # (?)
    else:
        return np.array([array_point[0] / norm, array_point[1] / norm])


def array_gradient_wall(array_coordinates):
    array_prefered_exit = array_prefered_point_to_quit(array_coordinates)
    array_gradient = array_square_norm_gradient(
        np.subtract(array_coordinates, array_prefered_exit)
    )
    if not isinstance(array_prefered_exit, bool):
        return array_gradient
    return False


def array_unit_direction_nearest_gradient(array_unit_gradient):
    theta = np.angle([array_unit_gradient[0] + 1j * array_unit_gradient[1]])[0]
    octant_circle_number = int(
        np.floor(((np.floor(theta / (2 * np.pi) * 16) + 1) % 16) / 2)
    )
    return VECTORS.acceptable_directions[octant_circle_number]


def array_compute_unit_vector_gradient_step(array_position):
    array_gradient_step = array_gradient_wall(array_position)
    if np.count_nonzero(array_gradient_step) > 0:
        array_unit_gradient_step = array_gradient_step / np.linalg.norm(
            array_gradient_step
        )
        return array_unit_direction_nearest_gradient(array_unit_gradient_step)
    else:
        return False


def float_distance_door(array_candiate_location):
    array_nearest_point_wall = array_prefered_point_to_quit(array_candiate_location)
    return np.linalg.norm(array_candiate_location - array_nearest_point_wall)


def score_valid_motion_vector_candidates(
    array_old_coordinates, list_array_new_locations_available
):
    array_gradient_unit_vector = array_compute_unit_vector_gradient_step(
        array_old_coordinates
    )
    dict_array_of_candidates = {}
    for i in range(0, len(list_array_new_locations_available)):
        array_new_direction_available = (
            list_array_new_locations_available[i] - array_old_coordinates
        )
        if np.array_equal(array_new_direction_available, array_gradient_unit_vector):
            dict_array_of_candidates[0] = list_array_new_locations_available[i]
        else:
            float_point_distance_to_door = float_distance_door(
                list_array_new_locations_available[i]
            )
            dict_array_of_candidates[
                float_point_distance_to_door
            ] = list_array_new_locations_available[i]
    return dict_array_of_candidates


def array_valid_new_point_coordinates(list_set_of_points, array_point):
    list_array_new_locations_available = []
    list_acceptable_values = VECTORS.acceptable_directions.values()
    for array_motion in list_acceptable_values:
        array_candidate_new_location = np.add(array_motion, array_point)
        if array_point_location_available(
            list_set_of_points, array_candidate_new_location
        ):
            list_array_new_locations_available.append(array_candidate_new_location)
    if len(list_array_new_locations_available) == 0:
        return array_point
    dict_scored_new_locations = score_valid_motion_vector_candidates(
        array_point, list_array_new_locations_available
    )
    list_classified_scored_label_new_point_location = list(
        dict(
            sorted(dict_scored_new_locations.items(), key=lambda item: item[0])
        ).items()
    )
    array_vector_closest_to_the_door = list_classified_scored_label_new_point_location[
        0
    ][1]
    return array_vector_closest_to_the_door


def move_all_points_once(
    list_list_list_array_set_of_points, get_list_list_vector_direction=False
):
    new_list_list_array_set_of_points = create_empty_set_of_points()
    new_list_list_vector_set_of_points = new_list_list_array_set_of_points
    for list_list_array_locations in list_list_list_array_set_of_points:
        for list_array_coordinates_individual in list_list_array_locations:
            for array_coordinates_individual in list_array_coordinates_individual:
                array_moved_point = array_valid_new_point_coordinates(
                    list_list_list_array_set_of_points, array_coordinates_individual
                )
                tuple_moved_points_coordinates = tuple_which_are_coordinates_of_rectangle_containing_array(
                    array_moved_point
                )
                if get_list_list_vector_direction:
                    new_list_list_array_set_of_points[
                        tuple_moved_points_coordinates[0]
                    ][tuple_moved_points_coordinates[1]].append(
                        array_moved_point - array_coordinates_individual
                    )

                new_list_list_array_set_of_points[tuple_moved_points_coordinates[0]][
                    tuple_moved_points_coordinates[1]
                ].append(array_moved_point)

    if get_list_list_vector_direction:
        return new_list_list_array_set_of_points, new_list_list_vector_set_of_points
    return new_list_list_array_set_of_points
