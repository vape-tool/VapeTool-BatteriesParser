import subprocess
import os
import json
from vapetool.utils import battery_id

with open('batteries.json', 'r') as file: 
    batteries = json.load(file)
    if not os.path.exists('pngs'):
        os.mkdir('pngs')

    if not os.path.exists('jpgs'):
        os.mkdir('jpgs')

    if not os.path.exists('webps'):
        os.mkdir('webps')

    for battery in batteries:
        out_webp = f'./webps/{battery_id(battery)}.webp'
        subprocess.run(['cp', battery['imgUrl'], out_webp])

        out_png = f'./pngs/{battery_id(battery)}.png'
        subprocess.run(['dwebp', battery['imgUrl'], '-o', out_png])

        out_jpg = f'./jpgs/{battery_id(battery)}.jpg'
        subprocess.run(['dwebp', battery['imgUrl'], '-o', out_jpg])

