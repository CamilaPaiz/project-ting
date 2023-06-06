from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        """Aqui enfileira ao final"""
        self._data.append(value)

    def dequeue(self):
        """Aqui desenfileira pelo começo"""
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        """Aqui retorna um valor da fila a partir de um index válido"""
        if len(self._data) == 0 or index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
