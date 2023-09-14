import random

# Gere um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicialize o número de tentativas
tentativas = 0

print("Bem-vindo ao jogo de adivinhação de números!")
print("Estou pensando em um número entre 1 e 100.")

while True:
    try:
        # Peça ao jogador para adivinhar o número
        palpite = int(input("Digite seu palpite: "))

        # Incremente o número de tentativas
        tentativas += 1

        # Verifique se o palpite está correto
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
    except ValueError:
        print("Por favor, digite um número válido.")
