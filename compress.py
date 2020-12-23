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
	print("filepath " + filepath)
	oldsize = os.stat(filepath).st_size

	kb_size = oldsize/1000
	max_kbs = 2000

	print("kb size:", kb_size)
	
	

	picture = Image.open(filepath)

	if kb_size > max_kbs:
		ratio = (max_kbs/kb_size)
		print(kb_size)

		quality = ratio * 100
		print('quality should be the following')
		print(quality)
	else:
		quality = 85
		
	#dim = picture.size
	
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	newPath = os.path.join(os.getcwd(), 'compressedFiles', 'compressed_' + file)
	picture.save(newPath,"JPEG",optimize=True,quality=math.floor(quality)) 
	
	#change the "compressed_+file" to be something else if I want
	newsize = os.stat(os.path.join(os.getcwd(),'originalFiles', file)).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	if (verbose):
		print( "File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent))
	return percent

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