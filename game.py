#Jogo Pedra, Papel e Tesoura - Exercicio 1 
from random import choice 

jogador_vitorias = 0
maq_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra , Papel ou Tesoura")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    # else:
        print("Opcao Invalida. Tente novamente")
        Opcao_Jogador ()

def Opcao_Maquina():
     esc_maquina = choice(["pedra","papel","tesoura"])
     return esc_maquina

while True:

    print('-'*30)  
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print('-'*30)

    if(esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador =="papel") and (esc_maquina == 'papel') \
            or (esc_jogador =='tesoura') and (esc_maquina =="papel"):
    #Jogador ganhou!
        print(f'Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} '
    ' Resultado: Voce ganhou')
        jogador_vitorias += 1

    elif esc_jogador == esc_maquina: 
        #Empatou!
        print(f'Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} ' 
    'Resultado: Empate')
    else:
        #Maquina ganhou!
        print(f'Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} ' 
          'Resultado: Voce Perdeu')
    maq_vitorias += 1

    print('-'*30)
    print(f"Vitorias do Jogador {jogador_vitorias}")
    print(f"Vitorias da Maquina`{maq_vitorias}")
    print('-'*30)

    esc_jogador = input("voce quer jogar novamente? ")
    if esc_jogador in ["SIM","sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["nao", "NAO", "N", "n", "Nao"]:
        break
    else:
        break