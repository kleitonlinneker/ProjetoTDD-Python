import unittest
from produtos import Produto

#DEFINIÇÃO
class TesteProduto(unittest.TestCase):
    def setUp(self):
        self.gerenciamento = Produto(':memory:')


    #TESTE DA FUNÇÃO ADICIONAR PRODUTO
    def teste_add_produto(self):
        self.gerenciamento.add_produto(1, "Produto A", 10.0, "Fornecedor A")
        produto = self.gerenciamento.exibir_produto(1)
        self.assertEqual(produto, (1, "Produto A", 10.0, "Fornecedor A"))

    #TESTE DA FUNÇÃO DELETAR PRODUTO
    def teste_delete_produto(self):
        self.gerenciamento.add_produto(1, "Produto A", 10.0, "Fornecedor A")
        self.gerenciamento.delete_produto(1)
        self.assertEqual(len(self.gerenciamento.exibir_todos_produtos()), 0)

    #TESTE DA FUNÇÃO UPDATE DE PRODUTO
    def teste_update_produto(self):
        self.gerenciamento.add_produto(1, "Produto A", 10.0, "Fornecedor A")
        self.gerenciamento.update_produto(1, "Novo Produto A", 15.0, "Novo Fornecedor A")
        produto = self.gerenciamento.exibir_produto(1)
        self.assertEqual(produto, (1, "Novo Produto A", 15.0, "Novo Fornecedor A"))

    #TESTE DA FUNÇÃO EXIBIR TODOS OS PRODUTOS
    def teste_exibir_todos_produtos(self):
        self.gerenciamento.add_produto(1, "Produto A", 10.0, "Fornecedor A")
        self.gerenciamento.add_produto(2, "Produto B", 15.0, "Fornecedor B")
        self.assertEqual(len(self.gerenciamento.exibir_todos_produtos()), 2)

    #TESTE DA FUNÇÃO EXIBIR UM PRODUTO
    def teste_exibir_produto(self):
        self.gerenciamento.add_produto(1, "Produto A", 10.0, "Fornecedor A")
        produto = self.gerenciamento.exibir_produto(1)
        self.assertIsNotNone(produto)
        self.assertEqual(produto, (1, "Produto A", 10.0, "Fornecedor A"))

        nao_existe_produto = self.gerenciamento.exibir_produto(99)
        self.assertIsNone(nao_existe_produto)

#EXECUTAR OS TESTES QUANDO O AQUIVO FOR ABERTO
if __name__ == '__main__':
    unittest.main()
