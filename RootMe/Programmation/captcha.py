import requests
import base64
import subprocess
import shlex
from lxml import html
from PIL import Image
import pytesseract as pyt
import urllib

pyt.pytesseract.tesseract_cmd = r'C:\Users\tom52\Desktop\TesseractOCR\tesseract.exe'

url = "http://challenge01.root-me.org/programmation/ch8/"
r = requests.get(url)
sess = r.cookies
content = html.fromstring(r.content)
img = content.xpath('//img/@src')[0]
bs = img.split(',')[-1]
bts = base64.b64decode(bs)

with open('img.png', 'wb') as f:
    f.write(bts)

im = Image.open("img.png")

# cleaning
for x in range(im.size[0]):
    for y in range(im.size[1]):
        r, g, b = im.getpixel((x, y))
        if r < 25 and g < 25 and b < 25:
            im.putpixel((x, y), (255, 255, 255)) 
im.save("img.png")

p = pyt.image_to_string(im)
p = p.replace("\n","")
p = p.replace("\r","")
p = p.replace(" ","")
p = p.replace(",","")
p = p.replace("_","")

data = {"cametu": p}
req = requests.post(url, cookies=sess, data=data)
print(req.text)
