
import database as db


class Estado:

        def __init__(self):
            self.id = 0
            self.nome = ""
            self.sigla = ""
            self.conexao = ConexaoMySQL()

        def salvar(self):
            conn = self.conexao.abrir()

        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO estado (nome) VALUES (%s)"
                    cursor.execute(sql, (self.nome,))
                    conn.commit()

                    self.id = cursor.lastrowid
                    print("Estado cadastrado com sucesso!")

            except Exception as erro:
                print(f"Erro ao salvar estado: {erro}")

            finally:
                self.conexao.fechar()

        def listar(self):
            conn = self.conexao.abrir()
        estados = []

        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM estado"
                    cursor.execute(sql)
                    estados = cursor.fetchall()

            except Exception as erro:
                print(f"Erro ao listar estados: {erro}")

            finally:
                self.conexao.fechar()

        return estados

        def atualizar(self):
            conn = self.conexao.abrir()

        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "UPDATE estado SET nome = %s WHERE id = %s"
                    cursor.execute(sql, (self.nome, self.id))

                    if cursor.rowcount > 0:
                        conn.commit()
                        print("Estado atualizado com sucesso!")
                    else:
                        print("Nenhum estado foi atualizado.")

            except Exception as erro:
                print(f"Erro ao atualizar estado: {erro}")

            finally:
                self.conexao.fechar()

        def excluir(self):
            conn = self.conexao.abrir()

        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM estado WHERE id = %s"
                    cursor.execute(sql, (self.id,))

                    if cursor.rowcount > 0:
                        conn.commit()
                        print("Estado excluído com sucesso!")
                    else:
                        print("Nenhum estado foi encontrado.")

            except Exception as erro:
                print(f"Erro ao excluir estado: {erro}")

            finally:
                self.conexao.fechar()
