import csv
#import requests

archivo = open("appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')
next(csvreader)

print("Estos son los juegos gratuitos y en español:")

pruebas = (filter(lambda line: line[7] == '0' and 'ES' in line[12], csvreader))
for i in pruebas:
    print(i[2])

ordenados = sorted(csvreader, key= lambda row: row[5])

print("Los 10 juegos con mejor puntaje son: ")
for line in ordenados[:10]:
    print(line[4])
archivo.close()
