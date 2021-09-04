import json
import random
import qrcode #pip install qrcode

with open("words.json") as f:
    word = json.load(f)

word = random.choice(word)

print(word)

data = word
img = qrcode.make(data)
img.save('qrcode.png')
