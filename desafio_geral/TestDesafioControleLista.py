import unittest
from seu_arquivo import (
    adicionar_numero,
    remover_numero,
    soma_lista,
    media_lista
)

class TestLista(unittest.TestCase):

    def setUp(self):
        self.lista = [10, 20, 30]

    def test_adicionar_numero(self):
        adicionar_numero(self.lista, 40)
        self.assertIn(40, self.lista)

    def test_remover_numero(self):
        remover_numero(self.lista, 20)
        self.assertNotIn(20, self.lista)

    def test_remover_numero_inexistente(self):
        with self.assertRaises(ValueError):
            remover_numero(self.lista, 100)

    def test_soma_lista(self):
        self.assertEqual(soma_lista(self.lista), 60)

    def test_media_lista(self):
        self.assertEqual(media_lista(self.lista), 20)

    def test_media_lista_vazia(self):
        self.assertEqual(media_lista([]), 0)

if __name__ == "__main__":
    unittest.main()
