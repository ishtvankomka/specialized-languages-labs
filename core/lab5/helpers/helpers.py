from termcolor import colored


def paint_text(text, color):
    if (len(color)):
        painted = colored(text, color)
        return painted
    else:
        return text


def text_file_saver(filename, text):
    with open(filename, "w") as file:
        file.write(text)
    print(f"text  was saved into {filename}")
