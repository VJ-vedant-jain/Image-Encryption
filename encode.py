from PIL import Image
import numpy as np
from itertools import permutations
import json

image = Image.open(r"D:\Code\image encoder decoder\image.png").convert("RGB")
image_array = np.array(image)

transformed_array = np.empty(image_array.shape, dtype=object)

for row_idx, row in enumerate(image_array):
    for col_idx, rgb in enumerate(row):
        for color_idx, color in enumerate(rgb):
            str_color = str(int(color))
            permList = sorted([''.join(p) for p in permutations(str_color)])

            l = [0] * 10
            x = list(dict.fromkeys(str_color))
            y = [str_color.count(i) for i in x]

            for idx, digit in enumerate(x):
                l[int(digit)] = y[idx]

            a = permList.index(str_color) if str_color in permList else -1
            j = (l, a)
            transformed_array[row_idx, col_idx, color_idx] = j

print(transformed_array)
with open(r'D:\Code\image encoder decoder\encoded.json', 'w') as f:
        f.write(json.dumps(transformed_array.tolist()))