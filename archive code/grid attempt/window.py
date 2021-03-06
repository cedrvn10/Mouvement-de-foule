from tkinter import *
from constants import *
from crowd_computation import move_all_points_once


def init_window():
    fenetre = Tk()
    fenetre.title("Mouvement de foules : Fuite")
    fenetre.geometry(str(WINDOW.width) + "x" + str(WINDOW.height))
    fenetre.resizable(height=0, width=0)
    return fenetre


def init_crow_canvas(fenetre):
    grille_epidemie = Canvas(
        fenetre,
        width=WINDOW.width_crowds_screen,
        height=WINDOW.height_crowds_screen,
        bg="grey",
    )
    return grille_epidemie


def create_door_on_epidemia_grid(grille_epidemie):
    grille_epidemie.create_line(
        WINDOW.door_coordinates["min"]
        * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates["direction"]][0],
        WINDOW.door_coordinates["min"]
        * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates["direction"]][1],
        WINDOW.door_coordinates["max"]
        * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates["direction"]][0],
        WINDOW.door_coordinates["max"]
        * VECTORS.unit_vectors_tkinter[WINDOW.door_coordinates["direction"]][1],
        fill="white",
        width="8",
    )
    return grille_epidemie


def create_walls_on_epidemia_grid(grille_epidemie):
    for i in range(0, len(WINDOW.walls_coordinates)):
        grille_epidemie.create_rectangle(
            WINDOW.walls_coordinates[i]["point1"][0],
            WINDOW.walls_coordinates[i]["point1"][1],
            WINDOW.walls_coordinates[i]["point2"][0],
            WINDOW.walls_coordinates[i]["point2"][1],
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
    fenetre, set_of_points, list_id_canvas_set_of_points, grille_epidemie
):
    set_of_points, set_of_vectors = move_all_points_once(set_of_points, True)

    for i in range(0, len(set_of_points)):
        grille_epidemie.move(
            list_id_canvas_set_of_points[i], set_of_vectors[i][0], set_of_vectors[i][1]
        )

    fenetre.after(
        100,
        move_set_of_points,
        fenetre,
        set_of_points,
        list_id_canvas_set_of_points,
        grille_epidemie,
    )
