nome = input('Digite seu nome: ')
sexo = input("Informe seu sexo (M/F): ")
while (sexo !='M') and (sexo !='F'):
    sexo = input('Sexo deve ser "m" Masculino/"f" Feminino, Digite novamente (minusculo): ')
while True:
    idade = int(input("Informe sua idade: "))
    if idade > 15 and idade < 100:
        break
    elif idade < 15:
        print('idade não pode ser menor que 15 anos. Tente novamente: ')
    else:
        print('idade não pode ser maior que 100 anos. Tente novamente: ')
peso = float(input("Informe seu peso (em kg): "))
while peso <30 or peso >300:
    peso = float(input('Valor inválido, digite novamente: '))
while True:
    altura = float(input("Informe sua altura (em cm): "))
    if altura <100:
        break
    else:
        print('Valor tem que ser maior que 100cm, digite novamente: ')
while True:
    atividade = input("Informe seu nível de atividade (sedentario, pouco ativo, ativo, muito ativo): ")
    if atividade == 'sedentario' or atividade == 'ativo' or atividade == 'muito ativo' or atividade == 'pouco ativo':
        break
    else:
        atividade = input('Digite corretamente')
while True:
    ref = int(input("Informe quantas refeições diarias deseja fazer? (de 4 a 6): "))
    if ref >=4 and ref <=6:
        break
    else:
        atividade = input('Digite de 4, 5 ou 6 refeições: ')
# Calcula o metabolismo basal
if sexo == "M":
    tmb = (66+(13.8*peso)+(5*altura)-(6.8-idade))*0.85
else:
    tmb = (655+(9.6*peso)+(1.8*altura)-(4.7-idade))*0.85

# Calcula o gasto calórico total
if atividade == "sedentario":
    tmbAtv = tmb*1.2
elif atividade == "pouco ativo":
    tmbAtv = tmb*1.32
elif atividade == "ativo":
    tmbAtv = tmb*1.55
elif atividade == "muito ativo":
    tmbAtv = tmb*1.9
else:
    print('Algo deu errado.')

# Calcula a necessidade diária de proteína
prot = peso*1.5

# Calcula a necessidade diária de carboidratos e gordura
carb = (tmbAtv-(prot*4))*0.6/4
gordura = (tmbAtv-(prot * 4))*0.4/9
frango = (prot)*3.7
ovo = (prot)*0.34
patinho = (prot)*3.44
arroz = ((carb)*3.57)
batata = ((carb)*5.43)
mandioca = ((carb)*2.63)
azeite = int(((gordura)*0.08))
castanha = ((gordura)*1.51)

# Divide o resultado diário pelo número de refeições escolhido pelo usuário
prot = prot/ref
protk = prot*4
carb = carb/ref
carbk = carb*4
gordura = gordura/ref
gordurak = gordura*9

# Imprime o resultado
print(f"{nome} sua necessidade diária para o emagrecimento é de {tmbAtv:.2f}kcal")
print(f"Você deve consumir cerca de {prot:.2f}g/{protk:.2f}kcal de proteína por refeição")
print(f"Você deve consumir cerca de {carb:.2f}g/{carbk:.2f}kcal de carboidratos por refeição")
print(f"Você deve consumir cerca de {gordura:.2f}g/{gordurak:.2f} de gordura por refeição")
print(f'''Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.''')
