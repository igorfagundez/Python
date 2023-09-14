import random 

numero_secreto = random.randint (1, 100)

tentativas = 0

print("Bem-Vindo ao jogo de adivinhação de números!")
print("Estou pensando em um número entre 1 e 100.")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break 
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")