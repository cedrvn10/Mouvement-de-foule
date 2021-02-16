from constants import *


def array_gradient_wall(array_coordinates):
    array_prefered_exit = array_prefered_point_to_quit(array_coordinates)
    tuple_coordinate = tuple(map(lambda i, j: i - j, array_coordinates, array_prefered_exit))
    array_gradient = array_square_norm_gradient(tuple_coordinate)
    if not isinstance(array_prefered_exit, bool):
        return array_gradient
    return False


def tuple_substract_tuples(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))


def array_square_norm_gradient(array_point):
    norm = np.sqrt(array_point[0] ** 2 + array_point[1] ** 2)
    if norm == 0:
        return False
    else:
        return np.array([array_point[0] / norm, array_point[1] / norm])


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


def float_distance_door(array_candiate_location):
    array_nearest_point_wall = array_prefered_point_to_quit(array_candiate_location)
    return sum(map(lambda i, j: (i - j) ** 2, array_candiate_location, array_nearest_point_wall))


def array_compute_unit_vector_gradient_step(array_position):
    array_gradient_step = array_gradient_wall(array_position)
    if np.count_nonzero(array_gradient_step) > 0:
        array_unit_gradient_step = array_gradient_step / np.linalg.norm(array_gradient_step)
        return array_unit_direction_nearest_gradient(array_unit_gradient_step)
    else:
        return False


def array_unit_direction_nearest_gradient(array_unit_gradient):
    theta = np.angle([array_unit_gradient[0] + 1j * array_unit_gradient[1]])[0]
    octant_circle_number = int(np.floor(((np.floor(theta / (2 * np.pi) * 16) + 1) % 16) / 2))
    return VECTORS.acceptable_directions[octant_circle_number]
