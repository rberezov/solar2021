from math import sqrt
#coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        r = sqrt((body.x - obj.x)**2 + (body.y - obj.y)**2)
        if body != obj:
            body.Fx += (obj.x - body.x) * gravitational_constant * obj.m * body.m / (r ** 3)
            body.Fy += (obj.y - body.y) * gravitational_constant * obj.m * body.m / (r ** 3)
            if r < body.R + obj.R:
                if body.R > obj.R:
                    obj.R = 0
                    obj.m = 0
                else:
                    body.R = 0
                    body.m = 0

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += ax * (dt ** 2) / 2 + body.Vx * dt
    body.y += ay * (dt ** 2) / 2 + body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
