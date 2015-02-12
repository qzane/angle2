#coding:utf-8
from math import tan,atan,pi,exp,log
import random

import pickle

def main(k1,k2):
    """输入值为斜率"""
    return abs(atan(k1)-atan(k2))*180/pi

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def mkds(n = 10000):
    """train set :[[sigmoid(k1),sigmoid(k2),angle/180],[]...]"""
    set = []
    for i in xrange(n):
        ang1 = random.random()*180 - 90
        k1 = tan(ang1)
        ang2 = random.random()*180 - 90
        k2 = tan(ang2)
        set.append([k1,k2,abs(ang1-ang2)/180])
    return set
    
    