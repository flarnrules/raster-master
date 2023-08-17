from PIL import Image

def image_to_ascii(image_path, width=100):
    image = Image.open(image_path)
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width * 0.55)
    resized_image = image.resize((width, new_height))
    grayscale_image = resized_image.convert("L")

    characters = "@%#*+=-:. "
    pixel_values = grayscale_image.getdata()
    factor = len(characters) / 256
    ascii_str = "".join([characters[int(value * factor)] for value in pixel_values])
    ascii_image = [ascii_str[index: index + width] for index in range(0, len(ascii_str), width)]
    return "\n".join(ascii_image)

ascii_art = image_to_ascii("image.png")
print(ascii_art)
with open("output.txt", "w") as file:
    file.write(ascii_art)
