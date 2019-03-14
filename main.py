import pandas as pd
import numpy as np

'''
a) calcular a media de cada coluna

b) calcular o max e min de cada coluna 

c) imprimeir as des linha com menor soma dos seus valores

d) impr as 5 linhas + prox da 12

e) impr as 3 linhas + prox da 12

f) impr a linha + prox da 12

prox=distancia euclidiana dos valores da linha 3D 
'''


data = pd.read_csv("iris.txt")

soma = data.sum(1)
soma = soma.sort_values(ascending=True)

print("a) calcular a media de cada coluna")
print(data.mean(0).to_string())
print("-------------------------\n-------------------------\n-------------------------\n-------------------------\n")

print("b) calcular o max e min de cada coluna")
print("c.1) max----------\n------------------:")
print(data.max(0).to_string())
print("c.2)min-----------\n------------------:")
print(data.min(0).to_string())
print("-------------------------\n-------------------------\n-------------------------\n-------------------------\n")


print("c) imprimeir as dez linhas com menor soma dos seus valores")
print(data.iloc[soma.iloc[:10].index]) 
print("-------------------------\n-------------------------\n-------------------------\n-------------------------\n")
print("d) imprimir as 5 linhas + prox da 12")

data1 = data.drop('species', 1)

data2 = data1.values.tolist()
    
distances = []
for row in data2:
    distances.append(np.linalg.norm(np.array(row)-np.array(data2[11])))    

data['distance'] = pd.Series(distances)

print(data.sort_values(by=['distance']).iloc[1:6].to_string())
print("-------------------------\n-------------------------\n-------------------------\n-------------------------\n")
print("e) impr as 3 linhas + prox da 12")
print(data.sort_values(by=['distance']).iloc[1:4].to_string())
print("-------------------------\n-------------------------\n-------------------------\n-------------------------\n")
print("f) impr a linha + prox da 12")
print(data.sort_values(by=['distance']).iloc[1:2].to_string())