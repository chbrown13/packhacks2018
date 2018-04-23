from image_utils import ImageText
import os
import random

DIR = "images/"
FONT = 'impact.ttf'
COLOR = (255, 255, 255)
MEMES = {
    "crying_jordan": {'error': "{err}", 'msg': "{msg}"}, 
    "aliens": {'error': "{err}???????", 'msg': "{msg}"},
    "phelps": {'error': "{err}", 'msg': "{msg}"},
    "boondocks": {'error': "[{err}]...", 'msg': "{msg}"},
    "woman": {'error': "{err}", 'msg': "{msg}"},
    "math_woman": {'error': "{err}???", 'msg': "{msg}"},
    "morpheus": {'error': "What if I told you", 'msg': "{msg}?"},
    "think": {'error': "{err}...", 'msg': "{msg}",},
    "rock": {'top': (0, 150), 'bottom': (0, 350), 'error': "{err}?", 'msg': "{msg}"},
    "drake": {'top': (450, 100), 'bottom': (450, 400), 'error': "[{err}]", 'msg': "{msg}", 'width': 2, 'top_place': 'left', 'bottom_place': 'left'},
    "disaster_girl": {'top': (0, 0), 'bottom': (10, 200), 'error': "{err}?",  'msg': "{msg}", 'width': 1.5, 'top_place': 'center', 'bottom_place': 'center'},
    "lebron": {'error': "{err}", 'msg': "{msg}"},
    "nobody_got_time": {'error': "{err}? Ain't nobody got time for that!", 'msg': "{msg}"},
    "swaggy_p": {'error': "{err}???", 'msg': "{msg}???"},
    "jackie_chan": {'error': "{err}?!?", 'msg': "{msg}"},
    "futurama": {'error': "{err}", 'msg': "{msg}"},
    "denzel": {'error': "{err}!", 'msg': "{msg}"},
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
    print error
    msg = parse(message)
    img.write_text_box(meme.get('top', (0,0)), meme['error'].replace("{err}", error), box_width=img.size[0]/meme.get('width', 1), font_filename=FONT,
                   font_size=f_size, color=COLOR, place=meme.get('top_place', 'center'))
    img.write_text_box(meme.get('bottom', (0, img.size[1]*0.75)), meme['msg'].replace("{msg}", msg), box_width=img.size[0]/meme.get('width', 1), font_filename=FONT,
                   font_size=f_size, color=COLOR, place=meme.get('bottom_place', 'center'))

    pic = path.replace(".java", ".png")
    img.save(pic)
    return pic