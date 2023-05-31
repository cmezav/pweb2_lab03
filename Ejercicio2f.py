from interpreter import draw
from chessPictures import *

line1 = square.join(square.negative()).horizontalRepeat(4)
line2 = square.negative().join(square).horizontalRepeat(4)

final = line1.up(line2)

draw(final)

