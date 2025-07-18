# Projeto-Sistema-Bancario-com-Python
Projeto de estudo, construindo projetos práticos com o conhecimento em Python adquirido ao longo dos estudos.

Este projeto consiste em um sistema bancário simples, desenvolvido em Python, com objetivo educacional. O sistema permite que o usuário realize operações bancárias básicas como depósito, saque e consulta de extrato, por meio de uma interface de linha de comando.

## Funcionalidades

- **Depósito:** Permite ao usuário depositar valores na conta, com verificação de valores válidos.
- **Saque:** Permite realizar saques, respeitando o limite de saldo, limite máximo por saque (R$ 500) e um número máximo de 3 saques diários.
- **Extrato:** Mostra todas as movimentações financeiras realizadas e o saldo atual da conta.
- **Saída:** Opção para encerrar o programa a qualquer momento.

## Como usar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/DanielCauldron/Projeto-Sistema-Bancario-com-Python.git
   cd Projeto-Sistema-Bancario-com-Python
   ```

2. **Execute o sistema:**
   ```bash
   python sistema-Bancario.py
   ```

3. **Siga as instruções do menu para realizar operações:**
   - `[d]` Depositar
   - `[s]` Sacar
   - `[e]` Extrato
   - `[q]` Sair

## Exemplo de uso

```text
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 1000
Deposito com sucesso!!

=> s
Informe o valor do saque: 200
Saque efetuado com sucesso!!

=> e
================ EXTRATO ================
Deposito de R$ 1000.00 
Saque de R$ 200.00

Saldo: R$ 800.00
==========================================
```

## Estrutura do Projeto

- `sistema-Bancario.py`: Código-fonte principal do sistema bancário.
- `README.md`: Este arquivo de documentação.
- `LICENSE`: Licença MIT.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

Desenvolvido por [Daniel Caldeirão](https://github.com/DanielCauldron)
