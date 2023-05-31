from interpreter import draw
from chessPictures import *

image = Picture(square.negative().img + square.img)
image2 = image.verticalRepeat(2)
draw(image2.join(image2.negative()).horizontalRepeat(4))


