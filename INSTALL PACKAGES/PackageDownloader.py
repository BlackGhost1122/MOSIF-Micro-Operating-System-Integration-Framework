from messagebox import *
import subprocess
import time

print("MOSIF PACKAGE DOWNLOADER...")

requirements_path = 'requirements.txt'

command = f'pip install -r {requirements_path}'

subprocess.run(command, shell=True)

showinfo("Message", "The files have been successfully downloaded to your computer")
