#Definindo a função do gerador
def contador(maximo):
    contador_atual = 1
    while contador_atual <= maximo: #Enquanto o contador atual for menor ou igual a 100, o gerador irá fazer a iteração.
        yield contador_atual #Cria um gerador atual em cima do contador.
        contador_atual += 1

# Executa um gerador(função)
meu_gerador = contador(100) #Executando o def acima.

# Iterando sobre o gerador (Representação dos núemros que irão ser iterados)
for numero in meu_gerador:
    print(numero)
