# Sistema Bancário v2 (Python)

Sistema modularizado de banco em Python com gestão de usuários, contas correntes e operações financeiras (depósito, saque e extrato), desenvolvido como parte de um desafio de curso.

## Funcionalidades

### Operações Bancárias
1. **Depósito**  
   - Valores positivos apenas.  
   - Atualiza saldo e extrato.  

2. **Saque**  
   - Limite de **3 saques diários** (máximo de **R$ 500,00 por saque**).  
   - Verifica saldo suficiente.  

3. **Extrato**  
   - Exibe histórico de movimentações e saldo atual.  

### Gestão de Usuários e Contas
4. **Criar Usuário**  
   - Cadastra: `Nome`, `CPF` (único), `Data de Nascimento`, `Endereço`.  
   - Validação de CPF duplicado.  

5. **Criar Conta Corrente**  
   - Vincula a um usuário existente via CPF.  
   - Número da conta sequencial e agência fixa (`0001`).  

6. **Listar Contas**  
   - Exibe todas as contas cadastradas com detalhes formatados.  

---

## Estrutura do Código

### Funções Principais
| Função                | Argumentos                           | Retorno                     |
|-----------------------|--------------------------------------|-----------------------------|
| `depositar(saldo, valor, extrato, /)` | Positional-only (`saldo`, `valor`, `extrato`) | `saldo`, `extrato` |
| `sacar(*, saldo, valor, extrato, ...)` | Keyword-only (`limite`, `numero_saques`, etc.) | `saldo`, `extrato`, `numero_saques` |
| `exibir_extrato(saldo, /, *, extrato)` | Híbrido (positional + keyword)      | None (exibe extrato) |

### Variáveis Globais
- `AGENCIA`: Número fixo `"0001"`.  
- `usuarios`: Lista de dicionários (armazena dados dos usuários).  
- `contas`: Lista de dicionários (armazena contas criadas).  

---

## Como Usar

1. **Menu Interativo**:  
   ```bash
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [nu] Novo usuário
   [nc] Nova conta
   [lc] Listar contas
   [q] Sair
