import base64
import os

import hashlib
from zipfile import ZipFile
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Definition of a dictionary in which will be stored the associations
# between a hash and the corresponding character
hashs = {}

# Define imgs path
imgs_path = os.getcwd() + '/imgs'


def md5(image_path):

    hash_md5 = hashlib.md5()
    with open(image_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Loop over each images
for file in sorted(os.listdir(imgs_path)):

    target = imgs_path + '/' + file

    # Retrieve MD5 hash of the file
    m = md5(target)

    # If the hash is discovered for the first time, we associate it with the character contained in the image
    if m not in hashs:

        plt.imshow(
            mpimg.imread(target)
        )
        plt.ion()
        plt.show()
        char = input('Char in file ? : ')
        hashs[m] = char
    else:
        print("pass")


# Loop for the last time over each images
b64_flag = ''
for file in sorted(os.listdir(imgs_path)):

    target = imgs_path + '/' + file
    # Retrieve MD5 hash of the file
    m = md5(target)

    # Retrieve char associated with the char
    b64_flag = b64_flag + hashs.get(m)

# print the base64 flag
print(b64_flag)

# print reversed flag :
print(
    base64.b64decode(b64_flag)
)

