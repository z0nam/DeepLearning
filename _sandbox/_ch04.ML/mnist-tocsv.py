import sys
import struct

def to_csv(name, maxdata):

	# file open

	lbl_f = open("_data/"+name+"-labels-idx1-ubyte", "rb")
	img_f = open("_data/"+name+"-images-idx3-ubyte", "rb")
	csv_f = open("_data/"+name+".csv", "w", encoding="utf-8")

	# read header

	mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
	mag, img_count = struct.unpack(">II", img_f.read(8))
	rows, cols = struct.unpack(">II", img_f.read(8))

	pixels = rows*cols

	# image read and saving to csv

	res = []
	for idx in range(lbl_count):
		if idx > maxdata: break
		label = struct.unpack("B", lbl_f.read(1))[0]
		bdata = img_f.read(pixels)
		sdata = list (map(lambda n: str(n), bdata))
		csv_f.write(str(label)+",")
		csv_f.write(",".join(sdata)+"\r\n")

		# validation
		
		if idx < 10:
			s = "P2 28 28 255\n"
			s += " ".join(sdata)
			iname = "_data//{0}-{1}-{2}.pgm".format(name,idx,label)
			with open(iname,"w",encoding="utf-8") as f:
				f.write(s)
		
	csv_f.close()
	lbl_f.close()
	img_f.close()
	

# print result

if len(sys.argv)>1: 
	num = int(sys.argv[1])
else:
	num = 1000


print("train set size:", num, "type:",type(num))

to_csv("train",num)
to_csv("t10k",500)

