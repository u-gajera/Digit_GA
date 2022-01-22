#!/usr/bin/env python
# coding: utf-8
# Owner : Uday Gajera


import numpy as np
import random
import os

class StructureTextWriter:
    
    def __init__(self, struture_array):
        self.struture_array      = struture_array
        self.struture_text       = ''
        self.samples             = []
        self.all_squares_xposition = np.arange(-1800e-9, 1850e-9, 400e-9)
        self.all_squares_yposition = np.arange(-1800e-9, 1850e-9, 400e-9)
        self.position_1Darray      = np.zeros(len(self.all_squares_xposition)*len(self.all_squares_yposition))
        self.position_2Darray    = struture_array.copy()
        
        
    def indexing_the_squares(self):
        for ii, value in enumerate(self.struture_array):
            if value == 1:
                temp = "{:02d}".format(ii)
                x_cord, y_cord = int(temp[0]),int(temp[1])
                
                
    def binary_to_array(self):
        return (np.where(self.struture_array == 1)[0])
    
    
    def position1D_to_position2D(self):
        self.position_2Darray = self.struture_array.reshape(len(self.all_squares_xposition),
                                                          len(self.all_squares_yposition))

        
    def square_selection(self):
        self.position1D_to_position2D()
        position_1Darray = np.zeros(len(self.all_squares_xposition)*len(self.all_squares_yposition))
        samples = []

        temp = 0
        for ii, xvalues in enumerate(self.position_2Darray):
            for jj, yvalues in enumerate(xvalues):
                if yvalues == 1:
                    x_cord, y_cord = int(ii),int(jj)
                    self.struture_text = self.struture_text+('tss{} := ts.transl({},{},0) \n'.format(temp, 
                                                                 round(self.all_squares_xposition[x_cord], 10), 
                                                                 round(self.all_squares_yposition[y_cord], 10)))
                temp += 1
            
    
    def square_removel(self):
        self.square_selection()
        square_possition_array = self.binary_to_array()
        removed_sqrs = ''
        for jj in square_possition_array:
            removed_sqrs = removed_sqrs+'.sub'+'(tss{})'.format(jj)

        self.struture_text   = self.struture_text+'decomplex := full_structure' +removed_sqrs + '\n'

'''
#Example
testArray = np.zeros(400)
testNumbers = [0,19,399]
testArray[testNumbers] = 1


struture_text = StructureTextWriter(struture_array=testArray)
struture_text.square_removel()

f = open('struture_text_test.txt','w')
f.write(struture_text.struture_text)
f.close()

struture_text.struture_text
'''
