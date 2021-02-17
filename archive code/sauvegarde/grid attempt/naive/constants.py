import numpy as np


class VECTORS:
    unit_vectors_tkinter = {
        "u": np.array([0, -1]),
        "d": np.array([0, 1]),
        "l": np.array([-1, 0]),
        "r": np.array([1, 0]),
    }
    acceptable_directions = {
        0: unit_vectors_tkinter["l"],
        1: unit_vectors_tkinter["l"] + unit_vectors_tkinter["u"],
        2: unit_vectors_tkinter["u"],
        3: unit_vectors_tkinter["u"] + unit_vectors_tkinter["r"],
        4: unit_vectors_tkinter["r"],
        5: unit_vectors_tkinter["r"] + unit_vectors_tkinter["d"],
        6: unit_vectors_tkinter["d"],
        7: unit_vectors_tkinter["d"] + unit_vectors_tkinter["l"],
    }


class CROWD:
    number_individuals_in_crowd = 50
    minimum_pixel_distance = 1
    minimum_distance_authorized_to_exit = 0.001
    number_of_movements = 1000


class WINDOW:
    width = 300
    height = 300

    width_crowds_screen = width - 100
    height_crowds_screen = height - 100

    str_height, str_width, str_height_crowds_screen, str_width_crowds_screen = (
        str(height),
        str(width),
        str(height_crowds_screen),
        str(width_crowds_screen),
    )

    door_coordinates = {"direction": "r", "min": 1, "max": 20}

    walls_coordinates = [
        {"point1": (100, 100), "point2": (200, 200)},
        {"point1": (10, 10), "point2": (20, 20)},
    ]
