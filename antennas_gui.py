import pyautogui
import math
from math import *
# to be changed
pyautogui.click()

a1 = [66, 0.6]
a2 = [346, 0.6]
a3 = [212, 0.6]
a4 = [120, 0.6]
a5 = [310, 1.2]
a6 = [20, 0.6]

speed = 0.5
ant_azimuth = 60
# to be changed end

# towers locations

w1 = {"left": [763, 352, 770, 348],
      "right": [928, 332, 923, 336],
      "middle": [864, 486, 855, 472]}
w2 = {"left": [1129, 352, 1121, 348],
      "right": [1293, 332, 1293, 337],
      "middle": [1228, 483, 1223, 489]}

sP_w1_left = [714, 468]
sP_w1_right = [990, 468]
sP_w1_middle =[852, 231]

sP_w2_left = [1079, 468]
sP_w2_right = [1355, 468]
sP_w2_middle =[1217, 231]
# towers locations end

azimuths = [a2, a3, a4, a5, a6]

def visibility(elem):
    if elem == 0.3:
        pyautogui.press("enter")
    elif elem == 0.6:
        pyautogui.typewrite('0')
        pyautogui.moveTo(x=2411, y=752)
        pyautogui.click()
    else:
        pyautogui.typewrite('1')
        pyautogui.click(x=2411, y=752)

def degree_change(azimuth):
    if azimuth < 180:
        degree = 180
        return degree
    else:
        degree = 0
        return degree


def position(azimuth):
    alfa = azimuth - 90
    cos = math.cos(math.radians(alfa))
    sin = math.sin(math.radians(alfa))
    P0 = [1736, 882]
    P1 = [1738, 707]
    l = sqrt((P0[0]-P1[0])**2+(P0[1]-P1[1])**2)
    x1 = P0[0]+l*cos -(1736 - 996)
    y1 = P0[1]+l*sin
    return x1, y1


def rorate(a, v, lok):
    pyautogui.moveTo(x=1736, y=882, duration=speed)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.click(x=2430, y=733)
    visibility(v)
    pyautogui.typewrite(str(a))
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.typewrite(str(degree_change(a)))
    pyautogui.press("enter")
    pyautogui.moveTo(x=1736, y=882, duration=speed)
    pyautogui.click()
    pyautogui.click(x=996, y=882, duration=speed)
    pyautogui.click(position(a), duration=speed)
    pyautogui.moveTo(lok[0:2])
    pyautogui.scroll(1)
    pyautogui.scroll(1)
    pyautogui.scroll(1)
    pyautogui.scroll(1)
    pyautogui.click(lok[2:4], duration=speed)
    pyautogui.press("esc")
    pyautogui.middleClick()
    pyautogui.middleClick()


def retList():
    azimuth1 = [a1]
    azimuth2 = []
    for i in azimuths:
        if not len(azimuth1) == 3:
            if 60 < abs(i[0] - azimuth1[0][0]) < 160 or 230 < abs(i[0] - azimuth1[0][0]) < 330:
                azimuth1.append(i)
        else:
            azimuth2.append(i)
    return azimuth1, azimuth2

azimuth1, azimuth2 = retList()

def check1(elem):
    if 180 < elem < 300:
         return pozcheck(sP_w1_left,pozicionen(w1["left"],ant_azimuth),pozicionen(w1["right"],ant_azimuth),pozicionen(w1["middle"],ant_azimuth))
    elif 60 < elem < 180:
         return pozcheck(sP_w1_right,pozicionen(w1["right"],ant_azimuth),pozicionen(w1["left"],ant_azimuth),pozicionen(w1["middle"],ant_azimuth))
    else:
         return pozcheck(sP_w1_middle,pozicionen(w1["middle"],ant_azimuth),pozicionen(w1["left"],ant_azimuth),pozicionen(w1["right"],ant_azimuth))

def check2(elem):
    if 180 < elem < 315:
         return pozcheck(sP_w2_left,pozicionen(w2["left"],ant_azimuth),pozicionen(w2["right"],ant_azimuth),pozicionen(w2["middle"],ant_azimuth))
    elif 60 < elem < 180:
         return pozcheck(sP_w2_right,pozicionen(w2["right"],ant_azimuth),pozicionen(w2["left"],ant_azimuth),pozicionen(w2["middle"],ant_azimuth))
    else:
         return pozcheck(sP_w2_middle,pozicionen(w2["middle"],ant_azimuth),pozicionen(w2["left"],ant_azimuth),pozicionen(w2["right"],ant_azimuth))

