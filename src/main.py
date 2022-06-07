#for this program inputs, the y axis has a standard cartesian plane orientation, so below < above
#TODO: UI intuitive interaction
#TEORICAMENTE ESTÁ FUNCIONANDO KKKKK
from functions import *

def main():
    rectList = [] #aqui será armazenado toda a lista de retangulos
    print("Olá, digite as coordenadas separadas por espaço.\nEsta versão não possui tratamento de dados, então tome cuidado, por favor")
    print("Para sair do programa, tecle ctrl+z ou ctrl+c")
    while True:
        new_rect = inputNewRect() #recebe do usuario as coordenadas tratadas
        rectList = getNewRectList(rectList,new_rect) #atualiza a lista com as coordenadas novas

        #printa os retangulos e a quantidade deles
        for i in rectList:#
            print(i.start,i.end)
        print("a quantidade de retangulos é",len(rectList))
main()
