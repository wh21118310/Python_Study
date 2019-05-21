import pytesseract
from PIL import Image
import os,io
def processing(newphoto,photo):
	img = Image.open(photo)
	img = img.convert('L')
	# img = img.point(lambda x:0 if x<126 else 255)
	img.save('D:\processed\\'+newphoto)
	text = pytesseract.image_to_string(img,lang='eng')
	return text

def savecontent(content,text):
	with io.open(content,'a+',encoding='utf8') as f:
		f.write(text)
		f.close()
	print("processing is ok!")

path = 'D:\Western'
dirs = os.listdir(path)
for dir in dirs:
	filepath = path+'\\'+dir
	filelist = os.listdir(filepath)
	filelist.sort(key=lambda x:int(x.split('.')[0]))
	for file in filelist:
		filename = file.split('.')
		if filename[1] == 'jpg':
			print(file)
			text = processing(file,filepath+'\\'+file)
			savecontent(dir,text)

