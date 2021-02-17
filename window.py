from tkinter import *
from constants import *
from crowd_computation import move_all_points_once


def init_crowd_window():
    fenetre = Tk()
    fenetre.title("Mouvement de foules : Fuite")
    fenetre.geometry(str(WINDOW.width) + "x" + str(WINDOW.height))
    fenetre.resizable(height=0, width=0)
    return fenetre


def init_epidemia_grid(fenetre):
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
    list_id_canvas_set_of_points = {}
    for point in set_of_points:
        id_individual = grille_epidemie.create_oval(
            point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1, fill="blue"
        )
        list_id_canvas_set_of_points[point] = id_individual
    return list_id_canvas_set_of_points


def move_set_of_points(
    fenetre, set_of_points, list_id_canvas_set_of_points, grille_epidemie
):
    (
        set_of_points,
        new_vector_set_of_points,
        equiv_old_new_coordinates,
    ) = move_all_points_once(set_of_points, True, True)

    list_id_canvas_set_of_points = {
        point: list_id_canvas_set_of_points[equiv_old_new_coordinates[point]]
        for point in set_of_points
    }

    for point in set_of_points:
        grille_epidemie.move(
            list_id_canvas_set_of_points[point],
            new_vector_set_of_points[point][0],
            new_vector_set_of_points[point][1],
        )

    fenetre.after(
        10,
        move_set_of_points,
        fenetre,
        set_of_points,
        list_id_canvas_set_of_points,
        grille_epidemie,
    )
