from image_utils import ImageText
import os
import random

DIR = "images/"
FONT = 'impact.ttf'
MEMES = {
    "crying_jordan": {'top': (0, 0), 'bottom': (0, 475), 'error': "{err}     )`:", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'}, 
    "aliens": {'top': (0, 0), 'bottom': (0, 325), 'error': "{err}???????", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "phelps": {'top': (0, 0), 'bottom': (0, 375), 'error': "{err}", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "boondocks": {'top': (0, 0), 'bottom': (0, 429), 'error': "[{err}]...", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "woman": {'top': (0, 0), 'bottom': (0, 625), 'error': "{err}", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "math_woman": {'top': (0, 0), 'bottom': (0, 650), 'error': "{err}???", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "morpheus": {'top': (0, 0), 'bottom': (0, 180), 'error': "What if I told you", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "think": {'top': (0, 0), 'bottom': (0, 300), 'error': "{err}...", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "rock": {'top': (0, 150), 'bottom': (0, 350), 'error': "{err}?", 'color': (255, 255, 255), 'width': 1, 'top_place': 'center', 'bottom_place': 'center'},
    "drake": {'top': (300, 0), 'bottom': (400, 500), 'error': "{err}?", 'color': (20, 20, 20), 'width': 2, 'top_place': 'center', 'bottom_place': 'center'},
    "disaster_girl": {'top': (0, 50), 'bottom': (10, 200), 'error': "{err}?", 'color': (255, 255, 255), 'width': 1.5, 'top_place': 'left', 'bottom_place': 'center'},
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
    img.write_text_box(meme['top'], meme['error'].replace("{err}", error), box_width=img.size[0]/meme['width'], font_filename=FONT,
                   font_size=f_size, color=meme['color'], place=meme['top_place'])
    img.write_text_box(meme['bottom'], msg, box_width=img.size[0]/meme['width'], font_filename=FONT,
                   font_size=f_size, color=meme['color'], place=meme['bottom_place'])

    pic = path.replace(".java", ".png")
    img.save(pic)
    return pic