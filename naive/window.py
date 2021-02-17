from tkinter import *
from naive.constants import *
from naive.crowd_computation import move_all_points_once


def init_crowd_window():
    fenetre = Tk()
    fenetre.title("Mouvement de foules : Fuite")
    fenetre.geometry(str(WINDOW.int_width) + "x" + str(WINDOW.int_height))
    fenetre.resizable(height=0, width=0)
    return fenetre


def init_epidemia_grid(fenetre):
    grille_epidemie = Canvas(
        fenetre,
        width=WINDOW.int_width_crowds_screen,
        height=WINDOW.int_height_crowds_screen,
        bg="grey",
    )
    return grille_epidemie


def create_door_on_epidemia_grid(grille_epidemie):
    grille_epidemie.create_line(
        WINDOW.dict_door_coordinates["min"]
        * VECTORS.array_unit_vectors_tkinter[WINDOW.dict_door_coordinates["direction"]][
            0
        ],
        WINDOW.dict_door_coordinates["min"]
        * VECTORS.array_unit_vectors_tkinter[WINDOW.dict_door_coordinates["direction"]][
            1
        ],
        WINDOW.dict_door_coordinates["max"]
        * VECTORS.array_unit_vectors_tkinter[WINDOW.dict_door_coordinates["direction"]][
            0
        ],
        WINDOW.dict_door_coordinates["max"]
        * VECTORS.array_unit_vectors_tkinter[WINDOW.dict_door_coordinates["direction"]][
            1
        ],
        fill="white",
        width="8",
    )
    return grille_epidemie


def create_walls_on_epidemia_grid(grille_epidemie):
    for i in range(0, len(WINDOW.dict_dict_walls_coordinates)):
        grille_epidemie.create_rectangle(
            WINDOW.dict_dict_walls_coordinates[i]["point1"][0],
            WINDOW.dict_dict_walls_coordinates[i]["point1"][1],
            WINDOW.dict_dict_walls_coordinates[i]["point2"][0],
            WINDOW.dict_dict_walls_coordinates[i]["point2"][1],
        )

    grille_epidemie.pack()


def init_set_points_epidemia_grid(set_of_points, grille_epidemie):
    list_id_canvas_set_of_points = []
    for i in range(0, len(set_of_points)):
        id_individual = grille_epidemie.create_oval(
            set_of_points[i][0] - 1,
            set_of_points[i][1] - 1,
            set_of_points[i][0] + 1,
            set_of_points[i][1] + 1,
            fill="blue",
        )
        list_id_canvas_set_of_points.append(id_individual)
    return list_id_canvas_set_of_points


def move_set_of_points(
    window, set_of_points, list_id_canvas_set_of_points, canvas_id_grid_simulation
):
    set_of_points, set_of_vectors = move_all_points_once(set_of_points, True)

    for i in range(0, len(set_of_points)):
        canvas_id_grid_simulation.move(
            list_id_canvas_set_of_points[i], set_of_vectors[i][0], set_of_vectors[i][1]
        )

    window.after(
        10,
        move_set_of_points,
        window,
        set_of_points,
        list_id_canvas_set_of_points,
        canvas_id_grid_simulation,
    )
