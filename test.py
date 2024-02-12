# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 07:59:47 2024

@author: Ughon
"""

kigry = open("KIGRY.csv", "r")
print("Name of file: ", kigry.name)
print("closed or not: ", kigry.closed)
print("opening mode: ", kigry.mode)
kigry.close()
print("closed or not: : ", kigry.closed)