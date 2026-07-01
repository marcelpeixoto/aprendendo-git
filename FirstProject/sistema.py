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
    print("3. Sair")

#Aqui vamos guardar os alunos futuramente
lista_alunos = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        #Vamos coletar os dados do aluno
        nome = input("Digite o nome do aluno: ")
        idade = ler_inteiro("Digite a idade do aluno: ", "Idade inválida. Digite um número inteiro.(Exemplo: 20)", 1, 110)
        nota = ler_float("Digite a nota do aluno: ", "Nota inválida. Digite um valor decimal.(Exemplo: 8.5)", 0, 10.0)
        print(f"Nota {nota} cadastrada com sucesso!")

                
        #Criando um dicionário para armazenar os dados do aluno
        aluno = {
            "nome": nome,
            "idade": idade,
            "nota": nota,
        }
        lista_alunos.append(aluno) #Adicionando o aluno à lista
        print(f"aluno {nome} cadastrado com sucesso!")
    elif opcao == "2":
        print("\n--- LISTA DE ALUNOS ---")
        soma_notas = 0
        for aluno in lista_alunos:
            soma_notas += aluno["nota"]
            print(f"nome: {aluno['nome']}")
        if lista_alunos:
            media = soma_notas / len(lista_alunos)
            print(f"\nMédia das notas: {media:.2f}")
    elif opcao == "3":
        print("Saindo do sistema...")
        break #isso vai encerrar o loop e sair do programa
    else:
        print("Opção inválida. Tente novamente.")
