import random
import os

def getWords(file):
    words=[]
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line)
    return words


def startGame(words, win=0, defeat=0):
    index = random.randint(0, len(words) - 1)
    word = words[index]
    word = word.casefold()
    game = {}
    game['word'] = [i for i in word if i != '\n']
    game['progress'] = ['' for i in word if i != '\n']
    game['lives'] = 7
    game['exit'] = False
    game['win'] = win
    game['defeat'] = defeat
    return game


def update(game, letter):
    mistake = 1
    large = len(game['word'])
    for i in range(0,large):
        if letter == game['word'][i] or stress(letter) == game['word'][i]:
            game['progress'][i] = game['word'][i]
            mistake *= 0
    game['lives'] -= mistake
    return game


def printMan(lives):
    bodies = [0, 119, 237, 353, 468, 582, 696, 809, 919]

    with open('hangman.txt', 'r', encoding='utf-8') as f2:
        body = bodies[7-lives]
        f2.seek(body,0)
        n = 1
        for line in f2:
            print(line[:-1])
            n += 1
            if n == 9: 
                print('\n')
                break


def reload(game , status=False):
    os.system ("cls")
    print('(Victorias) ' + str(game['win']) + ' - ' + str(game['defeat']) + ' (Derrotas)')
    print('\nVidas restantes: ' + str(game['lives']))  
    if status:      
        printMan(-1)
    else :
        printMan(int(game['lives']))
    print(game['progress'])


def stress(letter):
    replacements = (
        ("a", "á"),
        ("e", "é"),
        ("i", "í"),
        ("o", "ó"),
        ("u", "ú"),
    )
    for a, b in replacements:
        letter = letter.replace(a, b)
    return letter


def run():
    words = getWords('data.txt')
    game = startGame(words)

    while True:
        reload(game,0)

        letter = input('\nEnter a letter: ').casefold()

        game = update(game, letter)

        if game['progress'] == game['word']:
            reload(game, True)
            print('\nGanaste!')
            input('Presiona cualquier letra para continuar')
            game = startGame(words, game['win'] + 1, game['defeat'])

        elif game['lives'] == 0:
            reload(game)
            print('\nPerdiste. La palabra era: ' + str(game['word']))
            input('Presiona cualquier letra para continuar')
            game = startGame(words, game['win'], game['defeat'] + 1)


if __name__ == '__main__':
    run()

'''
QA:
1.- No ingresar números o espacios
3.- Poder detener
4.- incluir modos:   facil (1 cuerpo por palabra),
                     medio: un cuerpo por juego recuperando 1 vida
                     dificil un cuerpo por juego y 2 palabras.
'''
