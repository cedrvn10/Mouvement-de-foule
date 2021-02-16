from numpy import array, random

from constants import WINDOW, CROWD


def array_is_outside_screen(array_coordinates):
    if not array_coordinates[0] in range(0, WINDOW.width_crowds_screen) or \
            not array_coordinates[1] in range(0, WINDOW.height_crowds_screen):
        return True
    else:
        return False


def array_is_into_a_wall(array_coordinates):
    for i in range(0, len(WINDOW.walls_coordinates)):
        if array_coordinates[0] in range(WINDOW.walls_coordinates[i]['point1'][0],
                                         WINDOW.walls_coordinates[i]['point2'][0]) and \
                array_coordinates[1] in range(WINDOW.walls_coordinates[i]['point1'][1],
                                              WINDOW.walls_coordinates[i]['point2'][1]):
            return True
    return False


def set_already_contain_latter_array(list_array__of_points, array_coordinates):  # (?)
    list_set_of_points = [list(point) for point in list_array__of_points]
    list_coordinates = list(array_coordinates)
    return list_coordinates in list_set_of_points


def point_location_available(set_of_points, array_coordinates):
    if array_is_outside_screen(array_coordinates):
        return False

    if array_is_into_a_wall(array_coordinates):
        return False

    if set_already_contain_latter_array(set_of_points, array_coordinates):
        return False

    return True


def init_a_new_valid_point(set_of_points):
    while True:
        new_point = array(
            [int(random.randint(0, WINDOW.width_crowds_screen)), int(random.randint(0, WINDOW.height_crowds_screen))])
        if point_location_available(set_of_points, new_point):
            break
    set_of_points.append(new_point)
    return set_of_points


def create_set_of_valid_points():
    set_of_points = []
    for i in range(0, CROWD.number_individuals_in_crowd):
        set_of_points = init_a_new_valid_point(set_of_points)
    return set_of_points
