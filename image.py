import matplotlib.pyplot as plt
from pylab import *
from PIL import Image

pil_im = Image.open("goku_ssjb.jfif")
pil_im.show()

gray_im = Image.open("goku_ssjb.jfif").convert('L')
gray_im.show()

out = pil_im.resize((1024,1024))
out.show()

out = out.rotate(45)
out.show()
