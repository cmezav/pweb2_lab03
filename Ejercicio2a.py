from interpreter import draw
from chessPictures import *
knightN = knight.negative()
line1 = knight.join(knightN)

line2 = knightN.join(knight)
final = line1.up(line2)

draw(final)
