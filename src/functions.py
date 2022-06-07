from Rect import Rect #importa a classe retangulo

#verifica se dois retangulos estão intersectados
def isIntersected(rect1,rect2):
    x = (rect1.start["x"] - rect2.end["x"])
    y = (rect1.start["y"] - rect2.end["y"])
    a = (rect1.end["x"] - rect2.start["x"])
    b = (rect1.end["y"] - rect2.start["y"])
    if a == 0 or b == 0 or x == 0 or y == 0:  #the rectangles tangent each other
        return True #matematicamente isso seria false, considerando que um ponto de coordenada não possui área por estar em uma dimensão, de modo que os retângulos tangenciam mas não intersectam. mas parece que preciso colocar true.

    x_intersected = a/x < 0
    y_intersected = b/y < 0
    if x_intersected and y_intersected:
        return True


def getNewRectList(rectList,rect):
    #if the rectangles were sorted by the x axis, a more performatic search would be possible so we could parse an array with less values than the current one
    if rect in rectList:#já retorna a própria lista caso haja uma replicação de um retangulo ja na lista
        return rectList

    for r in rectList:#compara recursivamente as intersecções entre retângulos até não haver mais intersecções
        if isIntersected(rect,r):
            new_rect = Rect(
                min(rect.start["x"],r.start["x"]),
                max(rect.start["y"],r.start["y"]),
                max(rect.end["x"],r.end["x"]),
                min(rect.end["y"],r.end["y"])
            ) 
            rectList.remove(r)
            return getNewRectList(rectList,new_rect)
    rectList.append(rect)
    return rectList #retorna a lista atualizada

def inputNewRect():
    x1,y1,x2,y2 = map(int,input().split())
    return Rect(x1,y1,x2,y2)#retorna um objeto da classe retangulo com as coordenadas de parametro
