#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 18:39:20 2017

@author: joshuastuve
"""

import config
from wakeonlan import wol

''' Needs to return message for user '''
def WakeUpComputer():
    try:
        wol.send_magic_packet(config.BlackBeauty)
        return( config.name + ", I have awoken " + config.CompName + ".")
    except:
        return( config.name + ", there was an issue processing WoL.. Sorry.")
