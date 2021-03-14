import pyautogui
import math
from math import *

# to be changed
a1 = [96, 0.6, 1]
a2 = [180, 0.6, 2]
a3 = [113, 0.6, 3]
a4 = [252, 0.6, 4]
a5 = [288, 0.6, 5]
a6 = [20, 0.6, 6]

tow_check_E = "E3"      # E2 or E3 # note that: E4 == E3
tow_azimuth = 344
speed = 0
# to be changed end

# todo 2: try to split function that counts new rotated coordinates
# todo 4: do something with that cos, sin, and also with lists named azimuths, azimuths1 and azimuths2

# mouse location
# once set always will work
mid_w1_pos = [1180, 447]
mid_w2_pos = [1627, 447]
prop_visib_pos = [2411, 733]
arrow_red_pos = [1840, 1087]
cross_ant_local = [228, 357]
all_a = [a1, a2, a3, a4, a5, a6]


def tower_type(tow_check):
    if tow_check == "E2":
        return [0, 0, 0]
    elif tow_check == "E3":
        return [21, 16, 11]


w1 = {"left": [mid_w1_pos[0] - (60 + tower_type(tow_check_E)[1]), mid_w1_pos[1] + (32 + tower_type(tow_check_E)[2])],
      "right": [mid_w1_pos[0] + (60 + tower_type(tow_check_E)[1]), mid_w1_pos[1] + (32 + tower_type(tow_check_E)[2])],
      "middle": [mid_w1_pos[0], mid_w1_pos[1] - (68 + tower_type(tow_check_E)[0])]}
w2 = {"left": [mid_w2_pos[0] - (60 + tower_type(tow_check_E)[1]), mid_w2_pos[1] + (32 + tower_type(tow_check_E)[2])],
      "right": [mid_w2_pos[0] + (60 + tower_type(tow_check_E)[1]), mid_w2_pos[1] + (32 + tower_type(tow_check_E)[2])],
      "middle": [mid_w2_pos[0], mid_w2_pos[1] - (68 + tower_type(tow_check_E)[0])]}
prop_below_vis_pos = [prop_visib_pos[0], prop_visib_pos[1] + 19]
ant_green_pos = [arrow_red_pos[0], arrow_red_pos[1] - 160]
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
    x1 = poz1[0] + l * cos_alfa
    y1 = poz1[1] + l * sin_alfa
    return x1, y1


def sort_az_list():
    azimuths = [a2, a3, a4, a5, a6]
    azimuth1 = [a1]
    azimuth2 = []
    for elem in azimuths:
        if not len(azimuth1) == 3:
            if 30 < abs(elem[0] - azimuth1[0][0]) < 150 or 210 < abs(elem[0] - azimuth1[0][0]) < 330:
                azimuth1.append(elem)
            else:
                azimuth2.append(elem)
        else:
            azimuth2.append(elem)
    return azimuth1, azimuth2


def azimuth_check(az):
    if az < 120:
        return az
    elif 120 <= az < 240:
        return az - 120
    else:
        return az - 240


def antennas_pos_w(ant_azimuth, tow_az, tower):
    if 300 <= ant_azimuth[0] <= 360 or 0 <= ant_azimuth[0] <= 60:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antennas_positions(tower["middle"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antennas_positions(tower["left"], azimuth_check(tow_az))
    if 60 < ant_azimuth[0] < 180:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antennas_positions(tower["right"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antennas_positions(tower["middle"], azimuth_check(tow_az))
    if 180 <= ant_azimuth[0] < 300:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antennas_positions(tower["left"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antennas_positions(tower["right"], azimuth_check(tow_az))


def new_rotated_antennas_positions(elem, az):
    if elem == w1["left"]:
        alfa = az - 120 - 90
        cos_alfa = math.cos(math.radians(alfa))
        sin_alfa = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w1_pos[0] - elem[0]) ** 2 + (mid_w1_pos[1] - elem[1]) ** 2)
        x1 = mid_w1_pos[0] + l1 * cos_alfa
        y1 = mid_w1_pos[1] + l1 * sin_alfa
        return [x1, y1]
    elif elem == w1["right"]:
        alfa = az - 240 - 90
        cos_alfa = math.cos(math.radians(alfa))
        sin_alfa = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w1_pos[0] - elem[0]) ** 2 + (mid_w1_pos[1] - elem[1]) ** 2)
        x1 = mid_w1_pos[0] + l1 * cos_alfa
        y1 = mid_w1_pos[1] + l1 * sin_alfa
        return [x1, y1]
    elif elem == w1["middle"]:
        alfa = az - 90
        cos_alfa = math.cos(math.radians(alfa))
        sin_alfa = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w1_pos[0] - elem[0]) ** 2 + (mid_w1_pos[1] - elem[1]) ** 2)
        x1 = mid_w1_pos[0] + l1 * cos_alfa
        y1 = mid_w1_pos[1] + l1 * sin_alfa
        return [x1, y1]
    elif elem == w2["left"]:
        alfa = az - 120 - 90
        cos_alfa = math.cos(math.radians(alfa))
        sin_alfa = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w2_pos[0] - elem[0]) ** 2 + (mid_w2_pos[1] - elem[1]) ** 2)
        x1 = mid_w2_pos[0] + l1 * cos_alfa
        y1 = mid_w2_pos[1] + l1 * sin_alfa
        return [x1, y1]
    elif elem == w2["right"]:
        alfa = az - 240 - 90
        cos_alfa = math.cos(math.radians(alfa))
        sin_alfa = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w2_pos[0] - elem[0]) ** 2 + (mid_w2_pos[1] - elem[1]) ** 2)
        x1 = mid_w2_pos[0] + l1 * cos_alfa
        y1 = mid_w2_pos[1] + l1 * sin_alfa
        return [x1, y1]
    elif elem == w2["middle"]:
        alfa = az - 90
        cos_alfa = math.cos(math.radians(alfa))
        sin_alfa = math.sin(math.radians(alfa))
        l1 = sqrt((mid_w2_pos[0] - elem[0]) ** 2 + (mid_w2_pos[1] - elem[1]) ** 2)
        x1 = mid_w2_pos[0] + l1 * cos_alfa
        y1 = mid_w2_pos[1] + l1 * sin_alfa
        return [x1, y1]


