from random import randint
from time import sleep
while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('=' * 40)
    print('JOGO -> JOKENPO!')
    print('''Suas opções:
        [0] PEDRA
        [1] PAPEL
        [2] TESOURA''')
    jogador = int(input('escolha sua opção: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    while True:
        itens = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)
        if jogador < 0 or jogador > 2:
            print('Jogada Inválida! Tente novamente')
            print('=' * 40)
            print('''Suas opções:
            [0] PEDRA
            [1] PAPEL
            [2] TESOURA''')
            jogador = int(input('escolha sua opção: '))
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!')
        else:
            print('Jogada Válida!')
            break
    print('=' * 40)
    print('O Computador jogou {}' .format(itens[computador]))
    print('O Jogador jogou {}' .format(itens[jogador]))
    print('=' * 40)
    if computador == 0:
       if jogador == 0:
            print('o jogo empatou')
       elif jogador == 1:
            print('o jogador venceu')
       elif jogador == 2:
           print('o computador venceu')
    elif computador == 1:
        if jogador == 0:
            print('o computador venceu')
        elif jogador == 1:
            print('o jogo empatou')
        elif jogador == 2:
            print('o jogador venceu')
    elif computador == 2:
        if jogador == 0:
            print('o jogador venceu')
        elif jogador == 1:
            print('o computador venceu')
        elif jogador == 2:
            print('o jogo empatou')
    print('=' * 40)
    pergunta = str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        print('Obrigado por jogar! Volte novamente.')
        break
