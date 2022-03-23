nome= "Maria Alice"
idade= 24
altura= 1.48
peso= 50
anoAtual=2022
anoDeNascimento= (anoAtual-idade)
imc=(peso)/(altura*altura)
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {anoDeNascimento}.')
