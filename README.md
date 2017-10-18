# changeWallpaper
Simple python scripts to change wallpaper in windows. The script will pickup wallpaper from local folder.

# Setup
* Create a folder where all the wallpaper will be stored. This folder will also store "wallpaper.config" file if V2 script is used.
* In the script change the path to point it to the folder created.
* Create a schedular job in windows to automate the run of script to change wallpaper.

# Scripts
* ChangeWallpaperV1.py :  This is a fixed script. For example: A schedular job is created to run it every 30 mins i.e. wallpaper will keep changing after 30 minutes. Wallpaper will be selected randomly.
* changeWallpaperV2.py : This is more advanced script. It reads the rating of the images and based on that it will decide the amount of time the image should be set as wallpaper. For example: In the script base time is set as 15 minutes and the image selected has a rating of 4 then this image will have screen time of 15*4 i.e 60 minutes.

# Todo
* GUI & Binary creation for the script.
* Improvement in V2 script.
* Mulptiple platform support.
