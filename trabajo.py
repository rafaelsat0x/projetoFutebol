import random

# Entradas do usuário
timename = str(input("Digite o nome do time: "))
quantidadejogos = int(input("Digite a quantidade de jogos (máximo 10): "))

if quantidadejogos > 10:
    print("Quantidade de jogos não pode ser maior que 10.")
    exit()

mediapub = float(input("Digite a média de público do time: "))

# Lista de rivais (limitando a 10)
Rivais = ["Flamengo", "Coritiba", "Corinthians", "Athletico-PR", "Fluminense",
          "Grêmio", "Bahia", "CRB", "Vasco", "Paraná Clube"][:quantidadejogos]


golsTime = []
for i in range(quantidadejogos):
    linha = [random.randint(0, 3) for _ in range(10)]
    golsTime.append(linha)


golsTotaisTime = [sum(linha) for linha in golsTime]


golsRivais = [random.randint(0, 5) for _ in range(quantidadejogos)]


TimesParticipantes = ["Flamengo", "Coritiba", "Corinthians", "Athletico-PR",
                      "Fluminense", "Grêmio", "Bahia", "CRB", "Vasco", "Paraná Clube"]

golsDosTimes = {}

for time in TimesParticipantes:
    matriz = []
    for _ in range(10):
        linha = [random.randint(0, 3) for _ in range(10)]
        matriz.append(linha)
    golsDosTimes[time] = matriz


# Funções
def somaGolsTime():
    return sum(golsTotaisTime)

def somaGolsRivais():
    return sum(golsRivais)

def rivalMaisDificil():
    index = golsTotaisTime.index(min(golsTotaisTime))
    return Rivais[index]

def somaGolsDeTodosOsTimes():
    total = 0
    for time, matriz in golsDosTimes.items():
        for linha in matriz:
            total += sum(linha)
    return total

# Menu interativo
while True:
    print("\n------- MENU -------")
    print("1. Mostrar matriz dos gols")
    print("2. Mostrar rivais do campeonato")
    print("3. Mostrar quantidade total de gols do time")
    print("4. Mostrar rival mais difícil")
    print("5. Mostrar informações do seu clube")
    print("6. Mostrar total de gols de todos os times")
    print("0. Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\nMatriz de Gols do Time (jogos x tempos):")
        for i, linha in enumerate(golsTime):
            print(f"Jogo {i+1} vs {Rivais[i]}: {linha}")

    elif opcao == 2:
        print("\nRivais enfrentados:")
        for i, rival in enumerate(Rivais):
            print(f"Jogo {i+1}: {rival} (Gols deles: {golsRivais[i]})")

    elif opcao == 3:
        print(f"\nTotal de gols do seu time no campeonato: {somaGolsTime()}")

    elif opcao == 4:
        print(f"\nRival mais difícil (menos gols marcados contra ele): {rivalMaisDificil()}")

    elif opcao == 5:
        print(f"\nNome do time: {timename}")
        print(f"Quantidade de jogos: {quantidadejogos}")
        print(f"Média de público: {mediapub:.1f}")

    elif opcao == 6:
        print(f"\nTotal de gols de todos os times participantes: {somaGolsDeTodosOsTimes()}")
    
    elif opcao == 0:
        print("Saindo...")
        break
        exit()

    else:
        print("Opção inválida. Tente novamente.")