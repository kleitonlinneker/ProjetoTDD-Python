import sqlite3

class Produto:
    #CONEXÃO COM O BANCO DE DADOS E CRIAÇÃO DA TABELA PRODUTOS
    def __init__(self, bancodedados_produto):
        self.conn = sqlite3.connect(bancodedados_produto)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS produtos (
                cod INTEGER PRIMARY KEY,
                nome TEXT,
                preco REAL,
                fornecedor TEXT
            )
            '''
        )

    #FUNÇÃO QUE ADICIONA UM PRODUTO
    def add_produto(self, cod, nome, preco, fornecedor):
        self.cursor.execute(
            '''
            INSERT INTO produtos (cod, nome, preco, fornecedor) VALUES (?, ?, ?, ?)
            ''',
            (cod, nome, preco, fornecedor)
        )
        self.conn.commit()

    #FUNÇÃO QUE DELETA UM PRODUTO
    def delete_produto(self, cod):
        self.cursor.execute(
            '''
            DELETE FROM produtos WHERE cod = ?
            ''',
            (cod,)
        )
        self.conn.commit()

    #FUNÇÃO QUE FAZ O UPDATE DE UM PRODUTO
    def update_produto(self, cod, nome, preco, fornecedor):
        self.cursor.execute(
            '''
            UPDATE produtos SET nome = ?, preco = ?, fornecedor = ? WHERE cod = ?
            ''',
            (nome, preco, fornecedor, cod)
        )
        self.conn.commit()

    #FUNÇÃO QUE EXIBE TODOS OS PRODUTOS
    def exibir_todos_produtos(self):
        self.cursor.execute(
            '''
            SELECT * FROM produtos
            '''
        )
        return self.cursor.fetchall()

    #FUNÇÃO QUE EXIBE UM PRODUTO
    def exibir_produto(self, cod):
        self.cursor.execute(
            '''
            SELECT * FROM produtos WHERE cod = ?
            ''',
            (cod,)
        )
        return self.cursor.fetchone()
    
