# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
bossImg=Template(r"tpl1583547817862.png", threshold=0.75, record_pos=(0.0, -0.009), resolution=(1136, 640))
newImg=Template(r"tpl1585580707626.png", threshold=0.8500000000000001, record_pos=(-0.246, 0.117), resolution=(1440, 810))
bujiImg=Template(r"tpl1585662451330.png", record_pos=(0.311, 0.134), resolution=(1440, 810))#Template(r"tpl1584107269046.png", record_pos=(0.048, 0.031), resolution=(1440, 810))
zhuliImg=Template(r"tpl1585658118711.png", record_pos=(-0.056, -0.16), resolution=(1440, 810))#Template(r"tpl1584102672051.png", record_pos=(0.29, 0.0), resolution=(1440, 810))
zhencaImg=Template(r"tpl1585658134305.png", record_pos=(0.035, -0.155), resolution=(1440, 810))#Template(r"tpl1584107299547.png", record_pos=(-0.293, 0.176), resolution=(1440, 810))
hanmuImg=Template(r"tpl1585658149934.png", record_pos=(0.228, -0.093), resolution=(1440, 810))#Template(r"tpl1584102556381.png", record_pos=(0.23, 0.016), resolution=(1440, 810))
buji=Template(r"tpl1584102835763.png", record_pos=(0.209, -0.172), resolution=(1440, 810))
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
def hideQiantin():
    touch(Template(r"tpl1584785483325.png", record_pos=(0.462, 0.063), resolution=(1440, 810)))
    sleep(1)
    touch([1393, 503])
    sleep(1)
    touch([1210, 483])
    sleep(1)
def weixiu(number):
    if (number >= 5 and number <= 7):
        if exists(Template(r"tpl1584103499581.png", record_pos=(-0.407, 0.136), resolution=(1440, 810))):
            touch(Template(r"tpl1584103499581.png", record_pos=(-0.407, 0.136), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1584865510293.png", record_pos=(0.09, 0.068), resolution=(1440, 810)))
            sleep(1)
            if exists(Template(r"tpl1584865601517.png", record_pos=(-0.113, -0.115), resolution=(1440, 810))):
                touch(Template(r"tpl1584865611644.png", record_pos=(0.2, -0.117), resolution=(1440, 810)))
    
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
    while exists(Template(r"tpl1584775112579.png", record_pos=(0.463, 0.026), resolution=(1440, 810))):
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
def GetPoint():
    point = exists(newImg)
    if point:
            return point
    point = exists(bujiImg)
    if point:
            return point
    point = exists(zhencaImg)
    if point:
            return point
    point = exists(hanmuImg)
    if point:
            return point
    point = exists(zhuliImg)
    if point:
            return point
    return False
def GetBossPoint():
    return exists(bossImg)
def GetBujiPoint():
    return exists(buji)
def FindInMap(img,isloop=False):
    point=img()
    if UnableClick(point):
        SwipeFunc([857, 181],[217, 183]) #左移
        point=img()
        if UnableClick(point):
            SwipeFunc([1184, 672],[1187, 182]) #上移
            point=img()
            if UnableClick(point):
                SwipeFunc([184, 672],[847, 672]) #右移
                point=img()
                if UnableClick(point):
                    SwipeFunc([184, 672],[847, 672]) #右移
                    point=img()
                    if UnableClick(point):
                        SwipeFunc([184, 184],[184, 672]) #下移
                        point=img()
                        if UnableClick(point):
                            SwipeFunc([857, 182],[217, 181]) #左移
                            point=img()
                            if UnableClick(point):
                                SwipeFunc([857, 182],[217, 181]) #左移
                                point=img()
    if not UnableClick(point):
        touch(point)
    elif isloop:
        FindInMap(img,isloop)
def FindBoss():
    FindInMap(GetBossPoint,True)
def FindEnemy():
    FindInMap(GetPoint)
def FindBuji():
    FindInMap(GetBujiPoint)
def Dalao():
    number=0
    loop=True
    hideQiantin()
    while loop:
        number=number+1
        print("----第几次--------")
        print(number)
        #if number==4:
            #print("----找补给--------")
            #FindBuji()
            #continue
        if exists(bossImg):
            loop=False
            SwitchTeam()
            FindBoss()
        else:
            FindEnemy()
        sleep(10)
        touchOther()
        #weixiu(number)
        fight()
print("start sp3")
#touch(Template(r"tpl1583557219783.png", record_pos=(0.339, -0.028), resolution=(1136, 640)))
#sleep(1)
number=0
while number<10:
    #guanqia=exists(Template(r"tpl1584781122594.png", record_pos=(0.24, 0.052), resolution=(1440, 810)))
    guanqia=exists(Template(r"tpl1585580778071.png", threshold=0.8500000000000001, record_pos=(0.233, -0.039), resolution=(1440, 810)))
    if guanqia:
        touch(guanqia)
        sleep(1)
        if exists(Template(r"tpl1584776330893.png", threshold=0.9000000000000001, record_pos=(0.243, 0.124), resolution=(1440, 810))):
            touch(Template(r"tpl1584776330893.png", record_pos=(0.243, 0.124), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1584776330893.png", record_pos=(0.243, 0.124), resolution=(1440, 810)))
            sleep(2)
        Dalao()
    number=number+1
    print("----number--------")
    print(number)
