menu = """

[1] Depositar
[2] Sacar
[3] Visualizar extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

   opcao = input(menu)

   if opcao == "1":
      valor = float(input("Informe o valor de depósito: "))

      if valor > 0:
         saldo += valor
         extrato += f"Depósito: R$ {valor:.2f}\n"

      else:
         print(f"Operação falhou! O valor informado de R$ {valor:.2f} é inválido.")

   elif opcao == "2":
      valor = float(input("Informe o valor do saque: "))
     
      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >=LIMITE_SAQUES

      if excedeu_saldo:
         print(f"Operação falhou! Você não tem saldo suficiente. Seu saldo atual é de {saldo:.2f}")
         continue

      if excedeu_saques:
         print(f"Operação falhou! Número de saques excedeu o limite de {LIMITE_SAQUES} saques.")
         continue

      if excedeu_limite:
         print(f"Operação falhou! Valor do saque excedeu o limite de R$ {limite:.2f}")
         continue
   
      elif valor > 0:
         saldo -= valor
         extrato += f"Saque R$ {valor:.2f}\n"
         numero_saques += 1
         print (f"Valor de saque: R$ {valor:.2f}\n")
         print (f"Saldo após o saque: R$ {saldo-valor:.2f}\n")

      else:
         print("Operação falhou! Valor informado é inválido")
   
   elif opcao == "3":
         print ("\n================ EXTRATO ================")
         print ("Não foram realizadas movimentações." if not extrato else extrato)
         print (f"\nSaldo: R$ {saldo: .2f}")
         print ("=========================================")
   
   elif opcao == "0":
      break

   else: 
      print("Operação inválida, por favor selecione novamente a opção desejada")