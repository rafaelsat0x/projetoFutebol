def soma_gols(jogos):
    total = 0
    for jogo in jogos:
        for tempo in jogo:
            total += tempo
    return total

def adversario_chato(lista_adv, gols):
    if len(lista_adv) == 0:
        return None

    dificuldade = {}
    for idx in range(len(lista_adv)):
        nome = lista_adv[idx]
        gols_feitos = sum(gols[idx])
        dificuldade[nome] = gols_feitos

    mais_chato = min(dificuldade, key=dificuldade.get)
    return mais_chato

def main():
    time = input("Nome do time: ")
    try:
        n = int(input("Quantos jogos? "))
    except:
        print("Parabéns, você quebrou o programa.")
        return

    try:
        publico = float(input("Média de público? "))
    except:
        publico = 0 

    nomes_adversarios = []
    gols_por_jogo = []

    for i in range(n):
        print(f"\nJogo {i+1}")
        adv = input("Adversário: ")
        nomes_adversarios.append(adv)

        try:
            g1 = int(input("Gols no 1T: "))
            g2 = int(input("Gols no 2T: "))
        except:
            print("Colocou letra no lugar de número, ein gênio?")
            g1, g2 = 0, 0 

        gols_por_jogo.append([g1, g2])

    total = soma_gols(gols_por_jogo)
    print(f"\nO {time} fez {total} gols no total.")

    mais_dificil = adversario_chato(nomes_adversarios, gols_por_jogo)
    if mais_dificil:
        print(f"Quem deu mais trabalho: {mais_dificil}")
    else:
        print("Não teve nem adversário, só treininho.")

if __name__ == "__main__":
    main()
