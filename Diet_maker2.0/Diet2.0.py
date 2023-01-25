nome = input('Digite seu nome: ')
sexo = input("Informe seu sexo (M/F): ")
while sexo !='m' and sexo != 'M' and sexo != 'F' and sexo !='f':
    sexo = input('Sexo deve ser "M" Masculino/"F" Feminino, Digite novamente: ')
idade = int(input("Informe sua idade: "))
while idade < 15 or idade > 100:
    idade = int(input('Idade deve ser maior que 15 anos e menor que 100. Digite novamente: '))
peso = float(input("Informe seu peso (em kg): "))
while peso <30 or peso >300:
    peso = float(input('Valor inválido, digite novamente: '))
altura = int(input("Informe sua altura (em cm): "))
while altura < 80 or altura > 300:
    altura = int(input('Valor inválido, digite novamente: '))
atividade = input("Informe seu nível de atividade (sedentario, pouco ativo, ativo, muito ativo): ")
while atividade != 'sedentario' and atividade != 'ativo' and atividade != 'muito ativo' and atividade != 'pouco ativo':
    atividade = input('Digite corretamente: ')
ref = int(input('Informe quantas refeições diarias deseja fazer? (de 4 a 6): '))
while ref < 4 or ref > 6:
    ref = int(input("O número de refeições devem ser de 4 a 6, digite novamente: "))
if sexo == "M" or "m":
    tmb = (66+(13.8*peso)+(5*altura)-(6.8-idade))*0.85
else:
    tmb = (655+(9.6*peso)+(1.8*altura)-(4.7-idade))*0.85
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
prot = peso*1.5
carb = (tmbAtv-(prot*4))*0.6/4
gordura = (tmbAtv-(prot*4))*0.4/9
frango = (prot)*3.7
ovo = (prot)*0.34
patinho = (prot)*3.44
arroz = ((carb)*3.57)
batata = ((carb)*5.43)
mandioca = ((carb)*2.63)
azeite = int(((gordura)*0.08))
castanha = ((gordura)*1.51)

prot = prot/ref
protk = prot*4
carb = carb/ref
carbk = carb*4
gordura = gordura/ref
gordurak = gordura*9

print(f"\n{nome} sua necessidade diária para o emagrecimento é de {tmbAtv:.2f}kcal")
print(f"Você deve consumir cerca de {prot:.2f}g /{protk:.2f}kcal de proteína por refeição,")
print(f"Você deve consumir cerca de {carb:.2f}g/ {carbk:.2f}kcal de carboidratos por refeição,")
print(f"Você deve consumir cerca de {gordura:.2f}g/ {gordurak:.2f}kcal de gordura por refeição.\n")
print(f'''Escolha uma das 3 opções de Protreina, uma das 3 opções de Carboidratos e uma das 2 opções de Gordura para cada refeição:

Proteina:
[1]-{frango/ref:.0f}g de frango ou
[2]-{ovo/ref:.0f} claras de ovos ou
[3]-{patinho/ref:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz/ref:.0f}g de arroz branco ou
[2]-{batata/ref:.0f}g de batata doce cozida ou
[3]-{mandioca/ref:.0f}g de mandioca.
        
Gordura:
[1]-{azeite/ref:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha/ref:.0f}g de castanha do Pará.''')
