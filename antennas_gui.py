import pyautogui
import math
from math import *

# to be changed
a1 = [66, 0.6]
a2 = [346, 1.2]
a3 = [212, 0.6]
a4 = [120, 0.6]
a5 = [310, 1.2]
a6 = [249, 0.6]

tow_azimuth = 20
speed = 0
# to be changed end

# mouse location
# once set always will work
w1 = {"left": [769, 436],
      "right": [934, 437],
      "middle": [847, 292]}
w2 = {"left": [1133, 438],
      "right": [1299, 438],
      "middle": [1209, 291]}
prop_visib_pos = [2411, 752]
arrow_red_pos = [1736, 882]
ant_green_pos = [1736, 707]
mid_w1_pos = [851, 390]
mid_w2_pos = [1216, 389]
prop_below_vis_pos = [2430, 733]
offset_arrow_red = [996, 882]
# mouse location end


def visibility(elem):
    if elem == 0.3:
        pyautogui.press("enter")
    elif elem == 0.6:
        pyautogui.typewrite('0')
        pyautogui.click(prop_visib_pos)
    else:
        pyautogui.typewrite('1')
        pyautogui.click(prop_visib_pos)


def degree_change(azimuth):
    if azimuth < 180:
        return 180
    else:
        return 0


def rot_position(azimuth):
    alfa = azimuth - 90
    cos_alfa = math.cos(math.radians(alfa))
    sin_alfa = math.sin(math.radians(alfa))
    l = sqrt((arrow_red_pos[0] - ant_green_pos[0]) ** 2 + (arrow_red_pos[1] - ant_green_pos[1]) ** 2)
    x1 = arrow_red_pos[0] + l * cos_alfa - (arrow_red_pos[0] - offset_arrow_red[0])
    y1 = arrow_red_pos[1] + l * sin_alfa
    return x1, y1


def sort_az_list():
    azimuths = [a2, a3, a4, a5, a6]
    azimuth1 = [a1]
    azimuth2 = []
    for i in azimuths:
        if not len(azimuth1) == 3:
            if 30 < abs(i[0] - azimuth1[0][0]) < 150 or 210 < abs(i[0] - azimuth1[0][0]) < 330:
                azimuth1.append(i)
            else:
                azimuth2.append(i)
        else:
            azimuth2.append(i)
    return azimuth1, azimuth2


def antennas_pos_w(ant_azimuth, tow_az, tower):
    if tow_az < 120:
        tow_az += 0
    if 120 < tow_az < 240:
        tow_az -= 120
    if tow_az > 240:
        tow_az -= 240
    if 300 <= ant_azimuth <= 360 or 0 <= ant_azimuth < 60:
        if 300 <= tow_az <= 360 or 0 <= tow_az <= 60:
            return new_rotated_antenas_positions(tower["middle"], tow_az)
        elif 60 <= tow_az <= 120:
            return new_rotated_antenas_positions(tower["left"], tow_az)
    if 60 < ant_azimuth < 180:
        if 300 <= tow_az <= 360 or 0 <= tow_az <= 60:
            return new_rotated_antenas_positions(tower["right"], tow_az)
        elif 60 < tow_az <= 120:
            return new_rotated_antenas_positions(tower["middle"], tow_az)
    if 180 < ant_azimuth < 300:
        if 300 <= tow_az <= 360 or 0 <= tow_az <= 60:
            return new_rotated_antenas_positions(tower["left"], tow_az)
        elif 60 < tow_az <= 120:
            return new_rotated_antenas_positions(tower["right"], tow_az)


def new_rotated_antenas_positions(elem, az):
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
        l1 = sqrt((mid_w1_pos[0] - elem[0]) ** 2 + (mid_w1_pos[1] - elem[1]) ** 2)
        x1 = mid_w1_pos[0] + l1 * cos
        y1 = mid_w1_pos[1] + l1 * sin
        return [x1, y1]
    elif elem == w1["right"]:
        alfa = az - 240 - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w1_pos[0] - elem[0]) ** 2 + (mid_w1_pos[1] - elem[1]) ** 2)
        x1 = mid_w1_pos[0] + l1 * cos
        y1 = mid_w1_pos[1] + l1 * sin
        return [x1, y1]
    elif elem == w1["middle"]:
        alfa = az - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w1_pos[0] - elem[0]) ** 2 + (mid_w1_pos[1] - elem[1]) ** 2)
        x1 = mid_w1_pos[0] + l1 * cos
        y1 = mid_w1_pos[1] + l1 * sin
        return [x1, y1]
    elif elem == w2["left"]:
        alfa = az - 120 - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w2_pos[0] - elem[0]) ** 2 + (mid_w2_pos[1] - elem[1]) ** 2)
        x1 = mid_w2_pos[0] + l1 * cos
        y1 = mid_w2_pos[1] + l1 * sin
        return [x1, y1]
    elif elem == w2["right"]:
        alfa = az - 240 - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w2_pos[0] - elem[0]) ** 2 + (mid_w2_pos[1] - elem[1]) ** 2)
        x1 = mid_w2_pos[0] + l1 * cos
        y1 = mid_w2_pos[1] + l1 * sin
        return [x1, y1]
    elif elem == w2["middle"]:
        alfa = az - 90
        cos = math.cos(math.radians(alfa))
        sin = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w2_pos[0] - elem[0]) ** 2 + (mid_w2_pos[1] - elem[1]) ** 2)
        x1 = mid_w2_pos[0] + l1 * cos
        y1 = mid_w2_pos[1] + l1 * sin
        return [x1, y1]


def rorate(a, v, lok):
    pyautogui.click(arrow_red_pos, duration=speed)
    pyautogui.press("enter")
    pyautogui.click(prop_below_vis_pos)
    visibility(v)
    pyautogui.typewrite(str(a))
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.typewrite(str(degree_change(a)))
    pyautogui.press("enter")
    pyautogui.click(arrow_red_pos, duration=speed)
    pyautogui.click(offset_arrow_red, duration=speed)
    pyautogui.click(mid_w1_pos, duration=speed)
    pyautogui.click(mid_w2_pos, duration=speed)
    pyautogui.click(rot_position(a), duration=speed)
    pyautogui.press("f3")
    pyautogui.click(lok[0:2])
    pyautogui.press("f3")
    pyautogui.press("esc")


def towers_rotate(tow_az):
    pyautogui.click()
    pyautogui.click(mid_w1_pos, duration=speed)
    pyautogui.click(mid_w2_pos, duration=speed)
    pyautogui.click(prop_below_vis_pos)
    pyautogui.typewrite(str(tow_az))
    pyautogui.press("enter")
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.press("esc")


azimuth1, azimuth2 = sort_az_list()
towers_rotate(tow_azimuth)
rorate(azimuth1[0][0], azimuth1[0][1], antennas_pos_w(azimuth1[0][0], tow_azimuth, w1))
rorate(azimuth1[1][0], azimuth1[1][1], antennas_pos_w(azimuth1[1][0], tow_azimuth, w1))
rorate(azimuth1[2][0], azimuth1[2][1], antennas_pos_w(azimuth1[2][0], tow_azimuth, w1))

rorate(azimuth2[0][0], azimuth2[0][1], antennas_pos_w(azimuth2[0][0], tow_azimuth, w2))
rorate(azimuth2[1][0], azimuth2[1][1], antennas_pos_w(azimuth2[1][0], tow_azimuth, w2))
rorate(azimuth2[2][0], azimuth2[2][1], antennas_pos_w(azimuth2[2][0], tow_azimuth, w2))

pyautogui.typewrite("rea")
pyautogui.press("space")
