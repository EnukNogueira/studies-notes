# Jogo Pedra, Papel e Tesoura - Exercicio 1
from random import choice

jogador_vitorias = 0
maq_vitorias = 0

def Opcao_Jogador():
    while True:
        esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ").strip().lower()
        if esc_jogador in ["pedra", "papel", "tesoura"]:
            return esc_jogador
        else:
            print("Opção inválida. Tente novamente.")

def Opcao_Maquina():
    return choice(["pedra", "papel", "tesoura"])

def verificar_vencedor(esc_jogador, esc_maquina):
    global jogador_vitorias, maq_vitorias
    if (esc_jogador == "pedra" and esc_maquina == "tesoura") or \
       (esc_jogador == "papel" and esc_maquina == "pedra") or \
       (esc_jogador == "tesoura" and esc_maquina == "papel"):
        print(f'Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina}. Resultado: Você ganhou!')
        jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        print(f'Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina}. Resultado: Empate!')
    else:
        print(f'Jogador escolheu {esc_jogador} e a máquina escolheu {esc_maquina}. Resultado: Você perdeu!')
        maq_vitorias += 1

def jogar_novamente():
    while True:
        resposta = input("Você quer jogar novamente? (sim/não): ").strip().lower()
        if resposta in ["sim", "s"]:
            return True
        elif resposta in ["não", "nao", "n"]:
            return False
        else:
            print("Resposta inválida. Tente novamente.")

while True:
    print('-' * 30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print('-' * 30)

    verificar_vencedor(esc_jogador, esc_maquina)

    print('-' * 30)
    print(f"Vitórias do Jogador: {jogador_vitorias}")
    print(f"Vitórias da Máquina: {maq_vitorias}")
    print('-' * 30)

    if not jogar_novamente():
        break
    elif esc_jogador in ["nao", "NAO", "N", "n", "Nao"]:
        break
    else:
        break
