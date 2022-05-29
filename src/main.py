#for this program inputs, the y axis has a standard cartesian plane orientation, so below < above
#TODO: UI intuitive interaction
#TEORICAMENTE ESTÁ FUNCIONANDO KKKKK

class Rect:
    def __init__(self,x1,y1,x2,y2):
        self.start = {"x":x1,"y":y1}#ponto superior esquerdo
        self.end = {"x":x2,"y":y2}#ponto inferior direito

def isIntersected(rect1,rect2):
    x = (rect1.start["x"] - rect2.end["x"])
    y = (rect1.start["y"] - rect2.end["y"])
    a = (rect1.end["x"] - rect2.start["x"])
    b = (rect1.end["y"] - rect2.start["y"])
    if a == 0 or b == 0 or x == 0 or y == 0:  #the rectangles tangent each other
        return False

    x_intersected = a/x < 0
    y_intersected = b/y < 0
    if x_intersected and y_intersected:
        return True


def getNewRectList(rectList,rect):
    #if the rectangles were sorted by the x axis, a more performatic search would be possible so we could parse an array with less values than the current one
    if rect in rectList:
        return rectList
    for r in rectList:
        if isIntersected(rect,r):
            new_rect = Rect(
                min(rect.start["x"],r.start["x"]),
                max(rect.start["y"],r.start["y"]),
                max(rect.end["x"],r.end["x"]),
                min(rect.end["y"],r.end["y"])
            ) 
            rectList.remove(r)
            #rectList.append(new_rect)
            
            #switch r and rect by new_rect and restart rects search
            return getNewRectList(rectList,new_rect)
    rectList.append(rect)
    return rectList

def inputNewRect():
    x1,y1,x2,y2 = map(int,input().split())
    return Rect(x1,y1,x2,y2)

def main():
    rectList = []
    while True:
        new_rect = inputNewRect()
        rectList = getNewRectList(rectList,new_rect)

        for i in rectList:
            print(i.start,i.end,end=" ")
main()
