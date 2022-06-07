#aqui se encontra a classe retangulo, que possui as coordenadas do começo e do fim de maneira intuitiva de se ler,
#o import json é pra ter certeza que uma outra coisa não vai dar errado
import json
class Rect:
    def __init__(self,x1,y1,x2,y2):
        self.start = {"x":x1,"y":y1}#ponto superior esquerdo
        self.end = {"x":x2,"y":y2}#ponto inferior direito
