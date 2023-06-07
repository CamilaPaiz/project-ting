def exists_word(word, instance):
    results = []

    for file_data in instance._data:
        file_name = file_data["nome_do_arquivo"]
        lines_with_word = [
            {"linha": i + 1}
            for i, line in enumerate(file_data["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]

        if lines_with_word:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": lines_with_word,
            }
            results.append(result)

    return results


def search_by_word(word, instance):
    results = []

    for file_data in instance._data:
        file_name = file_data["nome_do_arquivo"]
        lines_with_word = []

        for i, line in enumerate(file_data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                line_data = {
                    "linha": i + 1,
                    "conteudo": line.strip()
                }
                lines_with_word.append(line_data)

        if lines_with_word:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": lines_with_word
            }
            results.append(result)

    return results
