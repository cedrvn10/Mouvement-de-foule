from constants import *
from tkinter import *
from crowd_init import create_set_of_valid_points
from crowd_computation import move_all_points_once

fenetre = Tk()
fenetre.title("Mouvement de foules : Fuite")
fenetre.geometry(str(WINDOW.width) + 'x' + str(WINDOW.height))
fenetre.resizable(height=0, width=0)

grille_epidemie = Canvas(fenetre, width=WINDOW.width_crowds_screen, height=WINDOW.height_crowds_screen,
                         bg='grey')

grille_epidemie.create_line(
    WINDOW.door_coordinates['min'] * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates['direction']][0],
    WINDOW.door_coordinates['min'] * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates['direction']][1],
    WINDOW.door_coordinates['max'] * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates['direction']][0],
    WINDOW.door_coordinates['max'] * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates['direction']][1],
    fill='black', width="8")

for i in range(0, len(WINDOW.walls_coordinates)):
    grille_epidemie.create_rectangle(WINDOW.walls_coordinates[i]['point1'][0], WINDOW.walls_coordinates[i]['point1'][1],
                                     WINDOW.walls_coordinates[i]['point2'][0], WINDOW.walls_coordinates[i]['point2'][1])

grille_epidemie.pack()

set_of_points = create_set_of_valid_points()
print(set_of_points)
list_id_canvas_set_of_points = []

for i in range(0, len(set_of_points)):
    id_individual = grille_epidemie.create_oval(set_of_points[i][0] - 1,
                                                set_of_points[i][1] - 1,
                                                set_of_points[i][0] + 1,
                                                set_of_points[i][1] + 1,
                                                fill='black')
    list_id_canvas_set_of_points.append(id_individual)


def move_set_of_points():
    global set_of_points, list_id_canvas_set_of_points, grille_epidemie
    set_of_points = move_all_points_once(set_of_points)
    for id_canvas in list_id_canvas_set_of_points:
        grille_epidemie.coords(id_canvas, set_of_points[i][0] - 1,
                               set_of_points[i][1] - 1,
                               set_of_points[i][0] + 1,
                               set_of_points[i][1] + 1)
    grille_epidemie.pack()


# move_set_of_points()
fenetre.mainloop()
