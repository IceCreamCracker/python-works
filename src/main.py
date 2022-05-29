#for this program inputs, the y axis has a standard cartesian plane orientation, so below < above
#TODO: UI intuitive interaction
#TEORICAMENTE ESTÁ FUNCIONANDO KKKKK
from functions import *

def main():
    rectList = []
    while True:
        new_rect = inputNewRect()
        rectList = getNewRectList(rectList,new_rect)

        for i in rectList:
            print(i.start,i.end,end=" ")
main()
