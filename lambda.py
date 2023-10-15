#expressão lambda é uma função anônima (sem nome) que pode ser usada para criar funções simples de forma concisa. 
#Elas são frequentemente usadas em situações em que você precisa passar uma função como argumento para outra função, como em funções de ordenação, mapeamento e filtragem.


#Exemplo1: X²
square = lambda x: x**2
print(square(5))
print(square(10))



#Exemplo2: Lambda sendo usado como ferramenta de ordenação.
numbers = [10, 6, 9, 4, 5, 2, 3, 8, 7, 1] #Lista
order = sorted(numbers, key = lambda x: x**2) # Chama a lista, calcula o quadrado de todos os números da lista, e ordena de forma crescente de acordo com o resultado
print(order) #Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

