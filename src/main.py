#for this program inputs, the y axis has a standard cartesian plane orientation, so below < above
#TODO: UI intuitive interaction


class Rect:
    def __init__(self,x1,y1,x2,y2):
        self.start = {"x":x1,"y":y1}#ponto superior esquerdo
        self.end = {"x":x2,"y":y2}#ponto inferior direito

def isIntersected():
    pass

def verifyIntersection():
    pass

def getNewRectList(rectList,rect):
    #if the rectangles were sorted by the x axis, a more performatic search would be possible so we could parse an array with less values than the current one
    for r in rectList:
        if isIntersected(rect,r):
            new_rect = Rect(
                min(rect.start["x"],r.start["x"]),
                max(rect.start["y"],r.start["y"]),
                max(rect.end["x"],r.end["x"]),
                min(rect.end["y"],r.end["y"])
            ) 
            rectList.remove(rect)
            rectList.remove(r)
            rectList.append(new_rect)
            #switch r and rect by new_rect and restart rects search
            return getNewRectList(rectList,new_rect)
    rectList.append(rect)
    return rectList

def inputNewRect():
    return Rect(int(input()),int(input()),int(input()),int(input()))

def main():
    rectList = []
    while True:
        new_rect = inputNewRect()
        rectList = getNewRectList(rectList,new_rect)
