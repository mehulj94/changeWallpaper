import PIL.Image
import PIL.ExifTags
import os
import sys
import ctypes
import random
import datetime


PATH = "C:\Users\element\Pictures\Wallpaper" #Path to Wallpaper folder
CONFIG_PATH = "C:\Users\element\Pictures\Wallpaper\wallpaper.config" #Path where the config file for wallpaper will be stored
SPI_SETDESKWALLPAPER = 20 
SCHEDULE_TIME = 30
CURRENT_TIME = datetime.datetime.now()
files = os.listdir(PATH)
files.remove('wallpaper.config')


def writeConfig(imgname):
    config = open(CONFIG_PATH, 'w')
    config.write(imgname)
    config.write('\n')
    config.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    config.close()

def currentConfig():
    try:
        curr_config = open(CONFIG_PATH, 'r')
        config_data = curr_config.readlines()
        curr_img = config_data[0].rstrip()
        curr_img_time = datetime.datetime.strptime(config_data[1].rstrip(),"%Y-%m-%d %H:%M:%S")
        return curr_img, curr_img_time
    except Exception as e:
        print e
        return None,None

def changeWallpaper():
    try:
        print '[*] In changeWallpaper'
        # Read config file
        cur_img_set, cur_img_set_time = currentConfig()
        
        # extract exif of current wallpaper
        img = PIL.Image.open(cur_img_set)
        
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
        #print exif
        # Rating of Current Wallpaper
        img_rating = exif['Rating']
        
        # Calculate time delta
        time_delta = CURRENT_TIME - cur_img_set_time
        time_delta = (time_delta.days * 24 * 60) + (time_delta.seconds/60)
        
        # Calculate active time
        idle_active_time = SCHEDULE_TIME * img_rating
        
        if time_delta > idle_active_time:
            if files:
                file_name = random.choice(files)
                openImage = PATH + "\\" + file_name
                ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, openImage , 3)
                
                writeConfig(openImage)
            sys.exit()
    except (AttributeError, Exception) as e:
        print '[*] In exception: ', e
        if files:
            file_name = random.choice(files)
            openImage = PATH + "\\" + file_name
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, openImage , 3)
            writeConfig(openImage)
        sys.exit()


def main():
    changeWallpaper()
    
if __name__ == '__main__':
    main()