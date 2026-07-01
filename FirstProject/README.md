# FirstProject - Sistema de Cadastro de Alunos

Este é o meu primeiro projeto focado em Engenharia de Software, desenvolvido em Python. O objetivo principal é aplicar conceitos fundamentais de programação, boas práticas de mercado e arquitetura de código resiliente.

## 🚀 Funcionalidades Atuais
* **Menu Interativo:** Navegação via terminal para gerenciamento do sistema.
* **Cadastro de Alunos:** Coleta de nome, idade e nota dos estudantes.

## 🛡️ Conceitos de Engenharia Aplicados
* **Tratamento de Erros e Exceções:** Implementação de blocos `try/except` para capturar falhas de entrada (`ValueError`), impedindo que o sistema quebre caso o usuário digite letras onde são esperados números.
* **Validação de Regras de Negócio:** Aplicação de travas lógicas para garantir que dados façam sentido no mundo real (limitação de idade entre 1 e 120 anos, e notas entre 0.0 e 10.0).
* **Princípio DRY (Don't Repeat Yourself):** Evitou-se a repetição de blocos de validação criando estruturas reaproveitáveis.
* **Encapsulamento:** Isolamento da lógica complexa de validação em funções genéricas (`ler_inteiro` e `ler_float`), mantendo o fluxo do menu principal limpo, legível e focado apenas na execução do negócio.

## 🛠️ Tecnologias Utilizadas
* Python 3
* Git & GitHub