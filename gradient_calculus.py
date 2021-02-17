from constants import *

#import pycuda.driver as cuda
#import pycuda.autoinit
#from pycuda.compiler import SourceModule


def array_gradient_wall(array_coordinates):
    array_prefered_exit = array_prefered_point_to_quit(array_coordinates)
    tuple_coordinate = tuple(map(lambda i, j: i - j, array_coordinates, array_prefered_exit))
    array_gradient = array_square_norm_gradient(tuple_coordinate)
    if not isinstance(array_prefered_exit, bool):
        return array_gradient
    return False


def tuple_addition(tuple1, tuple2):  # (?)
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def tuple_substract_tuples(tuple1, tuple2):  # (?)
    return tuple1[0] - tuple2[0], tuple1[1] - tuple2[1]


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


def array_compute_unit_vector_gradient_step(array_position):
    array_gradient_step = array_gradient_wall(array_position)
    if np.count_nonzero(array_gradient_step) > 0:
        array_unit_gradient_step = array_gradient_step / np.linalg.norm(array_gradient_step)
        return array_unit_direction_nearest_gradient(array_unit_gradient_step)
    else:
        return False


def array_unit_direction_nearest_gradient(array_unit_gradient):
    double_angle_gradient = np.angle([array_unit_gradient[0] + 1j * array_unit_gradient[1]])[0]
    int_octant_circle_number = int(np.floor(((np.floor(double_angle_gradient / (2 * np.pi) * 16) + 1) % 16) / 2))
    return VECTORS.acceptable_directions[int_octant_circle_number]


def compute_all_graidents_set_of_points(set_coordinates_points):
    tuple_gradient_unit_vector = array_compute_unit_vector_gradient_step(set_coordinates_points)  # Parall

    pass