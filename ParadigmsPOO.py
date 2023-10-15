#Definição da Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade): #Definindo as variáveis a serem chamadas
        self.nome = nome
        self.idade = idade
    
    def cumprimentar(self): # Definindo uma ação, puxando as variáveis acima.
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."



# Criando objetos da classe Pessoa
pessoa1 = Pessoa("Alice", 25)
pessoa2 = Pessoa("Bob", 30)



# Chamando o método cumprimentar() para os objetos. Função será executada conforme o def foi definido. Sendo aplicado ao Objeto.
print(pessoa1.cumprimentar())  # Saída: Olá, meu nome é Alice e eu tenho 25 anos.
print(pessoa2.cumprimentar())  # Saída: Olá, meu nome é Bob e eu tenho 30 anos.
