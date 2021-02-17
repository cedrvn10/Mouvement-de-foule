from crowd_init import create_set_of_valid_points
from window import *


fenetre = init_crowd_window()

grille_epidemie = init_epidemia_grid(fenetre)
grille_epidemie = create_door_on_epidemia_grid(grille_epidemie)
create_walls_on_epidemia_grid(grille_epidemie)

set_of_points = create_set_of_valid_points()
list_id_canvas_set_of_points = init_set_points_epidemia_grid(
    set_of_points, grille_epidemie
)

move_set_of_points(
    fenetre, set_of_points, list_id_canvas_set_of_points, grille_epidemie
)

fenetre.mainloop()
