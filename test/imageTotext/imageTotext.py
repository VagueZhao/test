# coding=utf-8
from PIL import Image
import pytesseract
import ImageEnhance
#python2.7,实现图片文本识别，仅限英文
image1 = Image.open('F:/test/imageTotext/images/1.jpg')
#使用ImageEnhance可以增强图片的识别率
enhancer = ImageEnhance.Contrast(image1)
image_enhancer = enhancer.enhance(4)
text=pytesseract.image_to_string(image_enhancer)
print ('image_1:\n'+text)
#python3,一行代码实现图片文本识别，仅限英文
text1=pytesseract.image_to_string(Image.open('F:/test/imageTotext/images/3.jpg'))
print ('image_3:\n'+text1)

#python3,一行代码实现图片文本识别，中文
# #image2 = Image.open('F:/test/images/3.jpg')
text2=pytesseract.image_to_string(Image.open('F:/test/imageTotext/images/2.jpg'),lang='chi_sim')
# tessdata_dir_config = '--tessdata-dir "D:\\Tesseract_ocr\\Tesseract-OCR\\tessdata"'
#text2=pytesseract.image_to_string(Image.open('F:/test/images/1.jpg'), config=tessdata_dir_config)
print('image_2:\n'+text2)
#text2=pytesseract.image_to_string(Image.open('F:/test/images/1.jpg'), config=tessdata_dir_config)
#print(text3)