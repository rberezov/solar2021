# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject
import solar_model

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    split_line = line.split(" ")
    star.R = float(split_line[1])
    star.color = split_line[2]
    star.m = float(split_line[3])
    star.x = float(split_line[4])
    star.y = float(split_line[5])
    star.Vx = float(split_line[6])
    star.Vy = float(split_line[7])

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    split_line = line.split(" ")
    planet.R = float(split_line[1])
    planet.color = split_line[2]
    planet.m = float(split_line[3])
    planet.x = float(split_line[4])
    planet.y = float(split_line[5])
    planet.Vx = float(split_line[6])
    planet.Vy = float(split_line[7])

def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'a') as out_file:
        for obj in space_objects:
            print("%s %d %s %f %f %f %f %f" % (obj.type.title(), obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy), file = out_file)

def write_satellite_to_file(output_filename, space_objects):
    with open(output_filename, 'a') as out_file:
        for obj in space_objects:
            if(obj.type == "planet"):
                print( "%s %f %s %f %s %f %s %f" % ("x: ", obj.x, "y: ", obj.y, "distance to star: ", solar_model.distance_satellite(space_objects[0], obj), "speed: ", solar_model.speed(obj)), file = out_file)

if __name__ == "__main__":
    print("This module is not for direct call!")