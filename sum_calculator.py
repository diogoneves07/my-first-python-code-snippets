import emoji

user_name = input("Olá usuário, por favor, digite seu nome: ")

def get_value():
      value = input("Degite um valor numérico: ")
      if not value.isnumeric():
            print("O valor inserido é inválido, o programa foi encerrado :(.")
            exit() 
      return value
  
first_value = int(get_value())
second_value = int(get_value())

print("Estou pensando...")

message = f"{first_value} mais {second_value} é:\t {first_value + second_value}"
print(message)

print(emoji.emojize(f'{user_name} :sun_with_face:') )
