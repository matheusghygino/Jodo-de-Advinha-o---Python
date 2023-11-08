print('****************************************')
print('*****Jogo	da	adivinhação!****')
print('****************************************\n')

import random

numero_secreto = random.randrange(1, 100)

print              ("***********Em qual dificuldade você quer jogar?**********")
dificuldade = ''
dificuldade = input("Digite (F) para fácil, (M) para médio ou (D) para difícil:\n").upper().strip()
while dificuldade != 'F' and dificuldade != "M" and dificuldade != "D":
    dificuldade = input("Valor inválido! Digite (F) para fácil, (M) para médio ou (D) para difícil:\n").upper().strip()

if dificuldade == "F":
    chances = 10
    print("Você terá 10 chances para advinhar o número!")
elif dificuldade == "M":
    print("Você terá 7 chances para advinhar o número!")
    chances = 7
elif dificuldade == "D":
    print("Você terá 5 chances para advinhar o número!")
    chances = 5

chute = int(input("Digite um número entre 1 e 100: "))

while chances > 1:
    if chute == numero_secreto:
        print("Parabéns você acertou o número secreto!")
        break
    elif chute < numero_secreto:
        print("O número digitado é menor do que o número secreto!")
        if chances == 2:
            print(f"Você ainda possui: [{chances-1}] chance! Tente novamente!")
        else:
            print(f"Você ainda possui: [{chances-1}] chances! Tente novamente!")
        chute = int(input("Digite um número: "))
    elif chute > numero_secreto:
        print("O número digitado é maior do que o número secreto! tente novamente! ")
        if chances == 2:
            print(f"Você ainda possui: [{chances-1}] chance! Tente novamente!")
        else:
            print(f"Você ainda possui: [{chances-1}] chances! Tente novamente!")
        chute = int(input("Digite um número: "))
    chances -= 1
    if chances == 1:
        print("Acabaram as chances! Você não conseguiu acertar o número secreto!")
        print(f"O número secreto era: {numero_secreto}")
    
print("Fim do Jogo!")