from PIL import Image


FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def add_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def convert_image_to_grayscale(image):
    img = Image.open(image)
    gray_img = img.convert("L")
    return gray_img

