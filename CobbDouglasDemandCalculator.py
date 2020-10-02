# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#These are the variable we will use for both X* and Y*
Alpha = int(input("Enter Alpha for function (X^A)(Y^B): "))
Beta = int(input("Enter Beta for function (X^A)(Y^B): "))
Px = int(input("Enter Px: "))
Py = int(input("Enter Py: "))
M = int(input ("Enter Budget or M: "))
LLD = Alpha + Beta

#These are X* specific
Xleft = Alpha / LLD
Xright = M / Px
Xstar = Xleft * Xright

#These are Y* specific variables
Yleft = Beta / LLD
Yright = M / Py
Ystar = Yleft * Yright
print ("X*= ", Xstar)
print ("Y*= ", Ystar)
input ('press ENTER to exit')