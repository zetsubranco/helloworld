from random import randint
import os
import time

print("----\njogo da tabuada\n----")

def tabuada():
    jogar = int(input("Com qual tabuada você quer jogar? "))
    while True: 
        
        numero = randint(1, 10)
        pergunta = int(input("Quanto é {} x {}? ".format(jogar, numero)))
        if pergunta != jogar * numero:
            option = input("Você errou. 's' para sair - 'a' para jogar de novo ")
            if option == 's':
                 break
            elif option == 'a':
                tabuada()

           
        else:
            print("você acertou!")
            time.sleep(1)
            os.system("cls")
        

tabuada()

