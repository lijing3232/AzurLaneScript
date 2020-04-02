# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
#每日
def Exit():
    if exists(Template(r"tpl1583563297011.png", record_pos=(-0.456, -0.243), resolution=(1136, 640))):
        touch(Template(r"tpl1583563297011.png", record_pos=(-0.456, -0.243), resolution=(1136, 640)))
        sleep(1)
        
def EnableAuto():
    if exists(Template(r"tpl1583566509405.png", record_pos=(0.11, -0.188), resolution=(1440, 810))):
        touch(Template(r"tpl1583566509405.png", record_pos=(0.11, -0.188), resolution=(1440, 810)))
        sleep(1)
def CloseInfo():
    if exists(Template(r"tpl1583636158951.png", record_pos=(-0.037, -0.14), resolution=(1440, 810))):
        touch([877, 537])
        touch(Template(r"tpl1583636231770.png", record_pos=(-0.003, 0.153), resolution=(1440, 810)))

        sleep(1)
    
def FindFleet():
    while exists(Template(r"tpl1583561633883.png", record_pos=(0.221, -0.014), resolution=(1136, 640))):
        touch(Template(r"tpl1583561633883.png", record_pos=(0.221, -0.014), resolution=(1136, 640)))
        sleep(1)

def Fight():
    touch(Template(r"tpl1583560082190.png", record_pos=(0.391, 0.216), resolution=(1136, 640)))
    sleep(1)
    if exists(Template(r"tpl1583498203239.png", record_pos=(-0.16, -0.114), resolution=(1136, 640))):
        touch(Template(r"tpl1583498213916.png", record_pos=(0.112, 0.131), resolution=(1136, 640)))
        sleep(1)
        touch(Template(r"tpl1583560082190.png", record_pos=(0.391, 0.216), resolution=(1136, 640)))
        sleep(1)
    print("出击")
    wait(Template(r"tpl1583557341072.png", record_pos=(-0.309, 0.212), resolution=(1136, 640)),180,5)
    touch(Template(r"tpl1583557341072.png", record_pos=(-0.309, 0.212), resolution=(1136, 640)))
    sleep(2)
    touch(Template(r"tpl1583557357276.png", record_pos=(-0.003, 0.096), resolution=(1136, 640)))
    sleep(1)
    touch(Template(r"tpl1583557371231.png", record_pos=(0.347, 0.233), resolution=(1136, 640)))

        
print("每日开始")
touch(Template(r"tpl1583557219783.png", record_pos=(0.339, -0.028), resolution=(1136, 640)))
sleep(1)
touch(Template(r"tpl1583559997601.png", record_pos=(0.142, 0.247), resolution=(1136, 640)))
sleep(1)
yanxiu=3
while yanxiu > 0:
    yanxiu=yanxiu-1
    touch(Template(r"tpl1583560043568.png", record_pos=(-0.022, 0.102), resolution=(1136, 640)))
    sleep(1)
    touch([620, 575]) # 战术研修(雷击)
    sleep(1)
    CloseInfo()
    if not exists(Template(r"tpl1583560082190.png", record_pos=(0.391, 0.216), resolution=(1136, 640))):
        break
    sleep(1)
    EnableAuto()
    FindFleet()
    print("第一次每日潜艇")
    Fight()
    
Exit()
# 斩首行动
def  zhanshou():
    zhanshou=3
    while zhanshou > 0:
        zhanshou=zhanshou-1
        touch(Template(r"tpl1583565220994.png", record_pos=(-0.145, -0.126), resolution=(1440, 810)))
        sleep(1)
        if not exists(Template(r"tpl1583560082190.png", record_pos=(0.391, 0.216), resolution=(1136, 640))):
            break
        EnableAuto()
        FindFleet()
        touch(Template(r"tpl1583563849777.png", record_pos=(-0.468, -0.022), resolution=(1136, 640)))
        sleep(1)

        print("每日斩首行动")
        Fight()
        
    Exit()
    
if exists(Template(r"tpl1583563699354.png", record_pos=(-0.002, 0.033), resolution=(1136, 640))):
    touch(Template(r"tpl1583563699354.png", record_pos=(-0.002, 0.033), resolution=(1136, 640)))
    sleep(1)
    touch(Template(r"tpl1583563699354.png", record_pos=(-0.002, 0.033), resolution=(1136, 640)))
    sleep(1)
    if exists(Template(r"tpl1583565220994.png", record_pos=(-0.145, -0.126), resolution=(1440, 810))):
        zhanshou()
# 海域突进
if exists(Template(r"tpl1583636039357.png", record_pos=(-0.213, 0.035), resolution=(1440, 810))):
    touch(Template(r"tpl1583636039357.png", record_pos=(-0.213, 0.035), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1583636062054.png", record_pos=(-0.004, 0.05), resolution=(1440, 810)))
    sleep(1)
    zhanshou=3
    while zhanshou > 0:
        zhanshou=zhanshou-1
        touch(Template(r"tpl1583636081368.png", record_pos=(-0.142, -0.125), resolution=(1440, 810)))
        sleep(1)
        if not exists(Template(r"tpl1583560082190.png", record_pos=(0.391, 0.216), resolution=(1136, 640))):
            Exit()
            break
        EnableAuto()
        FindFleet()
        touch(Template(r"tpl1583563849777.png", record_pos=(-0.468, -0.022), resolution=(1136, 640)))
        sleep(1)

        print("每日海域突进")
        Fight()