from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

img_path = 'C:/Users/Tamiluuu/.gemini/antigravity/brain/13f4b244-cabb-4cf6-82cd-1983739a963e/.user_uploaded/media_1791863836820_108cb860.png'
im = Image.open(img_path)
print("Image size:", im.size)
print("Format:", im.format)
print("Mode:", im.mode)
