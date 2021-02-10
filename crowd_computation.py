from constants import *
import numpy as np
from crowd_init import point_location_available


def array_prefered_point_to_quit(array_individuals_position):
    unit_vector_door = VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates['direction']]
    projection_outdoor_point = unit_vector_door * np.dot(unit_vector_door, array_individuals_position)

    int_not_null_coordinate = max(projection_outdoor_point[0], projection_outdoor_point[1])
    if int_not_null_coordinate > WINDOW.door_coordinates['max'] and int_not_null_coordinate > 0:
        return projection_outdoor_point / int_not_null_coordinate * WINDOW.door_coordinates['max']
    if int_not_null_coordinate < WINDOW.door_coordinates['min'] and int_not_null_coordinate['max'] > 0:
        return projection_outdoor_point / int_not_null_coordinate * WINDOW.door_coordinates['min']
    return projection_outdoor_point


def array_square_norm_gradient(array_point):
    norm = np.sqrt(array_point[0] ** 2 + array_point[1] ** 2)
    if norm == 0:
        return False
    else:
        return np.array([array_point[0] / norm, array_point[1] / norm])


def array_gradient_wall(array_coordinates):
    array_prefered_exit = array_prefered_point_to_quit(array_coordinates)
    array_gradient = array_square_norm_gradient(np.subtract(array_coordinates, array_prefered_exit))
    if not isinstance(array_prefered_exit, bool):
        return array_gradient
    return False


def array_unit_direction_nearest_gradient(array_unit_gradient):
    theta = np.angle([array_unit_gradient[0] - 1j * array_unit_gradient[1]])[0]
    octant_circle_number = int(np.floor(((np.floor(theta / (2 * np.pi) * 16) + 1) % 16) / 2))
    return VECTORS.acceptable_directions[octant_circle_number]


def array_compute_unit_vector_gradient_step(array_position):
    array_gradient_step = array_gradient_wall(array_position)
    if np.count_nonzero(array_gradient_step) > 0:
        array_unit_gradient_step = array_gradient_step / np.linalg.norm(array_gradient_step)
        return array_unit_direction_nearest_gradient(array_unit_gradient_step)
    else:
        return False


def int_distance_door(array_cadndiate):
    array_nearest_point_wall = array_prefered_point_to_quit(array_cadndiate)
    return np.linalg.norm(array_cadndiate - array_nearest_point_wall)


def score_valid_motion_vector_candidates(array_old_coordinates, list_array_new_locations_available):
    array_gradient_unit_vector = array_compute_unit_vector_gradient_step(array_old_coordinates)
    list_array_of_candidates = []
    for i in range(0, len(list_array_new_locations_available)):
        array_new_direction_available = list_array_new_locations_available[i] - array_old_coordinates
        if np.array_equal(array_new_direction_available, array_gradient_unit_vector):
            list_array_of_candidates.append([0, list_array_new_locations_available[i]])
        else:
            list_array_of_candidates.append([int_distance_door(list_array_new_locations_available[i]),
                                             list_array_new_locations_available[i]])
    return list_array_of_candidates


def array_valid_new_point_coordinates(list_set_of_points, array_point):
    list_array_new_locations_available = []
    for array_motion in VECTORS.acceptable_directions.values():
        array_candidate_new_point = np.add(array_motion, array_point)
        if point_location_available(list_set_of_points, array_candidate_new_point):
            list_array_new_locations_available.append(array_candidate_new_point)
    if len(list_array_new_locations_available) == 0:
        return array_point
    # return choice(list_array_new_locations_available)  # random direction of a point.
    return score_valid_motion_vector_candidates(array_point, list_array_new_locations_available)[0][1]


def move_all_points_once(list_array_set_of_points):
    new_list_array_set_of_points = list_array_set_of_points
    for i in range(0, len(list_array_set_of_points)):
        array_moved_point = array_valid_new_point_coordinates(new_list_array_set_of_points,
                                                              new_list_array_set_of_points[i])
        new_list_array_set_of_points[i] = array_moved_point
    return new_list_array_set_of_points
