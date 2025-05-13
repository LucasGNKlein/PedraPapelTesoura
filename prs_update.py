import random

def get_player_choice():
    while True:
        player = input("Faça a sua Jogada! 'r' para pedra, 's' para tesoura, 'p' para papel, ou 'q' para sair\n")
        if player in ['r', 's', 'p', 'q']:
            return player
        print("Escolha inválida. Tente novamente!")

def get_game_result(player, opponent):
    if player == opponent:
        return "tie"
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return "win"
    return "lose"

def get_result_message(result):
    messages = {
        "win": "Parabéns! Você Venceu!",
        "lose": "GAME OVER! Você Perdeu!",
        "tie": "Empataram",
        "quit": "Obrigado por Jogar! Até a Próxima!"
    }
    return messages.get(result, "Escolha Inválida")

def play_game():
    while True:
        player = get_player_choice()
        if player == "q":
            print(get_result_message("quit"))
            break

        opponent = random.choice(['r', 's', 'p'])
        print(f"Oponente escolheu: {opponent}")
        result = get_game_result(player, opponent)
        print(get_result_message(result))

if __name__ == "__main__":
    play_game()
