# -*- coding: utf-8 -*-

"""My first program in Python."""

def what_is_your_name():
    """Get user name and print on screen."""
    name = input("Qual é o seu nome? : ")
    if name == "Diogo":
        print("Meu nome é Diogo Neves")
    elif name == 'Cr7':
        print("The best soccer player of world!")
    else:
        print("Meu nome é : {}".format(name))
  
    return False

what_is_your_name()
