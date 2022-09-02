message = str.capitalize('first message')
print(message)
message = 'second message'.capitalize()
print(message)
message ='third message'
print(message.title())
print(message.upper())
print(len(message.title().swapcase()))
print(message.startswith('t'))
print(message.endswith('g'))
print(message.lstrip())
print(message.rstrip())
print(message.strip())

message = 'Diogo'

print(message.rjust(20))
print(message.ljust(20))

name ='Diogo'
last_name = "Neves"
print(f"{name} {last_name}")
print("{} {}".format(name, last_name))
print("{1} {0}".format(name, last_name))
print(f"{50*10} {last_name}")

print(f"{last_name:<25}.")
print(f"{last_name:^25}.")
print(f"{last_name:>25}.")
print(f"{last_name:-^25}.")



