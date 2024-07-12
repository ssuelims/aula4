nome1 = input("Digite um nome:")
nome2 = input("Digite um nome:")
nome3 = input("Digite um nome:")
nome4 = input("Digite um nome:")
nome5 = input("digite um nome:")

import os
import random
lista_nome = []
lista_sorteados = []

while True:

    nome = input("digite os nomes que serao sorteados:")
    if nome != '':
       lista_nome.append(nome)
    else:
        break      

escolhido = random. choice(lista_nome)

print(f"o sorteado ")
print(lista_nome)
      


while True:
    if lista_nome:
       os.system('cls')
       escolhido = random.choice(lista_nome)
       lista_sorteados.append(escolhido)
       print(f'o sorteado e {escolhido}')
       opcao = input('Deseja sorteao outro nome?(s/n)').lower()
       os.system('cls')

       if opcao != 's':
          break
    else:  
        print("nao existe nomes  para serem sorteados.")  
escolhido=random.choice(lista_nome) 
print(f' o soteado foi{escolhido}')
print(f'lista de sorteados {lista_sorteados}')

          







lista = ['Antonio','paulo','jose','joao','beltrano']
print(f"o primeiro nome da lista: {lista[0]}")
print(f"o segundo nome d lista:{lista[1]}")
print(f"o terceiro nome da lista:{lista[2]}")

for i in range (5):
    print(f'{i+1}º nome: {lista[i]}')
print() 
for i in range(len(lista)):
    print(f'{i + 1}º nome: {lista[i]}')  



                                    