stat = ['0x85+1x1+0x14','\
0x7+1x1+0x7+1x1+0x9+1x2+0x3+1x4+0x3+1x1+0x6+1x5+0x1+1x1+0x2+1x1+0x1+1x2+0x13+1x2+0x3+1x1+0x8+1x1+0x5+1x2+0x8','\
0x1+1x5+0x18+1x3+0x3+1x1+0x16+1x2+0x1+1x1+0x5+1x2+0x2+1x1+0x3+1x1+0x4+1x2+0x3+1x3+0x3+1x1+0x2+1x2+0x4+1x3+0x8','\
0x3+1x1+0x7+1x1+0x11+1x2+0x1+1x1+0x3+1x5+0x12+1x1+0x2+1x1+0x7+1x1+0x10+1x1+0x3+1x2+0x1+1x1+0x5+1x3+0x4+1x1+0x1+1x2+0x2+1x1+0x4','\
0x3+1x1+0x3+1x1+0x7+1x2+0x3+1x1+0x2+1x1+0x2+1x1+0x7+1x1+0x11+1x2+0x2+1x2+0x5+1x2+0x10+1x1+0x3+1x1+0x2+1x1+0x3+1x2+0x2+1x1+0x4+1x4+0x7','\
0x3+1x1+0x3+1x1+0x3+1x1+0x1+1x3+0x10+1x1+0x7+1x1+0x7+1x1+0x3+1x1+0x3+1x1+0x1+1x2+0x2+1x3+0x8+1x5+0x4+1x1+0x3+1x9+0x1+1x3+0x7','\
0x3+1x1+0x3+1x3+0x1+1x1+0x1+1x4+0x9+1x1+0x6+1x2+0x2+1x1+0x7+1x2+0x3+1x1+0x2+1x1+0x4+1x1+0x10+1x1+0x6+1x1+0x7+1x1+0x7+1x4+0x4','\
0x5+1x1+0x1+1x1+0x1+1x1+0x1+1x1+0x4+1x2+0x7+1x2+0x3+1x4+0x11+1x1+0x4+1x1+0x2+1x1+0x3+1x2+0x6+1x1+0x3+1x1+0x6+1x1+0x7+1x1+0x1+1x1+0x1+1x5+0x7','\
0x7+1x1+0x1+1x1+0x1+1x1+0x2+1x3+0x7+1x5+0x16+1x1+0x4+1x1+0x2+1x1+0x1+1x3+0x3+1x6+0x2+1x1+0x2+1x1+0x1+1x5+0x5+1x1+0x2+1x1+0x4+1x1+0x7','\
0x18+1x5+0x13+1x6+0x27+1x1+0x14+1x1+0x2+1x2+0x2+1x1+0x5+1x1+0x2','\
0x1+1x1+0x5+1x1+0x4+1x1+0x3+1x1+0x8+1x1+0x8+1x1+0x9+1x1+0x8+1x1+0x5+1x1+0x17+1x1+0x10+1x3+0x9','\
0x68+1x1+0x11+1x1+0x19']

from PIL import Image

width = len(stat)
height = 100

pixels = []
for i in range(len(stat)):
	tmp = stat[i].split('+')
	for pix in tmp:
		col, num = pix.split('x')
		if col == '0':
			pixels.extend([(255,255,255) for _ in range(int(num))])
		else:
			pixels.extend([(0,0,0) for _ in range(int(num))])

im = Image.new("RGB",(height,width))
im.putdata(pixels)
im.save("output.png")