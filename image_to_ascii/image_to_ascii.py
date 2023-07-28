# Import necessary packages
from PIL import Image
import numpy as np

# The set of ASCII characters to use to create the output art
#ASCII_CHARS = "@%#*+=-:. "
ASCII_CHARS = "@%#*+=-:. "

# Function to map a grayscale value to an ASCII character
def map_to_ascii(gray_val):
    # Map the gray_val which is in range [0, 255] to range [0, len(ASCII_CHARS)-1]
    ascii_val = gray_val * (len(ASCII_CHARS) - 1) // 255
    return ASCII_CHARS[int(ascii_val)]


# Function to convert image to ascii
def image_to_ascii(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale
    image = image.convert("L")

    # Resize the image
    # This might need some playing around with to look right on your terminal
    image = image.resize((150, 35)) # w, h

    # Convert image data to numpy array
    image_np = np.array(image)

    # Map each grayscale value in the image to an ASCII character
    ascii_img = ""
    for row in image_np:
        ascii_row = [map_to_ascii(pixel) for pixel in row]
        ascii_img += "".join(ascii_row) + "\n"

    return ascii_img

# Run the function and print the result
print(image_to_ascii("images/ink_nodescape_1.jpg"))
