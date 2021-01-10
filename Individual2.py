#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения рейса;
# номер рейса; тип самолета. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть размещены в алфавитном порядке по названиям пунктов назначения; вывод на экран
# пунктов назначения и номеров рейсов, обслуживаемых самолетом, тип которого введен с
# клавиатуры; если таких рейсов нет, выдать на дисплей соответствующее сообщение

import sys
import json


def add(flights, destination, number, typ):
    flight = {
        'destination': destination,
        'number': number,
        'typ': typ,
    }

    flights.append(flight)
    if len(flights) > 1:
        flights.sort(key=lambda item: item.get('destination', ' '))


def _list():
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Пункт назначения рейса",
            "Номер рейса",
            "Тип самолёта"
        )
    )
    table.append(line)

    for idx, flight in enumerate(flights, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:<17} |'.format(
                idx,
                flight.get('destination', ' '),
                flight.get('number', 0),
                flight.get('typ', ' ')
            )
        )
    table.append(line)

    return '\n'.join(table)


def select(type):
    result = []
    for flight in flights:
        if type == flight.get('typ'):
            result.append(flight)

    return result


def load(filename):
    with open(filename, 'r') as fin:
        return json.load(fin)


def save(trains, filename):
    with open(filename, 'w') as fout:
        json.dump(trains, fout)


if __name__ == '__main__':
    flights = []

    while True:
        command = input(">>> ")

        if command == 'exit':
            break

        elif command == 'add':
            destination = input("Пункт назначения рейса? ")
            number = int(input("Номер рейса? "))
            typ = (input("Тип самолёта? "))

            add(flights, destination, number, typ)

        elif command == 'list':
            print(_list())

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            selected = select(parts[1])
            count = 1
            if selected:
                for idx, flight in enumerate(selected, 1):
                    print(
                        '{:>4}: Пункт назначения - {}, Номер рейса- {}'.format(count,
                                                                               flight.get('destination', ''),
                                                                               flight.get('number', '')
                                                                               )
                    )
            else:
                print("Таких пунктов назначения не найдено.")

        elif command.startswith('load '):
            parts = command.split(maxsplit=1)
            flights = load(parts[1])

        elif command.startswith('save '):
            parts = command.split(maxsplit=1)
            save(flights, parts[1])

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить данные;")
            print("list - Вывести данные;")
            print("select <Тип самолета> - запросить нужный рейс;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
