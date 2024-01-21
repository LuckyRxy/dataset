from PIL import Image
import os
import numpy as np

def png_to_raw(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的PNG文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)

            png_image = Image.open(input_path)

            image_array = np.array(png_image)

            output_filename = os.path.splitext(filename)[0] + ".raw"
            output_path = os.path.join(output_folder, output_filename)

            with open(output_path, "wb") as raw_file:
                raw_file.write(image_array.tobytes())

            print(f"Converted {filename} to {output_filename}")

input_folder = "images"
output_folder = "raw"

png_to_raw(input_folder, output_folder)

