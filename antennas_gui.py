import pyautogui
import math
from math import *

# to be changed
a1 = [66, 0.6]
a2 = [346, 1.2]
a3 = [212, 0.6]
a4 = [120, 0.6]
a5 = [310, 1.2]
a6 = [221, 0.6]

tow_azimuth = 264
speed = 0
# to be changed end

# mouse location
# once set always will work
w1 = {"left": [769, 436],
      "right": [934, 437],
      "middle": [847, 292]}
w2 = {"left": [w1["left"][0] + 365, w1["left"][1]],
      "right": [w1["right"][0] + 365, w1["right"][1]],
      "middle": [w1["middle"][0] + 365, w1["middle"][1]]}
prop_below_vis_pos = [2411, 752]
prop_visib_pos = [prop_below_vis_pos[0], prop_below_vis_pos[1] - 19]
arrow_red_pos = [1736, 882]
ant_green_pos = [arrow_red_pos[0], arrow_red_pos[1] - 175]
mid_w1_pos = [851, 390]
mid_w2_pos = [mid_w1_pos[0] + 365, mid_w1_pos[1]]
offset_arrow_red = [arrow_red_pos[0] - 740, arrow_red_pos[1]]
# mouse location end


def visibility(elem):
    if elem == 0.3:
        pyautogui.press("enter")
    elif elem == 0.6:
        pyautogui.typewrite('0')
        pyautogui.click(prop_below_vis_pos)
    else:
        pyautogui.typewrite('1')
        pyautogui.click(prop_below_vis_pos)


def degree_change(azimuth):
    if azimuth < 180:
        return 180
    else:
        return 0


def rot_position(azimuth, poz1, poz2):
    alfa = azimuth - 90
    cos_alfa = math.cos(math.radians(alfa))
    sin_alfa = math.sin(math.radians(alfa))
    l = sqrt((poz1[0] - poz2[0]) ** 2 + (poz1[1] - poz2[1]) ** 2)
    x1 = poz1[0] + l * cos_alfa - (poz1[0] - offset_arrow_red[0])
    y1 = poz1[1] + l * sin_alfa
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


def azimuth_check(az):
    if az < 120:
        return az
    elif 120 <= az < 240:
        return az - 120
    else:
        return az - 240


def antennas_pos_w(ant_azimuth, tow_az, tower):
    if 300 <= ant_azimuth <= 360 or 0 <= ant_azimuth <= 60:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antenas_positions(tower["middle"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antenas_positions(tower["left"], azimuth_check(tow_az))
    if 60 < ant_azimuth < 180:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antenas_positions(tower["right"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antenas_positions(tower["middle"], azimuth_check(tow_az))
    if 180 <= ant_azimuth < 300:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antenas_positions(tower["left"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antenas_positions(tower["right"], azimuth_check(tow_az))


def new_rotated_antenas_positions(elem, az):
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
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.click(prop_visib_pos)
    visibility(v)
    pyautogui.typewrite(str(a))
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.typewrite(str(degree_change(a)))
    pyautogui.press("enter")
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.click()
    pyautogui.click(offset_arrow_red, duration=speed)
    pyautogui.moveTo(mid_w1_pos, duration=speed)
    pyautogui.click()
    pyautogui.moveTo(mid_w2_pos, duration=speed)
    pyautogui.click()
    pyautogui.moveTo(rot_position(a, arrow_red_pos, ant_green_pos), duration=speed)
    pyautogui.click()
    pyautogui.press("f3")
    pyautogui.moveTo(lok)
    pyautogui.click()
    pyautogui.press("f3")
    pyautogui.press("esc")


def towers_rotate(tow_az):
    pyautogui.click()
    pyautogui.click(mid_w1_pos, duration=speed)
    pyautogui.click(mid_w2_pos, duration=speed)
    pyautogui.click(prop_visib_pos)
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
