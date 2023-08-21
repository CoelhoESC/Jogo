from random import randint

secreto = ['PERFUME', 'VASSOURA', 'GARRAFA', 'ENERGETICO', 'MACACO', 'GIRRAFA', 'CELULAR', 'PARALELEPIPEDO']
digitadas = []
vidas = 3
Num = randint(0, 7)
print(f'{"Jogo para adivinhar a palavra".center(40)}')
print('-' * 40)
while True:
    if vidas <= 0:
        print('Você perdeu! Suas vidas acabaram!')
        print(f'A palavra era: {secreto[Num]}')
        break
    print(f'Você tem {vidas} vida(s)!')
    letras = input('Digite uma letra: ').strip().upper()
    if len(letras) > 1:
        if letras == secreto[Num]:
            print('PARABÉNS!! VOCÊ GANHOU!!')
            print(f'A palavra secreta é: {secreto[Num]}')
            break
        else:
            print('Digite a Palavra quando você ter certeza!!')
            vidas -= 1
            continue  # Para voltar ao While
    if letras.isnumeric():
        print('Número não pode!! Apenas letras!')
        continue
    digitadas.append(letras)
    if letras in secreto[Num]:
        print(f'Uhuuu!! A letra "{letras}" está na palavra secreta!')
    else:
        print(f'VISH!! A letra "{letras}" NÃO ESTÁ na palavra secreta!')
        vidas -= 1
        digitadas.pop()
    secreto_temporario = ''  # Verificando se a palavra que esta guardada na lista, esta na palavra secreta!
    for letra_secreta in secreto[Num]:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto[Num]:
        print('PARABLES!! VOCÊ GANHOU!!')
        print(f'A palavra secreta é: {secreto[Num]}')
        break
    else:
        print(f'A palavra secreta: {secreto_temporario}')
    print()
