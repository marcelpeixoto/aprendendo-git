import json
import os
# Cria/Define o caminho do arquivo JSON para armazenar os dados dos alunos
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "alunos.json") 

# Função para salvar os dados dos alunos em um arquivo JSON
def salvar_dados(lista_alunos):
    try:
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(lista_alunos, arquivo, indent=4)
            print("Dados salvos em arquivo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# Função para carregar os dados dos alunos de um arquivo JSON
def carregar_dados():
    if not os.path.exists(CAMINHO_ARQUIVO) or os.path.getsize(CAMINHO_ARQUIVO) == 0:
        salvar_dados([])
        return []

    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            if isinstance(dados, list):
                return dados
            return []
    except FileNotFoundError:
        print("Arquivo não encontrado. Iniciando com uma lista vazia.")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Iniciando com uma lista vazia.")
        return []
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return []

def ler_inteiro(mensagem, mensagem_erro, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"A idade deve ser entre {minimo} e {maximo}.")
        except ValueError:
            print(mensagem_erro)

def ler_float(mensagem, mensagem_erro, minimo, maximo):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"A nota deve ser entre {minimo} e {maximo}.")
        except ValueError:
            print(mensagem_erro)

def exibir_menu():
    print("\n--- SISTEMA DE CADASTRO ---")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Editar area de alunos")
    print("4. Excluir alunos")
    print("5. Sair")

#Função para exclusão de alunos do sistema.
def excluir_aluno(lista_alunos):
        print("\n----------Excluir Aluno----------------\n")
        nome_busca = input("Digite o nome do aluno a ser excluído: ")

        aluno_encontrado = None

        #Varremos a lista procurando o aluno pelo nome
        for alunos in lista_alunos:
            # usamos .lower() para ignorar letras maíusculas/minusculas desnecessárias.
            if alunos['nome'].lower() == nome_busca.lower():
                aluno_encontrado = alunos
                break
        
        if aluno_encontrado:
            lista_alunos.remove(aluno_encontrado)
            salvar_dados(lista_alunos)
            print(f"Aluno {aluno_encontrado["nome"]} removido com sucesso!")
        else:
            print("Aluno não encontrado no sistema")

        
def main():
    lista_alunos = carregar_dados()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            idade = ler_inteiro("Digite a idade do aluno: ", "Idade inválida. Digite um número inteiro.(Exemplo: 20)", 1, 110)
            nota = ler_float("Digite a nota do aluno: ", "Nota inválida. Digite um valor decimal.(Exemplo: 8.5)", 0, 10.0)
            print(f"Nota {nota} cadastrada com sucesso!")

            aluno = {
                "nome": nome,
                "idade": idade,
                "nota": nota,
            }
            lista_alunos.append(aluno)
            print(f"aluno {nome} cadastrado com sucesso!")
            salvar_dados(lista_alunos)
        elif opcao == "2":
            print("\n--- LISTA DE ALUNOS ---")
            if lista_alunos:
                soma_notas = 0
                for aluno in lista_alunos:
                    soma_notas += aluno["nota"]
                    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")

                media = soma_notas / len(lista_alunos)
                print(f"\nMédia das notas: {media:.2f}")
            else:
                print("Nenhum aluno cadastrado no sistema ainda.")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        elif opcao == "3":
            print("Em breve: UPDATE de edição de alunos.")
        elif opcao == "4":
            excluir_aluno(lista_alunos)

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
