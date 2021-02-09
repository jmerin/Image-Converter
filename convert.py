from PIL import Image
import sys
import os

input_folder = sys.argv[1]
output_folder = sys.argv[2]

print(input_folder,output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    img = Image.open(f'{input_folder}{filename}')
    new_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{new_name}.png", "png")
    print("converted")

