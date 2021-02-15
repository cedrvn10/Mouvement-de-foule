from crowd_init import create_set_of_valid_points
from crowd_computation import move_all_points_once
from constants import CROWD
import time

set_of_people = create_set_of_valid_points()
print("Tout début :\n")
print(set_of_people)
print("Nombre d'éléments dans un ensemble :")
print(len(set_of_people))

t0 = time.time()
i = 0
while i < CROWD.number_of_movements:
    set_of_people = move_all_points_once(set_of_people)
    print(str(i) + " :")
    print(set_of_people)
    i = i + 1

t = time.time()

print('Temps passé : ', t - t0)
