import random

numero_secreto = random.randint(1, 100)
tentativa = 0
palpite = int(input('Qual é o número inteiro secreto entre 1 e 100?'))

while (palpite != numero_secreto):
    tentativa += 1

    if palpite < numero_secreto:
        palpite = int(input("O número secreto é MAIOR que o seu palpite! Digite novamente:"))
    else:
        palpite = int(input("O número secreto é MENOR que o seu palpite! Digite novamente:"))
print("Parabéns, você acertou!")