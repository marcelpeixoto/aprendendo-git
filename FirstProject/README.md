# FirstProject - Sistema de Gestão de Alunos (CRUD em Python)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-orange.svg)](https://git-scm.com/)

Este é o meu primeiro projeto focado em Engenharia de Software, desenvolvido em Python. O objetivo principal é aplicar conceitos fundamentais de programação, boas práticas de mercado (*Clean Code*), arquitetura de código resiliente e persistência de dados em arquivos.

---

## Funcionalidades (CRUD Completo)

O sistema implementa o ciclo completo do **CRUD** (Create, Read, Update, Delete) via interface interativa de terminal:

* **[C]reate - Cadastrar Aluno:** Registro de nome, idade e nota com validação em tempo real.
* **[R]ead - Listar Alunos:** Exibição detalhada de todos os estudantes e cálculo automático da média da turma.
* **[U]pdate - Editar Cadastro:** Atualização dos dados de um aluno existente sem perder o histórico do arquivo.
* **[D]elete - Excluir Aluno:** Remoção de cadastros diretamente do sistema com recalculo automático dos dados.
* **💾 Persistência Automática:** Integração transparente com arquivo `JSON`. Os dados são preservados mesmo após o fechamento do sistema.

---

## Demonstração da Interface (Terminal)

```text
--- SISTEMA DE CADASTRO ---
1. Cadastrar aluno
2. Listar alunos
3. Editar aluno
4. Excluir aluno
5. Sair
Escolha uma opção:
```
## Conceitos de Engenharia Aplicados
Arquitetura Modular & Clean Code: Funções com responsabilidades únicas, mantendo a função principal (main) enxuta, legível e atuando apenas como orquestradora.

Tratamento de Erros e Exceções: Uso de blocos try/except para capturar falhas de entrada (ValueError), impedindo o travamento do sistema. Trata também arquivos inexistentes ou corrompidos (JSONDecodeError).

Validação de Regras de Negócio: Travas lógicas customizadas para garantir a integridade das informações (idade entre 1 e 110 anos, e notas entre 0.0 e 10.0).

Princípio DRY (Don't Repeat Yourself): Centralização e reuso de funções de validação de dados (ler_inteiro, ler_float).

Persistência de Dados (JSON): Manipulação da biblioteca nativa json para serialização e desserialização de estruturas de dados.

Caminhos Dinâmicos (Multiplataforma): Uso da biblioteca os para mapear os diretórios em tempo de execução (os.path.join), garantindo execução nativa em Windows, macOS e Linux.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Persistência: JSON (JavaScript Object Notation)

Controle de Versão: Git & GitHub

🔧 Como Executar o Projeto
1. Clone o repositório:

```Bash
git clone git clone https://github.com/marcelpeixoto/aprendendo-git.git

2. Acesse a pasta do projeto:

```Bash
cd FirstProject

3. Execute o script:

```Bash
python main.py