#coding:utf-8
from math import atan,pi

def main(d1,d2):
    """输入值为斜率"""
    return abs(atan(d1)-atan(d2))*180/pi

    