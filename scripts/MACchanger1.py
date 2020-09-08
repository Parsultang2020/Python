#!/usr/bin/env python3

import subprocess      # импортируем модуль subprocess
import optparse        # импортируем модуль optparse

parser = optparse.OptionParser()  # OptionParser - класс модуля optparser
parser.add_option("-i", "--interface", dest="interface", help="Интерфейс для изменения МАС адреса")
parser.parse_args()

interface = input("Введите имя интерфейса: ")
new_mac = input("Укажите новый МАС: ")

print("Меням МАС адрес для " + interface + " на " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])