def rotate(az, visib, lok):
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.click(prop_visib_pos)
    visibility(visib[1])
    pyautogui.typewrite(str(az[0]))
    pyautogui.press("enter")
    pyautogui.typewrite(str(az[2]))
    pyautogui.press("enter")
    pyautogui.typewrite(str(degree_change(az[0])))
    pyautogui.press("enter")
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.click()
    pyautogui.click(offset_arrow_red, duration=speed)
    pyautogui.moveTo(mid_w1_pos, duration=speed)
    pyautogui.click()
    pyautogui.moveTo(mid_w2_pos, duration=speed)
    pyautogui.click()
    pyautogui.moveTo(rot_position(az[0], arrow_red_pos, ant_green_pos)[0] - (arrow_red_pos[0] - offset_arrow_red[0]),
                     rot_position(az[0], arrow_red_pos, ant_green_pos)[1], duration=speed)
    pyautogui.click()
    pyautogui.press("f3")
    pyautogui.moveTo(lok, duration=speed)
    pyautogui.click()
    pyautogui.press("f3")
    pyautogui.press("esc")


def towers_rotate(tow_az, tow_check):
    pyautogui.click()
    pyautogui.click(mid_w1_pos, duration=speed)
    pyautogui.click(mid_w2_pos, duration=speed)
    if tow_check == "E3":
        pyautogui.click(prop_visib_pos)
        pyautogui.typewrite("e")
    pyautogui.click(prop_below_vis_pos)
    pyautogui.typewrite(str(tow_az))
    pyautogui.press("enter")
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.press("esc")


def visib_check(antenna):
    if antenna == 0.6:
        return cross_ant_local
    if antenna == 1.2:
        return [cross_ant_local[0], cross_ant_local[1] + 150]
    if antenna == 0.3:
        return [cross_ant_local[0], cross_ant_local[1] + 300]


def cross_antennas(antenna, number):
    pyautogui.click()
    pyautogui.moveTo(visib_check(antenna[1]), duration=speed)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.click(prop_visib_pos)
    for elem in range(rotate_cross_antennas(set_cross_antennas_angle(antenna[0], tow_azimuth))[1]):
        pyautogui.typewrite(str(rotate_cross_antennas(set_cross_antennas_angle(antenna[0], tow_azimuth))[0]))
    pyautogui.moveTo(prop_below_vis_pos, duration=speed)
    pyautogui.click()
    pyautogui.typewrite(str(antenna[0]))
    pyautogui.press("enter")
    pyautogui.typewrite(str(number[2]))
    pyautogui.press("enter")
    pyautogui.click(visib_check(antenna[1]))
    if antenna == azimuth1[0] or antenna == azimuth1[1] or antenna == azimuth1[2]:
        move = [800, 420]
    else:
        move = [1951, 420]
    pyautogui.click(move)
    pyautogui.press("esc")


def set_cross_antennas_angle(azimuth, az_tow):
    if azimuth - az_tow > 0:
        return azimuth - az_tow
    else:
        return 360 + (azimuth - az_tow)


def rotate_cross_antennas(angle):
    angle = round(angle/10)
    if angle < 10:
        return [angle, 1]
    elif 10 <= angle < 20:
        return [1, angle - 8]
    elif 20 <= angle < 30:
        return [2, angle - 18]
    elif angle == 36:
        return [0, 0]
    else:
        return [3, angle - 28]


azimuth1, azimuth2 = sort_az_list()
towers_rotate(tow_azimuth, tow_check_E)
for i in range(3):
    rotate(azimuth1[i], azimuth1[i], antennas_pos_w(azimuth1[i], tow_azimuth, w1))
    rotate(azimuth2[i], azimuth2[i], antennas_pos_w(azimuth2[i], tow_azimuth, w2))
    cross_antennas(azimuth1[i], azimuth1[i])
    cross_antennas(azimuth2[i], azimuth2[i])
pyautogui.typewrite("rea")
pyautogui.press("space")
