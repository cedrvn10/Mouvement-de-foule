from crowd_init import create_set_of_valid_points
from crowd_computation import move_all_points_once
from constants import CROWD

set_of_people = create_set_of_valid_points()
i = 0
while i < CROWD.number_of_movements:
    set_of_people = move_all_points_once(set_of_people)
    print(str(i) + " :")
    print(set_of_people)
    i = i+1
