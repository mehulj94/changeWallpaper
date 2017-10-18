import os
import sys
import ctypes
import random


PATH = "C:\Users\element\Pictures\Wallpaper" #Path to Wallpaper folder
SPI_SETDESKWALLPAPER = 20 
files = os.listdir(PATH)
files.remove('wallpaper.config')

if files:
    file_name = random.choice(files)
    openImage = PATH + "\\" + random.choice(files)
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, openImage , 3)
    
sys.exit()