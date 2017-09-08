#!/usr/bin/pyton
#-*- coding:utf-8 -*-

import sys
import shelve

if len(sys.argv) < 2:
    print "输入参数错误"
    sys.exit(-1)

action = sys.argv[1]

my_shelve = shelve.open("shelve_test")

if action == "save" and len(sys.argv) < 3:
    print "save need key"
    my_shelve.close()
    sys.exit(-1)
elif action == "save":
    param = sys.argv[2]
    my_shelve[param] = "default"

elif action == "list":
    for key in list(my_shelve.keys()):
        print key.center(20," ")," : " , my_shelve[key].center(20," ")

my_shelve.close()
