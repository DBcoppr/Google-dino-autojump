
# #dinosaur testing
import pyautogui as py
from time import sleep
from os import chdir
from PIL import ImageGra
chdir('c:\\users\\tarikh\\downloads')
def strt():
    py.click((893,1056),duration=0.5)
    py.click((800,900),duration=0.5)
    py.press('up')

def prss(str):
    py.press(str)


def guess():
      sleep(3)
      #bird
      im = py.screenshot()
      for i in range(280,294):
          for j in range(795,828):
              im.putpixel((j,i),(25,20,0))

      #cactus
      for i in range(315,326):
          for j in range(788,825):
              im.putpixel((j,i),(255,0,0))

      im.show()
def putt():
    im = py.screenshot()


    for i in range(315, 326):
        for j in range(788,825):
           # print(im.getpixel((j,i)))
            for k in im.getpixel((j, i)):
                if k<100 :
                    py.press('up')
                    return 0
    #
    # for i in range(280, 294):
    #      for j in range(795, 828):
    #         for k in im.getpixel((j, i)):
    #             if k<100:
    #                 py.press('down')
    #                 return 0
#guess()
strt()
while True:
   putt()








