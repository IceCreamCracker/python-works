#for this program inputs, the y axis has a standard cartesian plane orientation, so below < above
#TODO: UI intuitive interaction
#TEORICAMENTE ESTÁ FUNCIONANDO KKKKK
from functions import *
def helloWorld():
    print("Hello World")

def main():
    rectList = [] #aqui será armazenado toda a lista de retangulos
    
    while True:
        new_rect = inputNewRect() #recebe do usuario as coordenadas tratadas
        rectList = getNewRectList(rectList,new_rect) #atualiza a lista com as coordenadas novas

        #printa os retangulos e a quantidade deles
        for i in rectList:#
            print(i.start,i.end,end=" ")
        print("a quantidade de retangulos é",len(rectList))
main()
