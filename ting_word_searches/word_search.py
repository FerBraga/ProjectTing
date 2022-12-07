def exists_word(word, instance):

    for line in instance._data:
        if word not in line:
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
