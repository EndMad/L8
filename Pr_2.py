#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В основной ветке программы вызывается функция cylinder(), которая вычисляет площадь цилиндра. В теле cylinder()
# определена функция circle(), вычисляющая площадь круга по формуле . В теле cylinder() у пользователя спрашивается,
# хочет ли он получить только площадь боковой поверхности цилиндра, которая вычисляется по формуле , или полную
# площадь цилиндра. В последнем случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
# вычислений функции circle().

import math


def circle(r):
    return r ** 2 * math.pi


def cylinder(r, h, S=True):
    circle(r)

    S_cylinder = 2 * math.pi * r * h

    if S:
        return S_cylinder + 2 * circle(r)
    else:
        return S_cylinder


if __name__ == '__main__':
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    c = input("S_cylinder или S? ")
    s = cylinder(r, h, S=(c == 'S'))
    print(s)
