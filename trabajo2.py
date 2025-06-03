timename = str(input("Digite o nome time: "))
quantidadejogos = int(input("Digite a quantidade de jogos: "))
mediapub = float(input("Digite a média de público do time: "))

vetor=[]

timesrivais = ["Flamengo", "Fluminense", "Vasco", "Botafogo", "São Paulo", "Corinthians", "Santos", "Palmeiras", "Cruzeiro", "Atletico Mineiro"]

for time in timesrivais:
    print(time)