from image_utils import ImageText
import os
import random

DIR = "images/"
COLOR = (255, 255, 255)
FONT = 'impact.ttf'
MEMES = {
    "crying_jordan": {'top': (0, 0), 'bottom': (0, 475), 'extra': "   )`:"},
    "aliens": {'top': (0, 0), 'bottom': (0, 360), 'extra': "???????"},
    "phelps": {'top': (0, 0), 'bottom': (0, 375), 'extra': ""},
    "boondocks": {'top': (0, 0), 'bottom': (0, 429), 'extra': "..."},
    "woman": {'top': (0, 0), 'bottom': (0, 625), 'extra': ""},
    "math_woman": {'top': (0, 0), 'bottom': (0, 650), 'extra': ""},
}

def parse(text):
    t = text.replace("^", "")
    return t
    
def get_meme():
    memes = [DIR+x for x in os.listdir(DIR) if x.endswith(".jpg") or x.endswith(".png")]
    m = random.choice(memes)
    print m
    return m

def memify(path, error, message):
    img = ImageText(get_meme())
    f_size = max(int(img.size[1]/25.0), 24)    
    name = img.filename.split("/")[1].split(".")[0]
    meme = MEMES[name]
    print meme
    msg = parse(message)
    img.write_text_box(meme['top'], error + meme['extra'], box_width=img.size[0], font_filename=FONT,
                   font_size=f_size, color=COLOR, place='center')
    img.write_text_box(meme['bottom'], msg, box_width=img.size[0], font_filename=FONT,
                   font_size=f_size, color=COLOR, place='center')

    pic = path.replace(".java", ".png")
    img.save(pic)
    return pic