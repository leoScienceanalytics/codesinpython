class Dataset:
    def __init__(self, data):
        self.data = data
    
    def describe(self):
        print("Descrição do Dataset:")
        print(f"Número de instâncias: {len(self.data)}")
        print(f"Número de atributos: {len(self.data[0])}")
    
class Preprocessor:
    def __init__(self, dataset):
        self.dataset = dataset
    
    def normalize(self):
        # Implementar a lógica de normalização dos dados
        pass
    
class Model:
    def __init__(self, dataset):
        self.dataset = dataset
        self.trained = False
    
    def train(self):
        # Implementar a lógica de treinamento do modelo usando os dados
        self.trained = True
    
    def predict(self, input_data):
        if not self.trained:
            print("O modelo não foi treinado ainda.")
            return
        
        # Implementar a lógica de previsão usando o modelo treinado
        pass

# Criando um conjunto de dados
data = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [7.0, 3.2, 4.7, 1.4],
    # ... outras instâncias ...
]

dataset = Dataset(data)

# Pré-processamento
preprocessor = Preprocessor(dataset)
preprocessor.normalize()

# Treinamento do modelo
model = Model(dataset)
model.train()

# Fazendo previsões
input_data = [6.2, 2.8, 4.8, 1.8]
model.predict(input_data)
