class Animal:
    def __init__(self, name, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def __str__(self):  
        return f'{self.nome} - {self.idade} anos - {self.peso} ,
    nPeso: {self.peso}\ n"
        
    def emitir_som(self):
        print(f"{self.nome} diz AU! AU!")

class Passaro(Animal):
    def emitir_som(self):
        
