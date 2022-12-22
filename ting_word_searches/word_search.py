def exists_word(word, instance):

    for line in instance._data:
        if word not in line:
            return []
        else:
            {
                "palavra": word,
                "arquivo": instance._data['nome_do_arquivo'],
                "ocorrencias": fsdfs
            }


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
