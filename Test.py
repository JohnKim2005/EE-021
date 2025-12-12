from PIL import Image
import numpy as np

im = np.asarray(Image.open("Uc_merced_logo.png"))

print(im)

sum = 0.0
for row in im:
    for col in row:
        for val in col:
            sum = sum + val

print(sum)

value = sum % 10

print("The Value of the Image is:", int(value))