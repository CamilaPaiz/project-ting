import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """processa arquivo e gera dicionário"""
    # ignorar arquivos que já tenham sido processados anteriormente
    for path in instance._data:
        if path == path_file:
            return

    lines = txt_importer(path_file)
    if lines is not None:
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(path_file)
        print(data)


def remove(instance):
    """remove primeiro arquivo processado"""
    if len(instance) > 0:
        file = instance.dequeue()
        print(f"Arquivo {file} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    """Apresenta as informações superficiais processadas"""
    if position < 0 or position >= len(instance):
        print("Posição inválida", file=sys.stderr)
    else:
        file = instance.search(position)
        lines = txt_importer(file)
        if lines:
            data = {
                "nome_do_arquivo": file,
                "qtd_linhas": len(lines),
                "linhas_do_arquivo": lines,
            }
            print(data)
