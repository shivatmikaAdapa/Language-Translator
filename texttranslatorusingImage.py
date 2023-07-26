from translate import Translator 
from langdetect import detect

from pytesseract import pytesseract
import os

class OCR:
    def __init__(self):
         self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
    def extract(self,filename):
        try:
            pytesseract.tesseract_cmd=self.path
        
            text = pytesseract.image_to_string(filename)
            
            return text
        except Exception as e:
            print(e)
            return "error"
ocr = OCR()
imageName = input("Enter the name of your image:")
txt = ocr.extract(imageName)
target_lang = input("Enter the language you want to covert the statement:")

input_lang = detect(txt)

if(input_lang == target_lang):
     print("same")
else:
     #translator = Translator(to_lang=target_lang)
     translator = Translator(from_lang=input_lang,to_lang=target_lang)
     out = translator.translate(txt)
     print(out)