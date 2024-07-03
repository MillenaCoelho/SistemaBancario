menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = input("Informe o valor do depósito: ")
        if valor.replace('.', '', 1).isdigit():  # Verifica se a entrada é um número
            valor = float(valor)
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Entrada inválida! Por favor, insira um número válido.")

    elif opcao == "s":
        valor = input("Informe o valor do saque: ")
        if valor.replace('.', '', 1).isdigit():  # Verifica se a entrada é um número
            valor = float(valor)
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Entrada inválida! Por favor, insira um número válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Saindo... Obrigado por utilizar o nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
