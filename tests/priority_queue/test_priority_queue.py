import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Quando um arquivo prioritário (com menos de 5 linhas) é
    # adicionado à fila de prioridades, este arquivo ficará
    # após" todos os arquivos prioritários já inseridos,
    # mas ficará "antes" de todos os arquivos não-prioritários já inseridos.

    # Quando um arquivo não-prioritário (com 5 linhas ou mais)
    # é adicionado à fila de prioridades, este arquivo ficará
    # após" todos os arquivos já inseridos.
    priorityQueue = PriorityQueue()
    # implementa teste para função enqueue para priority_file

    file1 = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["line1", "line2", "line3"],
    }
    file2 = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["line1", "line2", "line3", "line4"],
    }
    priorityQueue.enqueue(file1)
    priorityQueue.enqueue(file2)
    assert len(priorityQueue) == 2
    assert len(priorityQueue.high_priority) == 2
    assert len(priorityQueue.regular_priority) == 0

    # implementa teste para função enqueue para regular_file

    file3 = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [
            "line1",
            "line2",
            "line3",
            "line4",
            "line5",
            "line6",
            "line7",
        ],
    }
    priorityQueue.enqueue(file3)
    assert len(priorityQueue) == 3
    assert len(priorityQueue.regular_priority) == 1

    # implementa teste para função dequeue para priorityQueue

    dequeuedQueue_file = priorityQueue.dequeue()
    assert dequeuedQueue_file == file1
    assert len(priorityQueue) == 2

    # implementa teste para função search
    searched_file = priorityQueue.search(0)
    assert searched_file == file2

    # implementa teste para função search com index inválido
    with pytest.raises(IndexError):
        priorityQueue.search(3)
