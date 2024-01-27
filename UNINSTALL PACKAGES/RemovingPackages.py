import subprocess
from messagebox import *
import time

print("UNINSTALLER PACKAGES...")

requirements_path = 'requirements.txt'

command = f'pip uninstall -r {requirements_path}'

#time.sleep(2)

subprocess.run(command, shell=True)

showinfo("Message", "All files have been successfully deleted from your computer")
