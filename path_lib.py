from os import path

#__file__ встроенная переменная которая содержит полный путь к исполняемому скрипту
img_dir = path.join(path.dirname(__file__),'images')
font_dir = path.join(path.dirname(__file__),'fonts')

# в основном теле
 #   from path_lib import *

 #  print(img_dir)