from colorama import *
import webbrowser
import pyfiglet as p
from datetime import datetime
import pygetwindow as gw
import subprocess
import ctypes
import time
import platform
import pygame
import pytz
import signal
import psutil
import os
import sys

class OperatingSystemMOS:
    def __init__(self, shell):
        self.shell = shell
        os.system('cls')
        pygame.mixer.init()
        init()
        pygame.mixer.music.load("musics\\Startup.mp3")
        pygame.mixer.music.play()
        signal.signal(signal.SIGINT, self.handle_ctrl_c)
        self.prev_active_window = None
        SW_HIDE = 0
        SW_SHOW = 5

    def handle_ctrl_c(self, signum, frame):
        print(Fore.RED + "\nCtrl+C is disabled. Please use 'exit' command to close the program." + Fore.WHITE)

    def full_display(self):
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        hWnd = kernel32.GetConsoleWindow()

        if hWnd:
            user32.ShowWindow(hWnd, 3)

    def hide_taskbar(self):
        hwnd = ctypes.windll.user32.FindWindowW("Shell_traywnd", None)
        ctypes.windll.user32.ShowWindow(hwnd, 0)

    def show_taskbar(self):
        hwnd = ctypes.windll.user32.FindWindowW("Shell_traywnd", None)
        ctypes.windll.user32.ShowWindow(hwnd, 1)
        ctypes.windll.user32.ShowWindow(hwnd, 4)

    def disable_close_button(self):
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        style = ctypes.windll.user32.GetWindowLongW(hwnd, ctypes.c_int(-16))
        new_style = style & ~0x80000
        ctypes.windll.user32.SetWindowLongW(hwnd, ctypes.c_int(-16), new_style)

    def disable_resize(self):
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        style = ctypes.windll.user32.GetWindowLongW(hwnd, ctypes.c_int(-16))
        new_style = style & ~0x40000 & ~0x10000
        ctypes.windll.user32.SetWindowLongW(hwnd, ctypes.c_int(-16), new_style)

    def hide_title_bar(self):
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        style = ctypes.windll.user32.GetWindowLongW(hwnd, ctypes.c_int(-16))
        new_style = style & ~0xC00000
        ctypes.windll.user32.SetWindowLongW(hwnd, ctypes.c_int(-16), new_style)

    def check_active_window(self):
        active_window = gw.getActiveWindow()
        if active_window != self.prev_active_window:
            pass
        self.prev_active_window = active_window

    def display_info(self):
        os.system('cls')
        self.mosif_emblem = p.figlet_format("M.O.S.I.F Enterprise", font="slant")
        print(Fore.RED + self.mosif_emblem)
        self.logo_mosif()
        print(Fore.WHITE + " M.O.S.I.F Enterprise")
        print(" Type 'help' to see a list of commands\n")

    def operating_system_function(self):
        while True:
            self.shell = input(" #> ")
            self.check_active_window()
            if self.shell == "help" or self.shell == "Help" or self.shell == "HELP":
                self.commands_list()

            elif self.shell == "open file manager" or self.shell == "Open file manager" or self.shell == "Open File manager" or self.shell == "Open File Manager" or self.shell == "OPEN FILE MANAGER":
                CREATE_NO_WINDOW = 0x08000000
                file_to_run = "FileManager.py"
                cmd = [sys.executable, file_to_run]
                subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)

            elif self.shell == "disk info" or self.shell == "Disk info" or self.shell == "Disk Info" or self.shell == "DISK INFO":
                self.print_disk_info()

            elif self.shell == "os info" or self.shell == "Os info" or self.shell == "Os Info" or self.shell == "OS INFO":
                print(" M.O.S.I.F Enterprise - Micro Operating System Integration Framework")
                print(" Version - 3.0\n")

            elif self.shell == "system info" or self.shell == "System info" or self.shell == "System Info" or self.shell == "SYSTEM INFO":
                self.print_system_info()

            elif self.shell == "open office manager" or self.shell == "Open office manager" or self.shell == "Open Office manager" or self.shell == "Open Office Manager" or self.shell == "OPEN OFFICE MANAGER":
                CREATE_NO_WINDOW = 0x08000000
                file_to_run = "MicrosoftOfficeManager.py"
                cmd = [sys.executable, file_to_run]
                subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)

            elif self.shell == "creators" or self.shell == "Creators" or self.shell == "CREATORS":
                self.print_creators()

            elif self.shell == "mendel info" or self.shell == "Mendel info" or self.shell == "Mendel Info" or self.shell == "MENDEL INFO":
                self.print_mendeleev_table()

            elif self.shell == "data time" or self.shell == "Data time" or self.shell == "Data Time" or self.shell == "DATA TIME":
                self.print_time_in_timezone(" Asia/Baku")
                self.print_time_in_timezone(" Europe/Istanbul")
                self.print_time_in_timezone(" Asia/Shanghai")
                self.print_time_in_timezone(" America/New_York")
                self.print_time_in_timezone(" Europe/Moscow")
                print("\n")

            elif self.shell == "cls" or self.shell == "CLS" or self.shell == "clear" or self.shell == "Clear" or self.shell == "CLEAR":
                self.display_info()

            elif self.shell == "shut down" or self.shell == "Shut down" or self.shell == "Shut Down" or self.shell == "SHUT DOWN":
                print(" Shutting down...")
                pygame.mixer.music.load("musics\\ShutDown.mp3")
                pygame.mixer.music.play()
                time.sleep(2)
                os.system("shutdown /s /t 1")
                self.show_taskbar()
                break

            elif self.shell == "open browser" or self.shell == "Open browser" or self.shell == "Open browser" or self.shell == "OPEN BROWSER":
                self.url = 'https://www.google.com'
                webbrowser.open_new_tab(self.url)

            elif self.shell == "browser info" or self.shell == "Browser info" or self.shell == "Browser Info" or self.shell == "BROWSER INFO":
                self.name_browser = "Chrome\Google"
                self.version_browser = 3.0
                print(f" Name: {self.name_browser}")
                print(f" Version: {self.version_browser}\n")

            elif self.shell == "activate mos" or self.shell == "Activate mos" or self.shell == "Activate Mos" or self.shell == "ACTIVATE MOS":
                CREATE_NO_WINDOW = 0x08000000
                file_to_run = "Activation.py"
                cmd = [sys.executable, file_to_run]
                subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)

            elif self.shell == "open calculator" or self.shell == "Open calculator" or self.shell == "Open Calculator" or self.shell == "Open Calculator" or self.shell == "OPEN CALCULATOR":
                CREATE_NO_WINDOW = 0x08000000
                file_to_run = "calculatorGUI.py"
                cmd = [sys.executable, file_to_run]
                subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)

            elif self.shell == "open mendel gui" or self.shell == "Open mendel gui" or self.shell == "Open Mendel gui" or self.shell == "Open Mendel Gui" or self.shell == "OPEN MENDEL GUI":
                exe_path = "C:\\Users\Admin\\Desktop\\OperatingSystemGUIM\\OperatingSystemGUIM\\bin\\Debug\\OperatingSystemGUIM.exe"
                subprocess.Popen(exe_path)

            elif self.shell == "open notepad" or self.shell == "Open notepad" or self.shell == "Open Notepad" or self.shell == "OPEN NOTEPAD":
                CREATE_NO_WINDOW = 0x08000000
                file_to_run = "notepad.py"
                cmd = [sys.executable, file_to_run]
                subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)
                
            elif self.shell == "exit":
                pygame.mixer.music.load("musics\\ShutDown.mp3")
                pygame.mixer.music.play()
                time.sleep(2)
                break

            elif self.shell == "mars algoritmika" or self.shell == "Mars algoritmika" or self.shell == "Mars Algoritmika" or self.shell == "MARS ALGORITMIKA":
                self.mars = "https://mars.algoritmika.az"
                print(" Starting...")
                webbrowser.open_new_tab(self.mars)

            elif self.shell == "open help center" or self.shell == "Open help center" or self.shell == "Open Help center" or self.shell == "Open Help Center" or self.shell == "OPEN HELP CENTER":
                help_center = "HelpUtilites\\HelpCenterMosif.exe"
                subprocess.Popen(help_center, creationflags=subprocess.DETACHED_PROCESS, shell=True)

            elif self.shell == "BIOS DOS" or self.shell == "bios dos":
                bios_dos = "BIOS.exe"
                subprocess.Popen(bios_dos, creationflags=subprocess.DETACHED_PROCESS, shell=True)
                break

            elif self.shell == "BIOS GUI" or self.shell == "bios gui":
                bat_file_path = 'BIOS GUI UTILITY\\BIOS.bat'
                subprocess.call(['start', 'cmd', '/c', bat_file_path], shell=True)
                break

            else:
                pygame.mixer.music.load("musics\\Errors.mp3")
                pygame.mixer.music.play()
                print(Fore.RED + "\n Error! Unknown command please try again\n" + Fore.WHITE)
    def commands_list(self):
        print(r"""
 +------------------------------+
 | command: help                |
 | command: open file manager   |
 | command: disk info           |
 | command: os info             |
 | command: system info         |
 | command: open office manager |
 | command: creators            |
 | command: mendel info         |
 | command: data time           |
 | command: cls\clear           |
 | command: shut down/Ctrl+C    |
 | command: open browser\info   |
 | command: browser --version   |
 | command: activate mos        |
 | command: open calculator     |
 | command: open notepad        |
 | command: open help center    |
 | command: BIOS DOS            |
 | command: BIOS GUI            |
 +------------------------------+
""")

    def print_disk_info(self):
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f" Устройство: {partition.device}")
            print(f" \tТочка монтирования: {partition.mountpoint}")
            print(f" \tТип файловой системы: {partition.fstype}")

            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue

            print(f" \tОбщий объем: {usage.total / (1024 ** 3):.2f} GB")
            print(f" \tИспользовано: {usage.used / (1024 ** 3):.2f} GB")
            print(f" \tСвободно: {usage.free / (1024 ** 3):.2f} GB")
            print(f" \tПроцент использования: {usage.percent}%\n")

    def print_system_info(self):
        system_info = platform.uname()

        print(f" Система: {system_info.system}")
        print(f" Узел сети: {system_info.node}")
        print(f" Версия: {system_info.version}")
        print(f" Архитектура: {system_info.machine}")
        print(f" Процессор: {platform.processor()}")

    def print_creators(self):
        print(r"""
 +---------------------------------------------+       
 |  Name     Surname      Work        Active   |
 +---------------------------------------------+
 |  Amin     Aliyev     Developer      True    |
 |  Saleh    Tahirli    Devel\Comp     True    |
 |  Eldar    Ismaylov   Eng Comp       True    |
 |  Ugur     Ragimov    Developer      True    |
 |  Rasul    Mamedli    Devel\Audio    True    |
 |  Elmar      ???      Developer      False   |
 +---------------------------------------------+
""")

    def print_mendeleev_table(self):
        print(Fore.GREEN + r"""
 ---------- Менделеевская таблица ----------
  "№ | Элемент  | Символ | Атомная масса");
  "1, 'Водород', 'H', 1.008"
  "2, 'Гелий', 'He', 4.0026"
  "3, 'Литий', 'Li', 6.94"
  "4, 'Бериллий', 'Be', 9.0122"
  "5, 'Бор', 'B', 10.81"
  "6, 'Углерод', 'C', 12.011"
  "7, 'Азот', 'N', 14.007"
  "8, 'Кислород', 'O', 15.999"
  "9, 'Фтор', 'F', 18.998"
  "10, 'Неон', 'Ne', 20.180"
  "11, 'Натрий', 'Na', 22.990"
  "12, 'Магний', 'Mg', 24.305"
  "13, 'Алюминий', 'Al', 26.982"
  "14, 'Кремний', 'Si', 28.085"
  "15, 'Фосфор', 'P', 30.974"
  "16, 'Сера', 'S', 32.06"
  "17, 'Хлор', 'Cl', 35.45"
  "18, 'Аргон', 'Ar', 39.948"
  "19, 'Калий', 'K', 39.098"
  "20, 'Кальций', 'Ca', 40.078"
  "21, 'Скандий', 'Sc', 44.956"
  "22, 'Титан', 'Ti', 47.867"
  "23, 'Ванадий', 'V', 50.942"
  "24, 'Хром', 'Cr', 51.996"
  "25, 'Марганец', 'Mn', 54.938"
  "26, 'Железо', 'Fe', 55.845"
  "27, 'Кобальт', 'Co', 58.933"
  "28, 'Никель', 'Ni', 58.693"
  "29, 'Медь', 'Cu', 63.546"
  "30, 'Цинк', 'Zn', 65.38"
  "31, 'Галлий', 'Ga', 69.723"
  "32, 'Германий', 'Ge', 72.630"
  "33, 'Мышьяк', 'As', 74.922"
  "34, 'Селен', 'Se', 78.971"
  "35, 'Бром', 'Br', 79.904"
  "36, 'Криптон', 'Kr', 83.798"
  "37, 'Рубидий', 'Rb', 85.468"
  "38, 'Стронций', 'Sr', 87.620"
  "39, 'Иттрий', 'Y', 88.906"
  "40, 'Цирконий', 'Zr', 91.224"
  "41, 'Ниобий', 'Nb', 92.906"
  "42, 'Молибден', 'Mo', 95.950"
  "43, 'Технеций', 'Tc', (98))"
  "44, 'Рутений', 'Ru', 101.070"
  "45, 'Родий', 'Rh', 102.906"
  "46, 'Палладий', 'Pd', 106.420"
  "47, 'Серебро', 'Ag', 107.868"
  "48, 'Кадмий', 'Cd', 112.414"
  "49, 'Индий', 'In', 114.818"
  "50, 'Олово', 'Sn', 118.710"
  "51, 'Антимоний', 'Sb', 121.760"
  "52, 'Теллур', 'Te', 127.600"
  "53, 'Иод', 'I', 126.904"
  "54, 'Ксенон', 'Xe', 131.293"
  "55, 'Цезий', 'Cs', 132.905"
  "56, 'Барий', 'Ba', 137.327"
  "57-71, 'Лантаноиды', 'La-Lu', -"
  "72, 'Гафний', 'Hf', 178.490"
  "73, 'Тантал', 'Ta', 180.948"
  "74, 'Вольфрам', 'W', 183.840"
  "75, 'Рений', 'Re', 186.207"
  "76, 'Осмий', 'Os', 190.230"
  "77, 'Иридий', 'Ir', 192.217"
  "78, 'Платина', 'Pt', 195.084"
  "79, 'Золото', 'Au', 196.967"
  "80, 'Ртуть', 'Hg', 200.592"
  "81, 'Таллий', 'Tl', 204.380"
  "82, 'Свинец', 'Pb', 207.200"
  "83, 'Висмут', 'Bi', 208.980"
  "84, 'Полоний', 'Po', 209"
  "85, 'Астат', 'At', 210"
  "86, 'Радон', 'Rn', 222"
  "87, 'Франций', 'Fr', 223"
  "88, 'Радий', 'Ra', 226"
  "89-103, 'Актиноиды', 'Ac-Lr'"
  "104, 'Резерфордий', 'Rf', (267)"
  "105, 'Дубний', 'Db', 270"
  "106, 'Сиборгий', 'Sg', 271"
  "107, 'Борий', 'Bh', '270'"
  "108, 'Хассий', 'Hs', 277"
  "109, 'Мейтнерий', 'Mt', 276"
  "110, 'Дармштадтий', 'Ds', 281"
  "111, 'Рентгений', 'Rg', 280"
  "112, 'Коперниций', 'Cn', 285"
  "113, 'Нихоний', 'Nh', 284"
  "114, 'Флеровий', 'Fl', 289"
  "115, 'Московий', 'Mc', 288"
  "116, 'Ливерморий', 'Lv', 293"
  "117, 'Теннессин', 'Ts', 294"
  "118, 'Оганессон', 'Og', 294"
""" + Fore.WHITE)

    def print_time_in_timezone(self, timezone_name):
        try:
            tz = pytz.timezone(timezone_name)
            current_time = datetime.now(tz)
            print(f"Текущее время в {timezone_name}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except pytz.UnknownTimeZoneError:
            print(f"Ошибка: Неизвестный часовой пояс {timezone_name}")

    def logo_mosif(self):
        print(r"""
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@#B@@@@@@@@@@@@@@@@
 @@@@@@@@@@#?. !#@@@@@@@@@@@@@@
 @@@@@@@@B7. .?B@@@@@@@@@@@@@@@
 @@@@@@G!  :J#@@@@@@G7?#@@@@@@@
 @@@@P~  ^Y&@@@@@@@@J. .7B@@@@@
 @&5^  ~P&@@@@@@@@@@@#Y:  !G@@@
 @!  .P@@@@@@@@@@@@@@@@@Y   Y@@
 @P^  ~P&@@@@@@@@@@@@@#Y^  !B@@
 @@@P~  ^Y&@@@@@@@@@B?: .7B@@@@
 @@@@@G!  :J#@@@@@@&J..J#@@@@@@
 @@@@@@@B7. .?B@@@@@@##@@@@@@@@
 @@@@@@@@@#?.  7&@@@@@@@@@@@@@@
 @@@@@@@@@@@#Y7P@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

mosif = OperatingSystemMOS("shell")
mosif.full_display()
mosif.hide_taskbar()
mosif.disable_close_button()
mosif.disable_resize()
mosif.hide_title_bar()
#mosif.handle_ctrl_c('', '')
mosif.display_info()
mosif.operating_system_function()