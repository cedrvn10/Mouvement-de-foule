from naive.crowd_init import create_set_of_valid_points
from naive.crowd_computation import move_all_points_once
from naive.constants import CROWD
import time

list_array_coordinates_crowd = create_set_of_valid_points()
t0 = time.time()
step_number = 0
while step_number < CROWD.int_number_of_movements:
    list_array_coordinates_crowd = move_all_points_once(list_array_coordinates_crowd)
    print(str(step_number) + " :")
    print(list_array_coordinates_crowd)
    step_number = step_number + 1

t = time.time()

print('Temps passé : ', t - t0)