#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Напишите программу, в которой определены следующие четыре функции: 1. Функция getInput() не имеет параметров,
# запрашивает ввод с клавиатуры и возвращает в основную программу полученную строку. 2. Функция testInput() имеет
# один параметр. В теле она проверяет, можно ли переданное ей значение преобразовать к целому числу. Если можно,
# возвращает логическое True. Если нельзя – False. 3. Функция strToInt() имеет один параметр. В теле преобразовывает
# переданное значение к целочисленному типу. Возвращает полученное число. 4. Функция printInt() имеет один параметр.
# Она выводит переданное значение на экран и ничего не возвращает.

import sys


def getInput():
    return float(input("Введите число "))


def testInput(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


def strToInt(b):
    return int(b)


def printInt(c):
    print(c)


if __name__ == '__main__':
    a = getInput()
    if testInput(a) is True:
        b = strToInt(a)
        printInt(b)
    if testInput(a) is False:
        print("Ошибка", file=sys.stderr)
        exit(1)
