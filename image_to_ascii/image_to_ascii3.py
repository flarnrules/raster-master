from PIL import Image, ImageDraw, ImageFont
import numpy as np

ASCII_CHARS = "@%$#89|/+=<>_-,."

def map_to_ascii(gray_val):
    ascii_val = gray_val * (len(ASCII_CHARS) - 1) // 255
    return ASCII_CHARS[int(ascii_val)]

def gradient_color(x, width):
    red_orange = (255, 69, 0)
    orange = (255, 165, 0)
    dark_brown_black = (50, 25, 0)

    if x < width * 1 / 3:
        t = x / (width * 1 / 3)
        return tuple(map(lambda start, end: int(start * (1 - t) + end * t), red_orange, orange))
    elif x < width * 2 / 3:
        t = (x - width * 1 / 3) / (width * 1 / 3)
        return tuple(map(lambda start, end: int(start * (1 - t) + end * t), orange, dark_brown_black))
    else:
        return dark_brown_black

def image_to_ascii(image_path, new_width=600):
    image = Image.open(image_path)
    (old_width, old_height) = image.size
    aspect_ratio = old_height/old_width
    new_height = int(aspect_ratio * new_width * 0.55)
    
    image = image.resize((new_width, new_height)).convert('L')  # convert to grayscale
    pixels = np.array(image)
    
    ascii_image = Image.new('RGB', (new_width * 6, new_height * 15), color=(250, 250, 143))
    d = ImageDraw.Draw(ascii_image)
    font = ImageFont.load_default()
    
    ascii_str = ""
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            char = map_to_ascii(pixel)
            fill_color = gradient_color(x, new_width)
            d.text((x * 6, y * 15), char, fill=fill_color, font=font)
            ascii_str += char
        ascii_str += "\n"

    ascii_image.save("knightriders2.png")
    
    return ascii_str

if __name__ == "__main__":
    ascii_str = image_to_ascii("images/knightriders.png")
    print(ascii_str)