from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    results = []

    for file in instance._data:
        lines_with_word = []
        lines = txt_importer(file)
        for i, line in enumerate(lines, 1):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": i})

        if lines_with_word:
            result = {
                "palavra": word,
                "arquivo": file,
                "ocorrencias": lines_with_word,
            }
            results.append(result)

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
