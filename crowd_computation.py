from crowd_init import bool_point_location_available
from gradient_calculus import *


def float_distance_door(array_candiate_location):
    array_nearest_point_wall = array_prefered_point_to_quit(array_candiate_location)
    return sum(
        map(
            lambda i, j: (i - j) ** 2, array_candiate_location, array_nearest_point_wall
        )
    )


def array_prefered_point_to_quit(array_individuals_position):
    unit_vector_door = VECTORS.unit_vectors_tkinter[
        WINDOW.door_coordinates["direction"]
    ]
    int_coefficient_projection = sum(
        p * q for p, q in zip(unit_vector_door, array_individuals_position)
    )
    projection_outdoor_point = (
        unit_vector_door[0] * int_coefficient_projection,
        unit_vector_door[1] * int_coefficient_projection,
    )

    int_not_null_coordinate = max(
        projection_outdoor_point[0], projection_outdoor_point[1]
    )

    if (
        int_not_null_coordinate > WINDOW.door_coordinates["max"]
        and int_not_null_coordinate > 0
    ):
        return (
            projection_outdoor_point[0]
            / int_not_null_coordinate
            * WINDOW.door_coordinates["max"],
            projection_outdoor_point[1]
            / int_not_null_coordinate
            * WINDOW.door_coordinates["max"],
        )
    if WINDOW.door_coordinates["min"] > int_not_null_coordinate > 0:
        return (
            projection_outdoor_point[0]
            / int_not_null_coordinate
            * WINDOW.door_coordinates["min"],
            projection_outdoor_point[1]
            / int_not_null_coordinate
            * WINDOW.door_coordinates["min"],
        )
    return projection_outdoor_point


def best_tuple_motion(set_of_points, tuple_old_coordinates_individual, tuple_gradient_unit_vector):

    tuple_best_direction = (0, 0)
    int_score_best_direction = CROWD.int_score_new_location_preference

    for tuple_direction_available in VECTORS.acceptable_directions.values():
        if not bool_point_location_available(
            set_of_points,
            tuple_addition(tuple_direction_available, tuple_old_coordinates_individual),
        ):
            continue
        elif tuple_direction_available == tuple_gradient_unit_vector:
            int_score_new_direction_proposed = 0
        else:
            int_score_new_direction_proposed = float_distance_door(
                tuple_addition(
                    tuple_direction_available, tuple_old_coordinates_individual
                )
            )

        if int_score_new_direction_proposed <= int_score_best_direction:
            tuple_best_direction = tuple_direction_available
            int_score_best_direction = int_score_new_direction_proposed

    return tuple_best_direction


def move_all_points_once(
    set_of_points,
    list_vectors_directions=False,
    create_dict_reference_old_new_coordinates=False,
):
    new_vector_set_of_points = {}
    set_tuple_new_points_coordinates = set_of_points.copy()
    equiv_old_new_vector = {}

    # (?)
    gpu_dict_list_compute_all_gradients_set_of_points(set_of_points)

    dict_tuple_gradient_unit_vector = dict_list_compute_all_gradients_set_of_points(set_of_points)

    for tuple_individual_coordinates in set_of_points:

        tuple_vector_motion = best_tuple_motion(
            set_tuple_new_points_coordinates, tuple_individual_coordinates,
            dict_tuple_gradient_unit_vector[tuple_individual_coordinates]
        )
        tuple_moved_coordinates = tuple_addition(
            tuple_individual_coordinates, tuple_vector_motion
        )
        set_tuple_new_points_coordinates.discard(tuple_individual_coordinates)
        set_tuple_new_points_coordinates.add(tuple_moved_coordinates)

        if len(set_tuple_new_points_coordinates) != CROWD.number_individuals_in_crowd:
            exit("Erreur fatale : le nombre de points dans le nuage a cahngé")

        if create_dict_reference_old_new_coordinates:
            equiv_old_new_vector[tuple_moved_coordinates] = tuple_individual_coordinates

        if list_vectors_directions:
            new_vector_set_of_points[tuple_moved_coordinates] = tuple_substract_tuples(
                tuple_moved_coordinates, tuple_individual_coordinates
            )

    if list_vectors_directions and equiv_old_new_vector:
        return (
            set_tuple_new_points_coordinates,
            new_vector_set_of_points,
            equiv_old_new_vector,
        )
    elif list_vectors_directions:
        return set_tuple_new_points_coordinates, new_vector_set_of_points

    return set_tuple_new_points_coordinates
