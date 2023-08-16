import random

def player1():
    player = input("Faça a sua Jogada! 'r' for rock, 's' for scissor, 'p' for paper, or 'q' to quit\n") #define as opções e começa a função
    
    if player == "q":
        return "Obrigado por Jogar! Até a Próxima!" #termina o jogo
    
    if player not in ['r', 's', 'p']:
        return "Escolha Inválida" #retorna uma escolha incorreta de caractere
    
    oponente = random.choice(['r', 's', 'p']) #define como aleatória a escolha do oponente
    
    if player == oponente:
        return "Empataram" #se o resultado do oponente for a mesma escolha do usuário empata o jogo
    
    if is_win(player, oponente):
        return "Parabéns! Você Venceu!" #define o estado de vitória e derrota
    
    return "GAME OVER! Você Perdeu!"

def is_win(player, oponente):
    if (player == 'r' and oponente == 's') or (player == 's' and oponente == 'p') \
    or (player == 'p' and oponente == 'r'):
        return True
    return False #define as características de qual vence qual caractere

while True:
    resultado = player1()
    print(resultado) #printa o resultado da rodada na tela
    if resultado == "Obrigado por Jogar! Até a Próxima!" or resultado == "Escolha Inválida":
        break #caso não apertar q ou não errar o caractere o jogo vai repetindo