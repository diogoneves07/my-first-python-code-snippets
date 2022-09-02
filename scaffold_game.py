from time import sleep
from math import ceil, floor

class Participante:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.avatar = avatar
    def finishGame(self):
        print(f'O participante {self.nome} "{self.avatar}" finalizou o jogo!')
      
class Game:
    def __init__(self) -> None:
        self.participantes = []
        self.vencedor = "Ninguém"
        
        while True:
            participante = input('Degite o nome de um usuário ou "|" para começar o jogo: ')
            
            if participante.lower() == "|":
                if len(self.participantes) <= 1:
                    print('\nPor favor é necessário ao menos dois jogadores para começar o jogo!\n')
                    continue
                else:
                    break
            
            self.participantes.append(participante)
            
        # self.mode = input('Informe o modo do jogo: 0 = "Aléatorio" ou 1 = "Manual": "')
        print(self.participantes)
        
    @property
    def vencedor(self):
        return self.__vencedor
    
    @vencedor.setter
    def vencedor (self, new_value):
        self.__vencedor = new_value


# my_game = Game()
my_list = ["Diogo", "Neves"]
my_list2 = ["Pereira", "Diogo"]
my_list3 = my_list + my_list2

a, b = 40, 50;

print((a , b)[ a < b])

print({True:a, False:b}[ a < b])

print((lambda: a , lambda: b)[ a < b]());

diogo = a > b and a or b;
print(diogo)

test = 10
ternary_perator = test if test == 10 else 90

print(ternary_perator)
my_another_list= my_list[0:1]
print(1042 // 60 )
print(abs(90-180))
print(round(1.5))
print(ceil(1.5))
print(floor(1.5))
print(my_another_list)

update_dict = {"Diogo neves":90}

update_dict.update({"N":9, "D":'90'})
update_dict.pop("Diogo neves")

