import subprocess
import platform
import ctypes
import psutil
import time
from colorama import *
import sys
import os

# teams_path = r''C:\Users\Admin\Desktop\\MOSIF\\ConsoleOS.py'
# subprocess.Popen([teams_path], shell=True)
# print("Teams Opened")

class StartingSystem():
    def __init__(self, mosif_os, architecture_true_false, product_key):
        self.mosif_os = mosif_os
        self.architecture = architecture_true_false
        self.product_key = product_key
    def hide_taskbar(self):
        hwnd = ctypes.windll.user32.FindWindowW("Shell_traywnd", None)
        ctypes.windll.user32.ShowWindow(hwnd, 0)
    def display_computer_info(self):
        os.system('clear')
        os.system('cls')
        print("SCANNING YOUR COMPUTER...")
        time.sleep(2)
        print("CHECKING YOUR COMPUTER...")
        time.sleep(2.5)
    def check_system(self):
        while True:
            if self.architecture != True:
                break
            else:
                continue
        system_info = platform.uname()
        print(f"Type Operating System: M.O.S.I.F")
        print(f"System: {system_info.system}")
        print(f"Network Node: {system_info.node}")
        print(f"Version: {system_info.version}")
        print(f"Architecture: x{system_info.machine}")
        print(f"CPU: {platform.processor()}")
        time.sleep(0.5)
        print("CHECKING YOUR PRODUCT KEY...")
        time.sleep(2.5)
        print(Fore.RED + "Activation key not found, follow the link and purchase a product key")
        print(Fore.BLUE + "http://project8404918.tilda.ws")
        time.sleep(3.5)
        print(Fore.WHITE + "CHECKING YOUR DISK")
        time.sleep(4)
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"Device: {partition.device}")
            print(f"\tMount point: {partition.mountpoint}")
            print(f"\tType file system: {partition.fstype}")

            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue

            print(f"\tOverall volume: {usage.total / (1024 ** 3):.2f} GB")
            print(f"\tUsed: {usage.used / (1024 ** 3):.2f} GB")
            print(f"\tFree: {usage.free / (1024 ** 3):.2f} GB")
            print(f"\tUsage percentage: {usage.percent}%\n")
            time.sleep(2.2)
        print("Your computer has been successfully verified")
        time.sleep(1.5)
    def starting_operating_system(self):
        self.mosif_os = r'C:\Users\Admin\Desktop\MOSIF Enterprise\ConsoleOS.py'
        subprocess.Popen([self.mosif_os], shell=True)

    def __del__(self):
        del self.mosif_os
        del self.architecture
        del self.product_key
        print("The system is running")

start_os = StartingSystem('M.O.S.I.F', 'Architecture', 'Product Key')
start_os.hide_taskbar()
start_os.display_computer_info()
start_os.check_system()
start_os.starting_operating_system()
