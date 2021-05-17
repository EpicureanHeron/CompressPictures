#run this in any directory add -v for verbose 

#get Pillow (fork of PIL) from pip before running --> pip install Pillow


# https://shantanujoshi.github.io/python-image-compression/

import os
import sys
import math
from PIL import Image

def compressMe(file, verbose=False):
	#seems like here is where I can detail where the directory I want, that is /originalImages, ought to be selected
	filepath = os.path.join(os.getcwd(), 'originalFiles', file)
	# this is the size in bits
	size = os.stat(filepath).st_size
	# kb_size = oldsize/1000
	mb = round(size / (1024 * 1024), 3)
	max_mbs = 2.0

	# print("kb size:", kb_size)	

	print("mb size:", mb)

	picture = Image.open(filepath)
	# https://stackoverflow.com/questions/400788/resize-image-in-python-without-losing-exif-data
	exif = picture.info['exif']
# Your picture process here

	if mb > max_mbs:
		ratio = (max_mbs/mb)
		print(ratio)
		quality = 70

		print('quality should be the following')
		print(quality)
	else:
		quality = 70
		
	#dim = picture.size
	
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	# picture = picture.rotate(90)
	newPath = os.path.join(os.getcwd(), 'compressedFiles', 'compressed_' + file)
	picture.save(newPath,"JPEG",optimize=True,quality=quality,  exif=exif)
	

	
	return 0

def main():
	verbose = False
	#checks for verbose flag
	if (len(sys.argv)>1):
		if (sys.argv[1].lower()=="-v"):
			verbose = True

	#finds present working dir
	pwd = os.path.join(os.getcwd(), "originalFiles")

	tot = 0
	num = 0
	#Seems like this is where it is looking initially? to run the process
	for file in os.listdir(pwd):
		print(file)
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			num += 1
			#this is running the compressMe function
			tot += compressMe(file, verbose)
	print("Average Compression: %d" % (float(tot)/num))
	print("Done")

if __name__ == "__main__":
	main()
