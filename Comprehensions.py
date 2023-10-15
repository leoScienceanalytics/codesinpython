#Listas de compreensão



#Exemplo 1: Achando os valores quadrados dos valores pares de 1 a 10.
quadrados_pares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(quadrados_pares)
# Resultado: [4, 16, 36, 64, 100]



#Exemplo 2: Achando os valores quadrados dos números de 7 em 7 até 30.
exemplo = [x**2 for x in range(1, 30) if x % 7 == 0]
print(exemplo)
#Resultado: [49, 196, 441, 784]




#Exemplo 3: Lista com números maiores que 5.
numbers = [1, 7, 3, 9, 4, 8]
greater_than_five = [x for x in numbers if x > 5]
print(greater_than_five)
# Output: [7, 9, 8]





#Aplicação 2:
#Importando biblioteca
import numpy as np

#Mostrando valores entre 4 e 17
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sigma = [x for x in numbers if x < 4 or x > 17]
print(sigma)
#Output valores entre o intervalo dos limites.

#Mostrando a lista criada somente com os valores dentro do intervalo.
newlist = [x for x in numbers if x not in sigma]
print(newlist)

#Calculando estatísticas da nova lista.
median =  np.mean(newlist)
median = round(median, 2)

dp = np.std(newlist)
dp = round(dp, 2)

print('Nova Média: ', median)
print('Novo Desvio Padrão: ', dp) 