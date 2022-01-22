#!/usr/bin/env python
# coding: utf-8
# Owner : Uday Gajera

import numpy as np
import random
import os

class Frequncies_writer:
    def __init__(self, digit, Frequncies = [2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]):
        self.digit             = digit
        self._Digitsarraylist  = []
        self.Frequncies        = Frequncies
        self.digit_freuncy_array= []
        self.frequncy_string   = ''
        self.mask_string       = ''
        
        if len(self.Frequncies) != 7:
            print('ERROR:Leanth of frequncies is not sufficent')
        
    def stored_digits(self):
        L0 = [0,0,0,1,0,0,0]
        L1 = [1,1,0,1,1,0,1]
        L2 = [0,0,1,0,1,0,0]
        L3 = [0,1,0,0,1,0,0]
        L4 = [1,1,0,0,0,0,1]
        L5 = [0,1,0,0,0,1,0]
        L6 = [0,0,0,0,0,1,0]
        L7 = [1,1,0,1,1,0,0]
        L8 = [0,0,0,0,0,0,0]
        L9 = [0,1,0,0,0,0,0]
        return self._Digitsarraylist.append([L0,L1,L2,L3,L4,L5,L6,L7,L8,L9])
    
    def select_digit(self):
        self.stored_digits()
        return self._Digitsarraylist[0][self.digit]

    def write_frequncies(self):
        digit_array = self.select_digit()
        for ii, value in enumerate(digit_array):
            if value == 1:
                self.frequncy_string=self.frequncy_string+('f{} := {}e+9 \n'.format(ii, self.Frequncies[ii]))
                self.mask_string    =self.mask_string+('B_ext.add(mask{}, B_exc*sin(2*pi*f{}*(t-T_loc))) \n'.format(ii,ii))
       
'''
#Example:
frequncy_writer = Frequncies_writer(digit=1)
frequncy_writer.frequncy_string
frequncy_writer.mask_string
'''