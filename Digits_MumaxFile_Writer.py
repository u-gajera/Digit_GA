#!/usr/bin/env python
# coding: utf-8
# Owner : Uday Gajera

import numpy as np
import random
import os

class MumaxFileWriter:
    
    def __init__(self, filename, structre_text, frequncy_text, writefilename):
        self.filename   = filename
        self.script_text = ''
        self.structre_text = structre_text
        self.frequncy_text = frequncy_text
        self.writefilename = writefilename
        
    
    def mumax_script_read(self):
        with open(self.filename,'r') as file:
            lines = file.read()
        lines = lines.split('\n')
        return lines
                    
    def script_writing(self):
        lines = self.mumax_script_read()
        for ii in range(lines.index('//input from the python')+1):
            self.script_text= self.script_text+(lines[ii]+'\n')
            
        self.script_text = self.script_text + self.structre_text

        for jj in range(lines.index('//end input from the python'),
                        lines.index('//input frequncies from the python')):
            self.script_text = self.script_text+(lines[jj]+'\n')
            
        self.script_text = self.script_text + self.frequncy_text
        
        for kk in range(lines.index('//end frequncies from the python'),
                        len(lines)):
            self.script_text = self.script_text+(lines[kk]+'\n')
            
    def file_writing(self):
        self.script_writing()
        with open(self.writefilename, 'w') as file:
            file.write(self.script_text)
        file.close()
