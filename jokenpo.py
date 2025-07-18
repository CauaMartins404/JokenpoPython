import random
import time
pontos_usuario = 0 
pontos_computador = 0
# Início do jogo
print("Bem-vindo ao Jokenpô!")
def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes)
    
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    
    escolha_usuario = int(input("Digite o número da sua escolha: "))
    
    if escolha_usuario < 1 or escolha_usuario > 3:
        print("Opção inválida! Tente novamente.")
        return jogar_jokenpo()
    
    usuario = opcoes[escolha_usuario - 1]
    print("Jo...")
    time.sleep(0.4)
    print("Ken...")
    time.sleep(0.4)
    print("Pô!")
    time.sleep(1.5)

    print(f"Você escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")
    
    if usuario == computador:
        print("Empate!")
    elif (usuario == 'pedra' and computador == 'tesoura') or \
         (usuario == 'papel' and computador == 'pedra') or \
         (usuario == 'tesoura' and computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    
    #contar pontos
    if usuario == computador:
        pontos_usuario += 0.5
        pontos_computador += 0.5
    elif (usuario == 'pedra' and computador == 'tesoura') or \
         (usuario == 'papel' and computador == 'pedra') or \
         (usuario == 'tesoura' and computador == 'papel'):
        pontos_usuario += 1
    else:
        pontos_computador += 1

    print(f"Pontos - Jogador: {pontos_usuario}, Computador: {pontos_computador}")
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == 's':
        jogar_jokenpo()
    else:
        print(f"Pontuação final - Jogador: {pontos_usuario}, Computador: {pontos_computador}")
        print("Obrigado por jogar! Até a próxima!")
jogar_jokenpo()
# Fim do jogo