from crowd_init import create_set_of_valid_points
from crowd_computation import move_all_points_once
from constants import CROWD
import time


def set_tuple_skip_all_sequences_motion_crowd():
    set_people_coordinates = create_set_of_valid_points()
    for i in range(0, CROWD.number_of_movements):
        set_people_coordinates = move_all_points_once(set_people_coordinates)
        print(set_people_coordinates)  # (?)
    return set_people_coordinates


t0 = time.time()
set_tuple_final_coordinates_crowd = set_tuple_skip_all_sequences_motion_crowd()
print(set_tuple_final_coordinates_crowd)
t = time.time()

print("Temps d'exécution du programme : ", t - t0)
