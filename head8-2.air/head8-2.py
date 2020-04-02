# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

bossImg=Template(r"tpl1583547817862.png", threshold=0.75, record_pos=(0.0, -0.009), resolution=(1136, 640))
def fight():
    touch(Template(r"tpl1583507548323.png", record_pos=(0.389, 0.216), resolution=(1136, 640)))
    wait(Template(r"tpl1583507625050.png", record_pos=(-0.277, 0.21), resolution=(1136, 640)),300,10)
    touch(Template(r"tpl1583507633547.png", record_pos=(-0.323, 0.207), resolution=(1136, 640)))
    sleep(1)
    touch(Template(r"tpl1583507667985.png", record_pos=(0.0, 0.095), resolution=(1136, 640)))
    sleep(1)
    if exists(Template(r"tpl1584797467959.png", record_pos=(-0.448, 0.132), resolution=(1440, 810))):
        touch([875, 487])
    touch(Template(r"tpl1583507688609.png", record_pos=(0.346, 0.232), resolution=(1136, 640)))
    sleep(2)
    touchInfo()
    
def touchInfo():
    if exists(Template(r"tpl1583508935293.png", record_pos=(-0.162, -0.128), resolution=(1136, 640))):
        touch(Template(r"tpl1583508941997.png", record_pos=(-0.011, 0.119), resolution=(1136, 640)))  
        sleep(2)
def touchOther():
    if exists(Template(r"tpl1583508935293.png", record_pos=(-0.162, -0.128), resolution=(1136, 640))):
        touch(Template(r"tpl1583508941997.png", record_pos=(-0.011, 0.119), resolution=(1136, 640)))
        sleep(1)
    if exists(Template(r"tpl1584103218714.png", record_pos=(0.244, 0.087), resolution=(1440, 810))):
        touch(Template(r"tpl1584103232890.png", record_pos=(0.331, 0.087), resolution=(1440, 810)))
        sleep(2)
      
def SwitchTeam():
    touch(Template(r"tpl1583548898282.png", record_pos=(0.305, 0.249), resolution=(1136, 640)))
    sleep(1)

def Reset():
    SwitchTeam()
    SwitchTeam()
    
    
def FindFleet():
    while exists(Template(r"tpl1583561633883.png", record_pos=(0.221, -0.014), resolution=(1136, 640))):
        touch(Template(r"tpl1583561633883.png", record_pos=(0.221, -0.014), resolution=(1136, 640)))
        sleep(1)
        
def FindMap():
    if exists(Template(r"tpl1584775112579.png", record_pos=(0.463, 0.026), resolution=(1440, 810))):
        touch(Template(r"tpl1584775112579.png", record_pos=(0.463, 0.026), resolution=(1440, 810)))
        sleep(1)
    touch(Template(r"tpl1584775214154.png", record_pos=(-0.46, 0.022), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1584775214154.png", record_pos=(-0.46, 0.022), resolution=(1440, 810)))
    sleep(1)
        
def SwipeFunc(start,end):
    swipe(start,end)
    sleep(2)
def UnableClick(point):
    return point==False or point[1]<180 or point[0]<150

def GetBossPoint():
    return exists(bossImg)
def FindInMap(img,isloop=False):
    point=img()
    if UnableClick(point):
        SwipeFunc([184, 184],[184, 672]) #下移
        point=img()
    if not UnableClick(point):
        touch(point)
    elif isloop:
        FindInMap(img,isloop)
def FindBoss():
    FindInMap(GetBossPoint,True)

def Dalao():
    SwitchTeam()
    FindBoss()
    sleep(10)
    touchOther()
    #weixiu(number)
    fight()
        
print("start head")
#touch(Template(r"tpl1583557219783.png", record_pos=(0.339, -0.028), resolution=(1136, 640)))
sleep(1)
#if exists(Template(r"tpl1584773637190.png", record_pos=(-0.431, 0.231), resolution=(1440, 810))):
    #touch(Template(r"tpl1584773637190.png", record_pos=(-0.431, 0.231), resolution=(1440, 810)))
    #FindMap()
number=0
while number<3:
    guanqia=exists(Template(r"tpl1584775394507.png", record_pos=(-0.222, 0.026), resolution=(1440, 810)))
    if guanqia:
        touch(guanqia)
        sleep(1)
        if exists(Template(r"tpl1584776330893.png", threshold=0.9000000000000001, record_pos=(0.243, 0.124), resolution=(1440, 810))):
            touch(Template(r"tpl1584776330893.png", record_pos=(0.243, 0.124), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1584776330893.png", record_pos=(0.243, 0.124), resolution=(1440, 810)))
            sleep(10)
        Dalao()
    number=number+1
    print("----number--------")
    print(number)