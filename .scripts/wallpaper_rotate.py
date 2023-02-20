#!/usr/bin/python

from pathlib import Path
import subprocess
import time
from random import choice


while True:
    next_wallpaper: Path = None
    time.sleep(900.0)
    wallpaper_list: Path = Path.home().joinpath(".wallpapers")
    wallpapers: list = [wp for wp in wallpaper_list.iterdir()]
    next_wallpaper = choice(wallpapers)
    subprocess.Popen(['hyprctl', 'hyprpaper', 'preload', next_wallpaper], stdout=subprocess.PIPE)  # Preload the next wallpaper
    subprocess.Popen(['hyprctl', 'hyprpaper', 'wallpaper', f'HDMI-A-1,{next_wallpaper}'], stdout=subprocess.PIPE)  # Set the next wallpaper
    subprocess.Popen(['hyprctl', 'hyprpaper', 'wallpaper', f'HDMI-A-2,{next_wallpaper}'], stdout=subprocess.PIPE)  # Set the next wallpaper
    subprocess.Popen(['hyprctl', 'hyprpaper', 'unload', 'all'], stdout=subprocess.PIPE)  # Unload the previous wallpaper
