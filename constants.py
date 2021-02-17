import numpy as np
import sys


class VECTORS:
    unit_vectors_tkinter = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}
    acceptable_directions = {
        0: (-1, 0),
        1: (-1, 1),
        2: (0, -1),
        3: (1, -1),
        4: (1, 0),
        5: (1, 1),
        6: (0, 1),
        7: (-1, 1),
    }


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


class CROWD:
    number_individuals_in_crowd = 50
    minimum_pixel_distance = 1
    minimum_distance_authorized_to_exit = 0.001
    number_of_movements = 1000
    int_score_new_location_preference = sys.maxsize
