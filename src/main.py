def verifyIntersection():
    pass

def updateRectList():
    pass

def inputNewRect():
    pass

class Rect:
    def __init__(self,x1,y1,x2,y2):
        self.start = {"x":x1,"y":y1}
        self.end = {"x":x2,"y":y2}

def main():
    rects = []
    while True:
        new_rect = inputNewRect()
        verifyIntersection(new_rect,rects)
