class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial):
        self.saldo_inicial = saldo_inicial
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.transacoes = []  # Lista para armazenar histórico de transações

    def deposito(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito: R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(f"Saque: R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo inicial: R$ {self.saldo_inicial:.2f}")
        print("Histórico de transações:")
        for t in self.transacoes:
            print(t)


# Exemplo de uso
minha_conta = ContaBancaria(numero_conta="12345", saldo_inicial=1000)
minha_conta.deposito(500)
minha_conta.saque(200)
minha_conta.extrato()
