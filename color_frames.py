import os, sys
from color2 import colorFrame

frames = int(sys.argv[1])

i = 0
while(i <= frames) :
	colorFrame("frames/frame" +str(i)+".jpg")
	i += 1
