from cs1lib import *


def fill_blue():
    set_fill_color(.54, .81, .94)  # Sets color to Blue


def draw_background():  # Makes blue background
    fill_blue()
    draw_rectangle(0, 0, 400, 400)


def stem_maker():
    set_stroke_width(10)  # Makes 3 Stems of 10 pixel width all Green
    set_stroke_color(0, 1, 0)
    draw_line(100, 250, 100, 125)
    draw_line(200, 250, 200, 125)
    draw_line(300, 250, 300, 125)

    set_stroke_width(5)  # Draws leaf going off stem
    draw_line(100, 190, 140, 150)
    draw_line(200, 200, 180, 160)
    draw_line(200, 230, 230, 180)
    draw_line(300, 220, 320, 170)


def flower_maker():
    set_stroke_width(1)

    set_stroke_color(1, 0, 0)  # Makes Red Flower
    set_fill_color(1, 0, 0)
    draw_circle(100, 115, 30)
    set_fill_color(1, .68, .26)
    draw_circle(100, 115, 10)

    set_stroke_color(1, .4, .7)  # Makes Pink Flower
    set_fill_color(1, .4, .7)
    draw_circle(200, 115, 30)
    set_fill_color(1, .68, .26)
    draw_circle(200, 115, 10)

    set_stroke_color(0, 0, 1)   # Makes Blue Flower
    set_fill_color(0, 0, 1)
    draw_circle(300, 115, 30)
    set_fill_color(1, .68, .26)
    draw_circle(300, 115, 10)


def sun():  # Draws yellow circle in corner
    set_fill_color(.8, 1, 0)
    draw_circle(0, 0, 75)


def dirt():
    set_fill_color(.40, .26, .12)  # Sets stroke/fill to brown then draws rectangle
    draw_rectangle(0, 300, 500, 400)


def grass():
    set_stroke_color(.4, .26, .12)  # Sets stroke/fill to dark green then draws rectangle
    set_fill_color(0, .2, .13)
    draw_rectangle(0, 250, 400, 50)


def clouds():
    set_stroke_color(1, 1, 1)  # Sets stroke/fill color to white then draws ellipses
    set_fill_color(1, 1, 1)
    draw_ellipse(300, 25, 50, 20)
    draw_ellipse(290, 45, 50, 20)
    draw_ellipse(280, 25, 50, 20)
    draw_ellipse(260, 45, 50, 20)
    draw_ellipse(320, 45, 50, 20)


def text():
    # Writes in bottom corner
    set_stroke_color(1, 1, 1)
    draw_text('Roses are Red,', 10, 325)
    draw_text('Violets are Blue,', 10, 350)
    draw_text('Pink is a Great Color too!', 10, 375)


def draw():  # Draws picture by calling various functions 
    draw_background()
    stem_maker()
    flower_maker()
    sun()
    dirt()
    grass()
    clouds()
    text()


start_graphics(draw)  # Main body of function
