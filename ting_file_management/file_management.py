import sys


def txt_importer(path_file):

    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, mode='r') as file:

            lines = [row.strip() for row in file]

        return lines

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
