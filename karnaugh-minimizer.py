# TODO Implements GUI, following imports are destined to this purpose
from tkinter import *
from tkinter import ttk


def is_pow2(a):
    """
    Return True if the integer a is a power of 2
    """
    return a == 1 or int(bin(a)[3:], 2) == 0


def filter(coord_list):
    """
    Return a list with non doublon of each item
    """

    checked_values = []

    for value in coord_list:
        if not value in checked_values:
            checked_values.append(value)

    return checked_values


def sort_list(coord_list):
    """
    Return a sorted list of coordinates, by y, then x
    """
    return sorted(coord_list, key=lambda k: [k[1], k[0]])


def find_rects(k_map):
    """
    Return a list containing all the possible rectangles containing 1 in a Karnaugh map
    """

    x,y = 0,0

    rects = []

    for line in k_map:
        for case in line:
            if case:
                rects.append([x, y])

    return rects


def reverse_map(k_map):
    """
    Return the reversed map from k_map

    Change each 1 by 0, and each 0 by a 1
    """
    
    r_map = []
    for line in k_map:
        r_line = []
        for case in line:
            r_line.append(not case)
        r_map.append(r_line)

    return r_map


def print_table(k_map):
    """
    Print a Karnaugh map
    """
    
    for line in k_map:
        line_to_print = ""
        for case in line:
            line_to_print += "["
            if case:
                line_to_print += "1"
            else:
                line_to_print += "0"
            line_to_print += "] "
        print(line_to_print)


def main():
    test_map = [[True, True, True, False], [False, True, False, True]]
    print_table(test_map)


if __name__ == '__main__':
    main()
