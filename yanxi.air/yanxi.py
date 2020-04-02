# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
#演习
print("演习开始")
#touch(Template(r"tpl1583557219783.png", record_pos=(0.339, -0.028), resolution=(1136, 640)))
#sleep(1)
#touch(Template(r"tpl1583557243109.png", record_pos=(0.417, 0.244), resolution=(1136, 640)))
#sleep(1)
n=10
while n > 0:
    n=n-1
    touch(Template(r"tpl1583557268981.png", record_pos=(-0.369, -0.094), resolution=(1136, 640)))
    sleep(1)
    if exists(Template(r"tpl1583557278619.png", record_pos=(0.003, 0.162), resolution=(1136, 640))):
        touch(Template(r"tpl1583557278619.png", record_pos=(0.003, 0.162), resolution=(1136, 640)))
        sleep(1)
        touch(Template(r"tpl1583557291557.png", record_pos=(0.389, 0.216), resolution=(1136, 640)))
        print("第一次演习")
        wait(Template(r"tpl1583557341072.png", record_pos=(-0.309, 0.212), resolution=(1136, 640)),300,10)
        touch(Template(r"tpl1583557341072.png", record_pos=(-0.309, 0.212), resolution=(1136, 640)))
        sleep(1)
        touch(Template(r"tpl1583557357276.png", record_pos=(-0.003, 0.096), resolution=(1136, 640)))
        sleep(1)
        touch(Template(r"tpl1583557371231.png", record_pos=(0.347, 0.233), resolution=(1136, 640)))
        sleep(1)
        if exists(Template(r"tpl1584459203325.png", record_pos=(-0.009, 0.197), resolution=(1440, 810))):
            touch(Template(r"tpl1584459203325.png", record_pos=(-0.009, 0.197), resolution=(1440, 810)))
            sleep(1)
