# Antennas-GUI
## Overview
An application that helps with setting antennas azimuths.  
I figure it out during my work in design office, where my duty was to plan first towers and antennas locations. To speed up my work I wrote this.  
Python version 3.8  
Used librabry:
- pyautogui
- math
- time

Used draft program:
- AutoCAD 2D

## Description
It includes similar moves accoring coordinates of certain parts of antennas.  
The main inputs are antennas azimuths their visibility states which are diameters and consecutive number.  
GUI application helps designer to solve the problem about antennas positions on towers, it saves a lot of time.  
Due prevously prepared dynamic blocks and inserted fields in CAD all informations are automatically updating.  
Program creates zones for rotated towers wings and fits antennas with written azimuths.  
All should be set in the begining of the project. Only one value which has to be given is towers angle degree based on towers location plan.  
## Below gif showing script capabilities
Script execution might be speeded up by setting value: speed = 0.  
Gif was made with speed = 0.3, it might work faster

![Antennas-GUI.gif](https://github.com/kamilego/Antennas-GUI/blob/main/demo/Antennas-GUI.gif)
