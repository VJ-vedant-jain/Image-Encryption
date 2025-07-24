from PIL import Image
import numpy as np
from itertools import permutations
import json

# Load JSON file
json_path = r"D:\Code\image encoder decoder\encoded.json"
with open(json_path, 'r') as f:
    decoded_data = json.load(f) 

decoded_array = np.zeros((len(decoded_data), len(decoded_data[0]), 3), dtype=np.uint8)

for row_idx, row in enumerate(decoded_data):
    for col_idx, rgb in enumerate(row):
        for color_idx in range(3):
            color = rgb[color_idx][0] 
            order = rgb[color_idx][1] 
            l = ''
            for i in range(len(color)):
                if color[i] != 0:
                    l += str(i) * color[i]
            permList = sorted([''.join(p) for p in permutations(l)])

            j = int(permList[order]) if order != -1 else 0 

            decoded_array[row_idx, col_idx, color_idx] = j

decoded_image = Image.fromarray(decoded_array)

decoded_image.save(r"D:\Code\image encoder decoder\decoded.png")

with open(r'D:\Code\image encoder decoder\decoded.json', 'w') as f:
    json.dump(decoded_array.tolist(), f)
