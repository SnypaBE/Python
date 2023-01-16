genero = int(input("Qual seu genero?: "))

while (genero < 1) or (genero > 2):
    genero = int(input("O valor tem que ser 1 ou 2!\n \
    Tente novamente:"))
print("Nota válida")
