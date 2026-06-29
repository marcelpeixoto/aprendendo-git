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
        idade = int(input("Digite a idade do aluno: "))
        nota = float(input("Digite a nota do aluno: "))
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
