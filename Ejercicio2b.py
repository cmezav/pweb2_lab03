from interpreter import draw
from chessPictures import *

knightN = knight.negative()
line1 = knight.join(knightN)

knightN2 = knightN.verticalMirror()
line2 = knightN2.join(knight.verticalMirror())

final = line1.up(line2)

draw(final)
