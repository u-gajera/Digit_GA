#!/usr/bin/env python
# coding: utf-8
# Owner : Uday Gajera
# Date  : 26/12/2021


import numpy as np
import random
import matplotlib.pylab as plt
import os
#get_ipython().run_line_magic('matplotlib', 'inline')


main_path = 'C:\\Users\\Uday Aalto Account\\OneDrive - Aalto University\\Documents\\mumax\\magnonic_device'
analysis_path = '\Algorithms'
os.chdir(main_path+analysis_path)


class IntensityCalculation:
    def __init__(self, filename, xcellrange, ycellrange, zcellrange):
        self.filename   = filename
        self.xcellrange = xcellrange
        self.ycellrange = ycellrange
        self.zcellrange = zcellrange
        
    def readfiles(self):
        with open(self.filename ,'r') as file:
            lines = file.read()
        lines  = lines.split('\n')
        xcell  = int(lines[20].split(' ')[2])
        ycell  = int(lines[21].split(' ')[2])
        zcell  = int(lines[22].split(' ')[2])
        xstepsize = float(lines[23].split(' ')[2])
        ystepsize = float(lines[24].split(' ')[2])
        zstepsize = float(lines[25].split(' ')[2])
        lines = lines[28:-3]
        tempx = np.array(range(0,xcell))
        tempy = np.array(range(0,ycell))
        tempz = np.array(range(0,zcell))
        return xcell, ycell, zcell, xstepsize, ystepsize                ,zstepsize, tempx, tempy, tempz, lines
    
    def getTotalM(self):
        xcell, ycell, zcell, xstepsize, ystepsize, zstepsize         ,tempx, tempy, tempz, lines = self.readfiles()
        mx, my, mz = [],[],[]
        for ii in lines:
            A = ii.split(' ')
            mx.append(float(A[0]))
            my.append(float(A[1]))
            mz.append(float(A[2]))

        mx = np.array(mx)
        my = np.array(my)
        mz = np.array(mz)
        return mx, my, mz, xcell, ycell, zcell
        
    def reshapeM(self):
        mx, my, mz, xcell, ycell, zcell = self.getTotalM()
        mx = np.reshape(mx,[xcell,ycell,zcell])
        my = np.reshape(my,[xcell,ycell,zcell])
        mz = np.reshape(mz,[xcell,ycell,zcell])
        return mx, my, mz
    
    def getSelectedM(self):
        mx, my, mz = self.reshapeM()
        selected_mx = mx[self.xcellrange,:,:][:,self.ycellrange,:][:,:,self.zcellrange]
        selected_my = my[self.xcellrange,:,:][:,self.ycellrange,:][:,:,self.zcellrange]
        selected_mz = mz[self.xcellrange,:,:][:,self.ycellrange,:][:,:,self.zcellrange]
        return selected_mx, selected_my, selected_mz



def calculate_intensities_all_arms(mumaxOutputFile):
    intensities = []
    xcellranges = [range(328,478),range(328,478),range(328,478),
                   range(302,303),range(253,254),range(203,204),
                   range(28 ,178),range(28 ,178),range(28 ,178)]
    
    ycellranges = [range(203,204),range(253,254),range(302,303),
                   range(328,478),range(328,478),range(328,478),
                   range(302,303),range(253,254),range(203,204)]
    
    for ii in range(9):
        obj = IntensityCalculation(filename = mumaxOutputFile, 
                                   xcellrange=xcellranges[ii], 
                                   ycellrange=ycellranges[ii], 
                                   zcellrange=range(0,1))
        selected_mx, selected_my, selected_mz = obj.getSelectedM()
        intensities.append(np.average(np.sqrt(selected_mx**2+selected_my**2)))
    return intensities

'''def calculate_intensities_all_arms(mumaxOutputFile):
    intensities = []
    xcellranges = [range(655,955),range(655,955),range(655,955),
                   range(605,607),range(505,507),range(405,407),
                   range(55 ,355),range(55 ,355),range(55 ,355)]
    
    ycellranges = [range(405,407),range(505,507),range(605,607),
                   range(655,955),range(655,955),range(655,955),
                   range(605,607),range(505,507),range(405,407)]
    
    for ii in range(9):
        obj = IntensityCalculation(filename = mumaxOutputFile, 
                                   xcellrange=xcellranges[ii], 
                                   ycellrange=ycellranges[ii], 
                                   zcellrange=range(0,1))
        selected_mx, selected_my, selected_mz = obj.getSelectedM()
        intensities.append(np.average(np.sqrt(selected_mx**2+selected_my**2)))
    return intensities'''

'''
#Example
obj1 = IntensityCalculation(filename='Digit_NN_allsides.out/m000005.ovf', 
                           xcellrange=range(655,955), 
                           ycellrange=range(405,407), 
                           zcellrange=range(0,1))


selected_mx, selected_my, selected_mz = obj1.getSelectedM()
np.average(np.sqrt(selected_mx**2+selected_my**2))



intensities = calculate_intensities_all_arms()

'''