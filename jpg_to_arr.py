from PIL import Image
import numpy as np
import os
import csv
import pickle

with open('ready_dataset.csv', 'w', newline='') as f:
    fields = ['img', 'true']

    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    map_dict = {'cat': 0, 'dog': 1}

    for im in os.listdir('images'):
        img = Image.open(f'images/{im}')
        img = img.resize((150, 150), Image.Resampling.LANCZOS)

        data = np.asarray(img)

        writer.writerow({'img': pickle.dumps(data), 'true': map_dict[str(im).split('.')[0]]})


