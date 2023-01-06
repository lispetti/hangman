"""
comp.cs.100
Liisa Piirainen
liisa.i.piirainen@tuni.fi
151254255
"""

from tkinter import Tk, Canvas, Frame, BOTH, ARC
import time
from tkinter import messagebox


class SlipknotGraphics:

    def __init__(self, win):
        self.__canvas = Canvas(win, width=100, height=100)
        self.__canvas.grid(row=0, column=15, rowspan=5)
        self.__step_nro = 0

    def draw_next(self):
        if self.__step_nro == 0:
            cord = 10, 85, 76, 300
            self.__canvas.create_arc(cord, start=30, extent=120, style=ARC, width=3)
        if self.__step_nro == 1:
            self.__canvas.create_line(43, 85, 43, 15)
        if self.__step_nro == 2:
            self.__canvas.create_line(43, 15, 80, 15)
        if self.__step_nro == 3:
            self.__canvas.create_line((43, 30, 58, 15))
        if self.__step_nro == 4:
            self.__canvas.create_oval(72, 30, 88, 46)
            self.__canvas.create_line(78, 37, 79, 37)
            self.__canvas.create_line(82, 37, 83, 37)
            self.__canvas.create_line(76, 42, 84, 42)
        if self.__step_nro == 5:
            self.__canvas.create_line(80, 46, 80, 66)
        if self.__step_nro == 6:
            self.__canvas.create_line(80, 51, 75, 61)
            self.__canvas.create_line(80, 51, 85, 61)
        if self.__step_nro == 7:
            self.__canvas.create_line(80, 66, 75, 80)
            self.__canvas.create_line(80, 66, 85, 80)
        if self.__step_nro == 8:
            self.__canvas.create_line(80, 15, 80, 30)
        is_finished = self.__step_nro == 8
        self.__step_nro += 1
        return is_finished


