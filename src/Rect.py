import json
class Rect:
    def __init__(self,x1,y1,x2,y2):
        self.start = {"x":x1,"y":y1}#ponto superior esquerdo
        self.end = {"x":x2,"y":y2}#ponto inferior direito
