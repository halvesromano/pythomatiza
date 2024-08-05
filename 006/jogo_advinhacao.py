import random from random

numero_secreto = random.randint(1, 100)
palpite = input('Qual é o número inteiro secreto entre 1 e 100?')
tentativa = 0

while palpite != numero_secreto