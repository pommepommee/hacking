import requests
import base64
import subprocess
import shlex
from lxml import html
import cv2
import urllib
import qrtools

url = "http://challenge01.root-me.org/programmation/ch7/"
r = requests.get(url)
sess = r.cookies
content = html.fromstring(r.content)
img = content.xpath('//img/@src')[0]
bs = img.split(',')[-1]
bts = base64.b64decode(bs)

with open('qr.png', 'wb') as f:
    f.write(bts)

padding = cv2.imread("padding.png")
code = cv2.imread("qr.png")

result = cv2.addWeighted(padding, 0.4, code, 0.4, 0)
cv2.imwrite("result.png", result)

qr = qrtools.QR()
qr.decode("result.png")
print(qr.data)
st = qr.data.split()[-1]
data = {"metu": st}
req = requests.post(url, cookies=sess, data=data)
print(req.text)
