# Sistema bancário simples

<br>

## Objetivo 

<br>

Criar um sistema bancário onde o cliente possa realizar operações básicas como:
<br>

- Depositar dinheiro;
- Sacar dinheiro;
- Visualizar extrato.

<br>

## Regras do sistema

<br>

- Cliente pode realizar até *3 saques no dia*;
- Valor máximo por saque é de *R$ 500,00*;
- Extrato exibe todas as movimentações realizadas (*depósitos e saques*).

<br>

## Funcionalidades

<br>

1. **Depósito**: O cliente informa o valor a ser depositado, que é adicionado ao saldo.


2. **Saque**: O cliente informa o valor a ser sacado. O sistema verifica se:
- Há saldo suficiente;
- O valor solicitado não excede o limite de saque;
- O número de saques diários ainda não atingiu o limite.
   

   *Caso todos os critérios sejam atendidos, o valor é subtraído do saldo.*


3. **Extrato**: Mostra todas as movimentações (depósitos e saques) e o saldo atual do cliente.

<br>

## Requisitos

- Python 3.# sistema-bancario
