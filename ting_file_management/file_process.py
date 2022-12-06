from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):

    for i in instance._data:
        if path_file == i['nome_do_arquivo']:
            return 'path already used'

    lines = txt_importer(path_file)

    lines_qtty = len(lines)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lines_qtty,
        "linhas_do_arquivo": lines
    }

    instance.enqueue(new_dict)

    sys.stdout.write(f"{new_dict}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
