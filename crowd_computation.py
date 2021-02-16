from crowd_init import point_location_available
from gradient_calculus import *


def array_prefered_point_to_quit(array_individuals_position):
    unit_vector_door = VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates['direction']]
    int_coefficient_projection = sum(p * q for p, q in zip(unit_vector_door, array_individuals_position))
    projection_outdoor_point = (unit_vector_door[0] * int_coefficient_projection,
                                unit_vector_door[1] * int_coefficient_projection)

    int_not_null_coordinate = max(projection_outdoor_point[0], projection_outdoor_point[1])

    if int_not_null_coordinate > WINDOW.door_coordinates['max'] and int_not_null_coordinate > 0:
        return (projection_outdoor_point[0] / int_not_null_coordinate * WINDOW.door_coordinates['max'],
                projection_outdoor_point[1] / int_not_null_coordinate * WINDOW.door_coordinates['max'])
    if WINDOW.door_coordinates['min'] > int_not_null_coordinate > 0:
        return (projection_outdoor_point[0] / int_not_null_coordinate * WINDOW.door_coordinates['min'],
                projection_outdoor_point[1] / int_not_null_coordinate * WINDOW.door_coordinates['min'])
    return projection_outdoor_point


def score_valid_motion_vector_candidates(tuple_old_coordinates, list_array_new_locations_available):
    tuple_gradient_unit_vector = array_compute_unit_vector_gradient_step(tuple_old_coordinates)
    dict_tuple_of_candidates = {}
    for tuple_location_available in list_array_new_locations_available:
        tuple_new_direction_available = tuple(map(lambda i, j: i - j, tuple_location_available, tuple_old_coordinates))
        if tuple_new_direction_available == tuple_gradient_unit_vector:
            dict_tuple_of_candidates[0] = tuple_location_available
        else:
            float_point_distance_to_door = float_distance_door(tuple_location_available)
            dict_tuple_of_candidates[float_point_distance_to_door] = tuple_location_available
    return dict_tuple_of_candidates


def array_valid_new_point_coordinates(set_of_points, tuple_point):
    list_tuple_new_locations_available = []
    for array_motion in VECTORS.acceptable_directions.values():
        array_candidate_new_point = tuple(map(sum, zip(array_motion, tuple_point)))
        if point_location_available(set_of_points, array_candidate_new_point):
            list_tuple_new_locations_available.append(array_candidate_new_point)

    if len(list_tuple_new_locations_available) == 0:
        return tuple_point

    dict_scored_new_locations = score_valid_motion_vector_candidates(tuple_point, list_tuple_new_locations_available)

    list_classified_scored_label_new_point_location = list(dict(sorted(dict_scored_new_locations.items(),
                                                                       key=lambda item: item[0])).items())
    array_vector_closest_to_the_door = list_classified_scored_label_new_point_location[0][1]

    return array_vector_closest_to_the_door


def move_all_points_once(set_of_points, list_vectors_directions=False, dict_corresponding_values_front=False):
    new_vector_set_of_points = {}
    copy_set_of_points = set_of_points.copy()
    equiv_old_new_vector = {}
    for tuple_set_of_points in set_of_points:
        array_moved_point = array_valid_new_point_coordinates(copy_set_of_points, tuple_set_of_points)
        copy_set_of_points.discard(tuple_set_of_points)
        copy_set_of_points.add(array_moved_point)

        if dict_corresponding_values_front:
            equiv_old_new_vector[array_moved_point] = tuple_set_of_points

        if list_vectors_directions:
            new_vector_set_of_points[array_moved_point] = tuple_substract_tuples(array_moved_point,
                                                                                 tuple_set_of_points)
    if list_vectors_directions and dict_corresponding_values_front:
        return copy_set_of_points, new_vector_set_of_points, equiv_old_new_vector
    elif list_vectors_directions:
        return copy_set_of_points, new_vector_set_of_points
    return copy_set_of_points
