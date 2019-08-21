import subprocess
import os
import json
from utils import battery_id

with open('batteries.json', 'r') as file: 
    batteries = json.load(file)
    if not os.path.exists('pngs'):
        os.mkdir('pngs')

    for battery in batteries:
        out_png = f'./pngs/{battery_id(battery)}.png'
        subprocess.run(['dwebp', battery['imgUrl'], '-o', out_png])

