from PIL import Image, ImageDraw, ImageFont
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def map_to_ascii(gray_val):
    ascii_val = gray_val * (len(ASCII_CHARS) - 1) // 255
    return ASCII_CHARS[int(ascii_val)]

def image_to_ascii(image_path, new_width=100):
    image = Image.open(image_path)

    (old_width, old_height) = image.size
    aspect_ratio = old_height/old_width
    new_height = int(aspect_ratio * new_width * 0.55)

    image = image.resize((new_width, new_height)).convert('L')  # convert to grayscale
    pixels = np.array(image)

    # Create a new white image with dimensions calculated for ASCII characters
    ascii_image = Image.new('RGB', (new_width * 6, new_height * 15), color=(0, 0, 0))  # adjust dimensions and color
    d = ImageDraw.Draw(ascii_image)
    font = ImageFont.load_default()

    ascii_str = ""
    for y, row in enumerate(pixels):
        ascii_row = [map_to_ascii(pixel) for pixel in row]
        ascii_str += "".join(ascii_row) + "\n"
        d.text((0, y*15), "".join(ascii_row), fill=(0, 255, 0), font=font)  # adjust vertical positioning, fill color and font

    ascii_image.save("ascii_output.png")

    return ascii_str

if __name__ == "__main__":
    ascii_str = image_to_ascii("images/ink_nodescape_1.jpg")
    print(ascii_str)
