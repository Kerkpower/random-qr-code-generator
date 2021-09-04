import json
import random
import qrcode #pip install qrcode

with open("words.json") as f:
    test = json.load(f)

word = random.choice(test)

print(word)

data = word
img = qrcode.make(data)
img.save('qrcode.png')