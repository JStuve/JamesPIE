#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 18:39:20 2017

@author: joshuastuve
"""

from wakeonlan import wol

def WakeUpComputer(macAddy):
    print("Waking up computer...")
    wol.send_magic_packet(macAddy)
