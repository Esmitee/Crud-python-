
import subprocess

from estado import Estado


def estado():

    while True:
        
        subprocess.run("cls", shell=True)

        print("===== MENU ESTADO =====")
        print("1 - Cadastrar Estado")
        print("2 - Listar Estados")
        print("3 - Atualizar Estado")
        print("4 - Excluir Estado")
        print("0 - Sair")

        opcao = input("Digite a opção: ")

        if opcao == "0":
            break

        
        elif opcao == "1":
            estado = Estado()

            print("Cadastro de Estado")
            estado.nome = input("Digite o nome do estado: ")

            estado.salvar()

        # Opção 2 - Listar Estados.
        elif opcao == "2":
            estado = Estado()

            estados = estado.listar()

            print("Lista de Estados:")

            for item in estados:
                print(f"ID: {item['id']} - Nome: {item['nome']}")

        elif opcao == "3":
            estado = Estado()

            print("Atualizar Estado")
            estado.id = int(input("Digite o ID do estado: "))
            estado.nome = input("Digite o novo nome do estado: ")

            estado.atualizar()

        elif opcao == "4":
            estado = Estado()

            print("Excluir Estado")
            estado.id = int(input("Digite o ID do estado: "))

        estado.excluir()

    else:
            print("Opção inválida!")

    input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    estado()

