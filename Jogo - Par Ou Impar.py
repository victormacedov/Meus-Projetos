import random

contvitorias = 0
print('=' * 40)
print('Jogo - Par ou Impar')
while True:
    print('=' * 40)
    n = int(input('Digite o seu número: '))
    print('=' * 40)
    escolhacomputador = random.randint(1, 10)
    soma = n + escolhacomputador
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {escolhacomputador} -> Total: {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print(f'Você venceu!')
            contvitorias += 1
            pergunta = (input('Você deseja continuar jogando? [S/N]')).strip().upper()[0]
            if pergunta == "N":
                break
        else:
            print('Você perdeu!')
            pergunta = (input('Você deseja continuar jogando? [S/N]')).strip().upper()[0]
            if pergunta == "N":
                break
    if tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu!')
            contvitorias += 1
            pergunta = (input('Você deseja continuar jogando? [S/N]')).strip().upper()[0]
            if pergunta == "N":
                break
        else:
            print('Você perdeu!')
            pergunta = (input('Você deseja continuar jogando? [S/N]')).strip().upper()[0]
            if pergunta == "N":
                break
print(f'O jogo acabou! Você venceu {contvitorias} vezes')