def pozicionen (elem,az):
    if az < 120:
        az = az + 0
    if 120 < az < 240:
        az = az - 120
    if az > 240:
        az = az - 240
    if elem == w1["left"]:
        alfa = az - 120 - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        P0 = [851, 390]
        P1 = elem[0:2]
        P2 = elem[2:4]
        l1 = sqrt((P0[0] - P1[0]) ** 2 + (P0[1] - P1[1]) ** 2)
        l2 = sqrt((P0[0] - P2[0]) ** 2 + (P0[1] - P2[1]) ** 2)
        x1 = P0[0] + l1 * cos
        y1 = P0[1] + l1 * sin
        x2 = P0[0] + l2 * cos
        y2 = P0[1] + l2 * sin
        return [x1, y1, x2, y2]
    elif elem == w1["right"]:
        alfa = az - 240 - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        P0 = [851, 390]
        P1 = elem[0:2]
        P2 = elem[2:4]
        l1 = sqrt((P0[0] - P1[0]) ** 2 + (P0[1] - P1[1]) ** 2)
        l2 = sqrt((P0[0] - P2[0]) ** 2 + (P0[1] - P2[1]) ** 2)
        x1 = P0[0] + l1 * cos
        y1 = P0[1] + l1 * sin
        x2 = P0[0] + l2 * cos
        y2 = P0[1] + l2 * sin
        return [x1, y1, x2, y2]
    elif elem == w1["middle"]:
        alfa = az - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        P0 = [851, 390]
        P1 = elem[0:2]
        P2 = elem[2:4]
        l1 = sqrt((P0[0] - P1[0]) ** 2 + (P0[1] - P1[1]) ** 2)
        l2 = sqrt((P0[0] - P2[0]) ** 2 + (P0[1] - P2[1]) ** 2)
        x1 = P0[0] + l1 * cos
        y1 = P0[1] + l1 * sin
        x2 = P0[0] + l2 * cos
        y2 = P0[1] + l2 * sin
        return [x1, y1, x2, y2]
    elif elem == w2["left"]:
        alfa = az - 120 - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        P0 = [1216, 390]
        P1 = elem[0:2]
        P2 = elem[2:4]
        l1 = sqrt((P0[0] - P1[0]) ** 2 + (P0[1] - P1[1]) ** 2)
        l2 = sqrt((P0[0] - P2[0]) ** 2 + (P0[1] - P2[1]) ** 2)
        x1 = P0[0] + l1 * cos
        y1 = P0[1] + l1 * sin
        x2 = P0[0] + l2 * cos
        y2 = P0[1] + l2 * sin
        return [x1, y1, x2, y2]
    elif elem == w2["right"]:
        alfa = az - 240 - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        P0 = [1216, 390]
        P1 = elem[0:2]
        P2 = elem[2:4]
        l1 = sqrt((P0[0] - P1[0]) ** 2 + (P0[1] - P1[1]) ** 2)
        l2 = sqrt((P0[0] - P2[0]) ** 2 + (P0[1] - P2[1]) ** 2)
        x1 = P0[0] + l1 * cos
        y1 = P0[1] + l1 * sin
        x2 = P0[0] + l2 * cos
        y2 = P0[1] + l2 * sin
        return [x1, y1, x2, y2]
    elif elem == w2["middle"]:
        alfa = az - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        P0 = [1216, 390]
        P1 = elem[0:2]
        P2 = elem[2:4]
        l1 = sqrt((P0[0] - P1[0]) ** 2 + (P0[1] - P1[1]) ** 2)
        l2 = sqrt((P0[0] - P2[0]) ** 2 + (P0[1] - P2[1]) ** 2)
        x1 = P0[0] + l1 * cos
        y1 = P0[1] + l1 * sin
        x2 = P0[0] + l2 * cos
        y2 = P0[1] + l2 * sin
        return [x1, y1, x2, y2]



def pozcheck(sP,wclose,wfar1,wfar2):
    l1 = int(sqrt((sP[0] - wclose[0]) ** 2 + (sP[1] - wclose[1]) ** 2))
    l2 = int(sqrt((sP[0] - wfar1[0]) ** 2 + (sP[1] - wfar1[1]) ** 2))
    l3 = int(sqrt((sP[0] - wfar2[0]) ** 2 + (sP[1] - wfar2[1]) ** 2))
    lista = sorted([l1, l3, l2])
    if lista[0] == l1:
        return wclose


rorate(azimuth1[0][0],azimuth1[0][1],check1(azimuth1[0][0]))
rorate(azimuth1[1][0],azimuth1[1][1],check1(azimuth1[1][0]))
rorate(azimuth1[2][0],azimuth1[2][1],check1(azimuth1[2][0]))

rorate(azimuth2[0][0],azimuth2[0][1],check2(azimuth2[0][0]))
rorate(azimuth2[1][0],azimuth2[1][1],check2(azimuth2[1][0]))
rorate(azimuth2[2][0],azimuth2[2][1],check2(azimuth2[2][0]))

pyautogui.typewrite("rea")
pyautogui.press("space")
