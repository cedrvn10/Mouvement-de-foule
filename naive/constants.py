import numpy as np


class VECTORS:
    array_unit_vectors_tkinter = {"u": np.array([0, -1]), "d": np.array([0, 1]),
                            "l": np.array([-1, 0]), "r": np.array([1, 0])}
    acceptable_directions = {
        0: array_unit_vectors_tkinter["l"],
        1: array_unit_vectors_tkinter["l"] + array_unit_vectors_tkinter["u"],
        2: array_unit_vectors_tkinter["u"],
        3: array_unit_vectors_tkinter["u"] + array_unit_vectors_tkinter["r"],
        4: array_unit_vectors_tkinter["r"],
        5: array_unit_vectors_tkinter["r"] + array_unit_vectors_tkinter["d"],
        6: array_unit_vectors_tkinter["d"],
        7: array_unit_vectors_tkinter["d"] + array_unit_vectors_tkinter["l"],
    }


class CROWD:
    int_number_individuals_in_crowd = 50
    int_minimum_pixel_distance = 1
    float_minimum_distance_authorized_to_exit = 0.001
    int_number_of_movements = 1000


class WINDOW:
    int_width = 300
    int_height = 300

    int_width_crowds_screen = int_width - 100
    int_height_crowds_screen = int_height - 100

    str_height, str_width, str_height_crowds_screen, str_width_crowds_screen = str(int_height), str(int_width), str(
        int_height_crowds_screen), str(int_width_crowds_screen)

    dict_door_coordinates = {'direction': 'r', 'min': 1, 'max': 20}

    dict_dict_walls_coordinates = [
        {'point1': (100, 100), 'point2': (200, 200)},
        {'point1': (10, 10), 'point2': (20, 20)}
    ]
