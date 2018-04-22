from image_utils import ImageText
import os
import random

DIR = "images/"

#TODO: divide error message, top/bottom meme text

def parse(text):
    t = text.replace(": error:", "")
    header = t[0:t.index("]") + 1]
    footer = t[t.index("]")+1:t.index("(see")]
    return (header, footer)
    
def get_meme():
    memes = [DIR+x for x in os.listdir(DIR) if x.endswith(".jpg") or x.endswith(".png")]
    print memes
    m = random.choice(memes)
    print m
    return m

color = (255, 255, 255)
text = "ShortSet.java:6: error: [CollectionIncompatibleType] Argument 'i - 1' should not be passed to this method;\nits type int is not compatible with its collection's type argument Short\n      s.remove(i - 1);\n              ^\n    (see http://errorprone.info/bugpattern/CollectionIncompatibleType)"
font = 'impact.ttf'
img = ImageText(get_meme())
f_size = max(int(img.size[1]/25.0), 24)

texts = parse(text)
print img.size, f_size
img.write_text_box((0, 0), texts[0], box_width=img.size[0], font_filename=font,
                   font_size=f_size, color=color, place='center')

img.write_text_box((0, (3*img.size[1])/4), texts[1], box_width=img.size[0], font_filename=font,
                   font_size=f_size, color=color, place='center')

img.save('sample-imagetext.png')