# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:41:50 2017

@author: stuve
"""

import string
import config
from WoL import WakeUpComputer

def getTask(msg):
    msg = preprocessMsg(msg)
    lenMsg = len(msg.split())
    curPerc = 0.0
    curTask = ""
    for task, wordList in tasks.items():
        wordsFoundInTask = 0
        for word in wordList:
            for w in msg.split():
                if( w == word):
                    wordsFoundInTask = wordsFoundInTask + 1
        perc = wordsFoundInTask/lenMsg
        
        if(curPerc == 0.0):
            curPerc = perc
            curTask = task
        elif(curPerc < perc):
            curPerc = perc
            curTask = task
    return process[curTask]()
    
    
''' Needs to return message for user '''
def DNE():
    return(config.name + ", I cannot process that task.")


def preprocessMsg(s):
    
    excludePunc = set(string.punctuation)
    s = ''.join(ch for ch in s if ch not in excludePunc)
    s = s.lower()
    
    for word in ignoreWords:
        s = s.replace(word, "")
    return s


ignoreWords = ['james', 'hey', 'hello', 'hi']

tasks = {
        'WoL' : ['turn','on','computer','wake', 'up'],
        'CrateOpen': ['open', 'crate', 'up'],
        'PowerDown': ['power', 'down', 'turn', 'off'],
        'Destory': ['this', 'is', 'a', 'computer', 'on', 'test']
        }

process = {'WoL': WakeUpComputer,
               'CrateOpen': DNE,
               'PowerDown': DNE,
               'Destory': DNE}