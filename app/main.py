def copy_file(argument: str) -> None:
    if argument in ["", " "] or argument.count(" ") != 2:
        return None

    command, file1, file2 = argument.split(" ")

    if command != "cp" or file1 == file2:
        return None

    try:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            for line in file_in.readlines():
                file_out.write(line)
    except FileNotFoundError:
        return None
