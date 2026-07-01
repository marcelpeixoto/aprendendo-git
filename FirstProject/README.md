# FirstProject - Sistema de Cadastro de Alunos

Este é o meu primeiro projeto focado em Engenharia de Software, desenvolvido em Python. O objetivo principal é aplicar conceitos fundamentais de programação, boas práticas de mercado, arquitetura de código resiliente e persistência de dados.

## 🚀 Funcionalidades Atuais
* **Menu Interativo:** Navegação via terminal para gerenciamento facilitado do sistema.
* **Cadastro de Alunos:** Coleta de nome, idade e nota dos estudantes com validação em tempo real.
* **Listagem Inteligente:** Exibição de todos os alunos cadastrados e cálculo automático da média da turma.
* **Persistência Automática:** Os dados não se perdem ao fechar o terminal; são salvos e carregados de forma transparente.

## 🛡️ Conceitos de Engenharia Aplicados
* **Tratamento de Erros e Exceções:** Uso de blocos `try/except` para capturar falhas de entrada (`ValueError`), impedindo o travamento do sistema caso o usuário digite letras onde são esperados números. Trata também exceções de ficheiros corrompidos (`JSONDecodeError`).
* **Validação de Regras de Negócio:** Aplicação de travas lógicas para garantir a integridade dos dados (limitação de idade entre 1 e 110 anos, e notas entre 0.0 e 10.0).
* **Princípio DRY (Don't Repeat Yourself):** Centralização de lógicas repetitivas em funções reaproveitáveis.
* **Encapsulamento:** Isolamento da lógica complexa de validação e de manipulação de ficheiros em funções genéricas, mantendo o fluxo do menu principal limpo, legível e focado no negócio.
* **Persistência de Dados (JSON):** Utilização da biblioteca nativa `json` para serializar e desserializar dicionários e listas Python, convertendo-os num formato de armazenamento universal permanente (`alunos.json`).
* **Caminhos Dinâmicos (Multiplataforma):** Uso da biblioteca `os` para mapear o diretório do script em execução em tempo de execução (`os.path.join`). Isto garante que o sistema funcione perfeitamente e crie os ficheiros no local correto, seja no Windows, Mac ou Linux.

## 🛠️ Tecnologias Utilizadas
* Python 3
* Git & GitHub