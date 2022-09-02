import random

user_name = input("Olá usuário, por favor, digite seu nome: ")

print(f'\n{user_name} a qualquer momento poderá finalizar o programa digitando "q"; :) \n ')


def somar_valores(a, b):
    return a + b


def subtrair_valores(a, b):
    return a - b


def multiplicar_valores(a, b):
    return a * b


def dividir_valores(a, b):
    return a / b


while True:
    try:
        a = input("\nDigite o primeiro valor: ")

        if a.strip() == 'q':
            break

        a = int(a)

        b = input("Digite o segundo valor: ")

        if b.strip() == 'q':
            break

        b = int(b)

        operacao = random.randint(0, 3)
        result = 0

        if operacao == 0:
            result = somar_valores(a, b)
            print(f"\n{user_name} a soma de {a} com {b} é: {result}")

        elif operacao == 1:
            result = subtrair_valores(a, b)
            print(f"\n{user_name} a subtração de {a} por {b} é: {result}")

        elif operacao == 2:
            result = multiplicar_valores(a, b)
            print(f"\n{user_name} a multiplicação de {a} por {b} é: {result}")

        else:
            result = dividir_valores(a, b)
            print(f"\n{user_name} a divisão de {a} por {b} é: {result}")
    except ValueError:
        print("\nPor favor insira apenas valores numéricos ou 'q'!!!\n")
        break
