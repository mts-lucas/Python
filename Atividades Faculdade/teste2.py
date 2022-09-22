distancia = float(input("Insira a distanci entre os Palantir: "))
diametro_sauron = float(input("Insira o diametro do Palantrir de sauron: "))
diametro_saruman = float(input("Insira o diametro do Palantrir de saruman: "))

icm = distancia / (diametro_sauron + diametro_saruman)

print(f"o icm: entre O Palantrir de Saruman e o Palantrir de Sauron é de: {icm:.2f}")