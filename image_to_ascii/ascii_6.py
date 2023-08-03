import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

ASCII_CHARS = "@%#*|\+=-:. "  #[::-1]

FONT_SCALING_FACTORS = {
    'SpaceMono-Regular.ttf': (8, 15),
}

def map_to_ascii(gray_val):
    ascii_val = gray_val * (len(ASCII_CHARS) - 1) // 255
    return ASCII_CHARS[int(ascii_val)]

def image_to_ascii(image_path, output_file_name, font_path, new_width=200):
    image = Image.open(image_path)

    (old_width, old_height) = image.size
    aspect_ratio = old_height/old_width
    char_aspect_ratio = scaling_factor[0] / scaling_factor[1]  # font's width/height
    new_height = int(aspect_ratio * new_width * char_aspect_ratio)

    image = image.resize((new_width, new_height)).convert('L')  # convert to grayscale
    pixels = np.array(image)

    # Create a new image with dimensions calculated for ASCII characters
    ascii_image = Image.new('RGB', (new_width * scaling_factor[0], new_height * scaling_factor[1]), color=(0, 0, 0))  
    d = ImageDraw.Draw(ascii_image)
    
    # Use a lighter font instead of the default one
    font = ImageFont.truetype(font_path, 15)

    ascii_str = ""
    for y, row in enumerate(pixels):
        ascii_row = [map_to_ascii(pixel) for pixel in row]
        ascii_str += "".join(ascii_row) + "\n"
        green = int((1 - y/new_height) * 255)
        blue = int((y/new_height) * 255)
        d.text((0, y * scaling_factor[1]), "".join(ascii_row), fill=(0, green, blue), font=font)

    output_directory = "output"
    ascii_image.save(os.path.join(output_directory, output_file_name))

    return ascii_str


if __name__ == "__main__":
    output_file_name = input("Enter output file name (with extension): ")
    font_path = input("Enter font file name (with extension): ")
    new_width = int(input("Enter new width (default is 200): ") or "200")
    font_path = "fonts/" + font_path 
    scaling_factor = FONT_SCALING_FACTORS.get(os.path.basename(font_path), (6, 15)) # Use scaling factor for chosen font, or default of 6, 15.
    ascii_str = image_to_ascii("images/crabbear-better.png", output_file_name, font_path)
    print(ascii_str)
