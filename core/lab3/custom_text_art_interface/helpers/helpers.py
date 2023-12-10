def text_file_saver(filename, text):
    with open(filename, "w") as file:
        file.write(text)
    print(f"text  was saved into {filename}")
