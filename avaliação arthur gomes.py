#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Coloque seu nome aqui:

**Atividade Avaliativa **

Enunciado:

Crie um programa em Python para avaliar uma competição de bandas de música. O programa deve:

Perguntar a quantidade de bandas participantes (mínimo 3).

Perguntar o nome de cada banda.

Para cada banda, receber as notas de 5 jurados (valores de 0 a 10).

Calcular a média das notas de cada banda e armazenar o resultado em um dicionário, onde a chave será o nome da banda e o valor será a média das notas.

Ao final, mostrar:

A média de cada banda.

O nome da banda vencedora (a que tiver maior média).


# Digite sua resposta
     
Enunciado:

Crie um programa que conte quantas vezes cada palavra aparece em uma frase.

Pedir ao usuário para digitar uma frase

Imprimir a palavra e quantas vezes ela aparece


# Digite sua resposta
     
Enunciado:

Crie um programa em python que imprima números pares

Pedir o usuário para digitar uma lista com mínimo 10 números

Criar uma nova somente com numeros pares

Imprimir números pares


# In[ ]:





# In[11]:


def avaliar_competicao():
   
    while True:
        num_bandas = int(input("Quantas bandas estão participando da competição? (mínimo 3): "))
        if num_bandas >= 3:
            break
        print("O número de bandas deve ser no mínimo 3.")


    medias = {}

   
    for i in range(num_bandas):
        nome_banda = input(f"\nDigite o nome da banda {i+1}: ")

        notas = []
        for j in range(5):  
            while True:
                try:
                    nota = float(input(f"Digite a nota do jurado {j+1} (0 a 10) para a banda {nome_banda}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número entre 0 e 10.")


        media = sum(notas) / len(notas)
        medias[nome_banda] = media


    print("\nMédia das notas das bandas:")
    for banda, media in medias.items():
        print(f"{banda}: {media:.2f}")


    banda_vencedora = max(medias, key=medias.get)
    print(f"\nA banda vencedora é: {banda_vencedora} com a média de {medias[banda_vencedora]:.2f}.")


avaliar_competicao()


# In[12]:


def contar_palavras():

    frase = input("Digite uma frase: ")


    palavras = frase.lower().split()


    contagem = {}


    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1


    print("\nContagem de palavras:")
    for palavra, quantidade in contagem.items():
        print(f"'{palavra}': {quantidade} vez(es)")


contar_palavras()


# In[13]:


def imprimir_numeros_pares():

    while True:
        try:
            numeros = input("Digite uma lista com pelo menos 10 números separados por espaço: ")
            lista_numeros = [int(num) for num in numeros.split()]
            if len(lista_numeros) >= 10:
                break
            else:
                print("A lista precisa ter pelo menos 10 números. Tente novamente.")
        except ValueError:
            print("Por favor, insira apenas números inteiros separados por espaços.")

  
    numeros_pares = [num for num in lista_numeros if num % 2 == 0]


    print("\nNúmeros pares na lista:")
    if numeros_pares:
        print(numeros_pares)
    else:
        print("Não há números pares na lista.")


imprimir_numeros_pares()


# In[ ]:





# In[ ]:




