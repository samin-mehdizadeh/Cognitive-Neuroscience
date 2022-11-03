#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on Wed Mar  9 22:06:36 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'hndns': '', 'eye': '', 'sex': '', 'age': '', 'edu': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mac/Desktop/CA1_scripts/Task1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "trial"
trialClock = core.Clock()
hello = visual.TextStim(win=win, name='hello',
    text='سلام :)\nدر این تسک چندین تصویر به شما نشان داده می شود\nبرای هر تصویر از شما خواسته می شود که جنسیت فرد\nمشاهده شده را با فشردن کلید های مشخص اعلام کنید.\n',
    font='B Nazanin',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "round1"
round1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Ins_R"
Ins_RClock = core.Clock()
ins_r = visual.ImageStim(
    win=win,
    name='ins_r', 
    image='KbRight.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_r = keyboard.Keyboard()

# Initialize components for Routine "fix_R"
fix_RClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.05,0.05),
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_R"
Test_RClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_r = keyboard.Keyboard()

# Initialize components for Routine "Ins_L"
Ins_LClock = core.Clock()
ins_l = visual.ImageStim(
    win=win,
    name='ins_l', 
    image='KbLeft.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_l = keyboard.Keyboard()

# Initialize components for Routine "fix_L"
fix_LClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_L"
Test_LClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_l = keyboard.Keyboard()

# Initialize components for Routine "round2"
round2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Ins_L"
Ins_LClock = core.Clock()
ins_l = visual.ImageStim(
    win=win,
    name='ins_l', 
    image='KbLeft.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_l = keyboard.Keyboard()

# Initialize components for Routine "fix_L"
fix_LClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_L"
Test_LClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_l = keyboard.Keyboard()

# Initialize components for Routine "Ins_R"
Ins_RClock = core.Clock()
ins_r = visual.ImageStim(
    win=win,
    name='ins_r', 
    image='KbRight.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_r = keyboard.Keyboard()

# Initialize components for Routine "fix_R"
fix_RClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.05,0.05),
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_R"
Test_RClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_r = keyboard.Keyboard()

# Initialize components for Routine "round3"
round3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Ins_L"
Ins_LClock = core.Clock()
ins_l = visual.ImageStim(
    win=win,
    name='ins_l', 
    image='KbLeft.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_l = keyboard.Keyboard()

# Initialize components for Routine "fix_L"
fix_LClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_L"
Test_LClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_l = keyboard.Keyboard()

# Initialize components for Routine "Ins_R"
Ins_RClock = core.Clock()
ins_r = visual.ImageStim(
    win=win,
    name='ins_r', 
    image='KbRight.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_r = keyboard.Keyboard()

# Initialize components for Routine "fix_R"
fix_RClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.05,0.05),
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_R"
Test_RClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_r = keyboard.Keyboard()

# Initialize components for Routine "round4"
round4Clock = core.Clock()

# Initialize components for Routine "Ins_R"
Ins_RClock = core.Clock()
ins_r = visual.ImageStim(
    win=win,
    name='ins_r', 
    image='KbRight.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_r = keyboard.Keyboard()

# Initialize components for Routine "fix_R"
fix_RClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.05,0.05),
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_R"
Test_RClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_r = keyboard.Keyboard()

# Initialize components for Routine "Ins_L"
Ins_LClock = core.Clock()
ins_l = visual.ImageStim(
    win=win,
    name='ins_l', 
    image='KbLeft.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_ins_l = keyboard.Keyboard()

# Initialize components for Routine "fix_L"
fix_LClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Test_L"
Test_LClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_l = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [hello]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hello* updates
    if hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hello.frameNStart = frameN  # exact frame index
        hello.tStart = t  # local t and not account for scr refresh
        hello.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hello, 'tStartRefresh')  # time at next scr refresh
        hello.setAutoDraw(True)
    if hello.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > hello.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            hello.tStop = t  # not accounting for scr refresh
            hello.frameNStop = frameN  # exact frame index
            win.timeOnFlip(hello, 'tStopRefresh')  # time at next scr refresh
            hello.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('hello.started', hello.tStartRefresh)
thisExp.addData('hello.stopped', hello.tStopRefresh)

# ------Prepare to start Routine "round1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
round1Components = [text]
for thisComponent in round1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
round1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "round1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = round1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=round1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "round1"-------
for thisComponent in round1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "Ins_R"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_r.keys = []
key_ins_r.rt = []
_key_ins_r_allKeys = []
# keep track of which components have finished
Ins_RComponents = [ins_r, key_ins_r]
for thisComponent in Ins_RComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_R"-------
while continueRoutine:
    # get current time
    t = Ins_RClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_RClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_r* updates
    if ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_r.frameNStart = frameN  # exact frame index
        ins_r.tStart = t  # local t and not account for scr refresh
        ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_r, 'tStartRefresh')  # time at next scr refresh
        ins_r.setAutoDraw(True)
    
    # *key_ins_r* updates
    waitOnFlip = False
    if key_ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_r.frameNStart = frameN  # exact frame index
        key_ins_r.tStart = t  # local t and not account for scr refresh
        key_ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_r, 'tStartRefresh')  # time at next scr refresh
        key_ins_r.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_r.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_r.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_r.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_r_allKeys.extend(theseKeys)
        if len(_key_ins_r_allKeys):
            key_ins_r.keys = _key_ins_r_allKeys[-1].name  # just the last key pressed
            key_ins_r.rt = _key_ins_r_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_RComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_R"-------
for thisComponent in Ins_RComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_r.started', ins_r.tStartRefresh)
thisExp.addData('ins_r.stopped', ins_r.tStopRefresh)
# check responses
if key_ins_r.keys in ['', [], None]:  # No response was made
    key_ins_r.keys = None
thisExp.addData('key_ins_r.keys',key_ins_r.keys)
if key_ins_r.keys != None:  # we had a response
    thisExp.addData('key_ins_r.rt', key_ins_r.rt)
thisExp.addData('key_ins_r.started', key_ins_r.tStartRefresh)
thisExp.addData('key_ins_r.stopped', key_ins_r.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_R" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
R1 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='R1')
thisExp.addLoop(R1)  # add the loop to the experiment
thisR1 = R1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisR1.rgb)
if thisR1 != None:
    for paramName in thisR1:
        exec('{} = thisR1[paramName]'.format(paramName))

for thisR1 in R1:
    currentLoop = R1
    # abbreviate parameter names if possible (e.g. rgb = thisR1.rgb)
    if thisR1 != None:
        for paramName in thisR1:
            exec('{} = thisR1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_R"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_RComponents = [polygon]
    for thisComponent in fix_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_R"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_R"-------
    for thisComponent in fix_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R1.addData('polygon.started', polygon.tStartRefresh)
    R1.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "Test_R"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setPos((r*1.45*cos((pos-2)%6*(pi/3)),r*1.45*sin((pos-2)%6*(pi/3))))
    image.setSize((size*1.45,size*1.45))
    image.setImage(stim)
    key_resp_r.keys = []
    key_resp_r.rt = []
    _key_resp_r_allKeys = []
    # keep track of which components have finished
    Test_RComponents = [image, key_resp_r]
    for thisComponent in Test_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_R"-------
    while continueRoutine:
        # get current time
        t = Test_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_r* updates
        waitOnFlip = False
        if key_resp_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_r.frameNStart = frameN  # exact frame index
            key_resp_r.tStart = t  # local t and not account for scr refresh
            key_resp_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_r, 'tStartRefresh')  # time at next scr refresh
            key_resp_r.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_r.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_r.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_r.getKeys(keyList=['p','o'], waitRelease=False)
            _key_resp_r_allKeys.extend(theseKeys)
            if len(_key_resp_r_allKeys):
                key_resp_r.keys = _key_resp_r_allKeys[-1].name  # just the last key pressed
                key_resp_r.rt = _key_resp_r_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_R"-------
    for thisComponent in Test_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R1.addData('image.started', image.tStartRefresh)
    R1.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_r.keys in ['', [], None]:  # No response was made
        key_resp_r.keys = None
    R1.addData('key_resp_r.keys',key_resp_r.keys)
    if key_resp_r.keys != None:  # we had a response
        R1.addData('key_resp_r.rt', key_resp_r.rt)
    R1.addData('key_resp_r.started', key_resp_r.tStartRefresh)
    R1.addData('key_resp_r.stopped', key_resp_r.tStopRefresh)
    # the Routine "Test_R" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'R1'


# ------Prepare to start Routine "Ins_L"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_l.keys = []
key_ins_l.rt = []
_key_ins_l_allKeys = []
# keep track of which components have finished
Ins_LComponents = [ins_l, key_ins_l]
for thisComponent in Ins_LComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_L"-------
while continueRoutine:
    # get current time
    t = Ins_LClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_LClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_l* updates
    if ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_l.frameNStart = frameN  # exact frame index
        ins_l.tStart = t  # local t and not account for scr refresh
        ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_l, 'tStartRefresh')  # time at next scr refresh
        ins_l.setAutoDraw(True)
    
    # *key_ins_l* updates
    waitOnFlip = False
    if key_ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_l.frameNStart = frameN  # exact frame index
        key_ins_l.tStart = t  # local t and not account for scr refresh
        key_ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_l, 'tStartRefresh')  # time at next scr refresh
        key_ins_l.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_l.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_l.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_l.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_l_allKeys.extend(theseKeys)
        if len(_key_ins_l_allKeys):
            key_ins_l.keys = _key_ins_l_allKeys[-1].name  # just the last key pressed
            key_ins_l.rt = _key_ins_l_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_LComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_L"-------
for thisComponent in Ins_LComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_l.started', ins_l.tStartRefresh)
thisExp.addData('ins_l.stopped', ins_l.tStopRefresh)
# check responses
if key_ins_l.keys in ['', [], None]:  # No response was made
    key_ins_l.keys = None
thisExp.addData('key_ins_l.keys',key_ins_l.keys)
if key_ins_l.keys != None:  # we had a response
    thisExp.addData('key_ins_l.rt', key_ins_l.rt)
thisExp.addData('key_ins_l.started', key_ins_l.tStartRefresh)
thisExp.addData('key_ins_l.stopped', key_ins_l.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_L" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
L1 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='L1')
thisExp.addLoop(L1)  # add the loop to the experiment
thisL1 = L1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisL1.rgb)
if thisL1 != None:
    for paramName in thisL1:
        exec('{} = thisL1[paramName]'.format(paramName))

for thisL1 in L1:
    currentLoop = L1
    # abbreviate parameter names if possible (e.g. rgb = thisL1.rgb)
    if thisL1 != None:
        for paramName in thisL1:
            exec('{} = thisL1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_L"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_LComponents = [polygon_2]
    for thisComponent in fix_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_L"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_L"-------
    for thisComponent in fix_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L1.addData('polygon_2.started', polygon_2.tStartRefresh)
    L1.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    
    # ------Prepare to start Routine "Test_L"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_2.setPos((r*4/2.8*cos((pos-2)%6*(pi/3)),r*4/2.8*sin((pos-2)%6*(pi/3))))
    image_2.setSize((size*4/2.8,size*4/2.8))
    image_2.setImage(stim)
    key_resp_l.keys = []
    key_resp_l.rt = []
    _key_resp_l_allKeys = []
    # keep track of which components have finished
    Test_LComponents = [image_2, key_resp_l]
    for thisComponent in Test_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_L"-------
    while continueRoutine:
        # get current time
        t = Test_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *key_resp_l* updates
        waitOnFlip = False
        if key_resp_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_l.frameNStart = frameN  # exact frame index
            key_resp_l.tStart = t  # local t and not account for scr refresh
            key_resp_l.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_l, 'tStartRefresh')  # time at next scr refresh
            key_resp_l.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_l.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_l.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_l.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_l_allKeys.extend(theseKeys)
            if len(_key_resp_l_allKeys):
                key_resp_l.keys = _key_resp_l_allKeys[-1].name  # just the last key pressed
                key_resp_l.rt = _key_resp_l_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_L"-------
    for thisComponent in Test_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L1.addData('image_2.started', image_2.tStartRefresh)
    L1.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_l.keys in ['', [], None]:  # No response was made
        key_resp_l.keys = None
    L1.addData('key_resp_l.keys',key_resp_l.keys)
    if key_resp_l.keys != None:  # we had a response
        L1.addData('key_resp_l.rt', key_resp_l.rt)
    L1.addData('key_resp_l.started', key_resp_l.tStartRefresh)
    L1.addData('key_resp_l.stopped', key_resp_l.tStopRefresh)
    # the Routine "Test_L" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'L1'


# ------Prepare to start Routine "round2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
round2Components = [text_2]
for thisComponent in round2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
round2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "round2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = round2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=round2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "round2"-------
for thisComponent in round2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "Ins_L"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_l.keys = []
key_ins_l.rt = []
_key_ins_l_allKeys = []
# keep track of which components have finished
Ins_LComponents = [ins_l, key_ins_l]
for thisComponent in Ins_LComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_L"-------
while continueRoutine:
    # get current time
    t = Ins_LClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_LClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_l* updates
    if ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_l.frameNStart = frameN  # exact frame index
        ins_l.tStart = t  # local t and not account for scr refresh
        ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_l, 'tStartRefresh')  # time at next scr refresh
        ins_l.setAutoDraw(True)
    
    # *key_ins_l* updates
    waitOnFlip = False
    if key_ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_l.frameNStart = frameN  # exact frame index
        key_ins_l.tStart = t  # local t and not account for scr refresh
        key_ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_l, 'tStartRefresh')  # time at next scr refresh
        key_ins_l.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_l.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_l.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_l.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_l_allKeys.extend(theseKeys)
        if len(_key_ins_l_allKeys):
            key_ins_l.keys = _key_ins_l_allKeys[-1].name  # just the last key pressed
            key_ins_l.rt = _key_ins_l_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_LComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_L"-------
for thisComponent in Ins_LComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_l.started', ins_l.tStartRefresh)
thisExp.addData('ins_l.stopped', ins_l.tStopRefresh)
# check responses
if key_ins_l.keys in ['', [], None]:  # No response was made
    key_ins_l.keys = None
thisExp.addData('key_ins_l.keys',key_ins_l.keys)
if key_ins_l.keys != None:  # we had a response
    thisExp.addData('key_ins_l.rt', key_ins_l.rt)
thisExp.addData('key_ins_l.started', key_ins_l.tStartRefresh)
thisExp.addData('key_ins_l.stopped', key_ins_l.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_L" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
L2 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='L2')
thisExp.addLoop(L2)  # add the loop to the experiment
thisL2 = L2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisL2.rgb)
if thisL2 != None:
    for paramName in thisL2:
        exec('{} = thisL2[paramName]'.format(paramName))

for thisL2 in L2:
    currentLoop = L2
    # abbreviate parameter names if possible (e.g. rgb = thisL2.rgb)
    if thisL2 != None:
        for paramName in thisL2:
            exec('{} = thisL2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_L"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_LComponents = [polygon_2]
    for thisComponent in fix_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_L"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_L"-------
    for thisComponent in fix_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L2.addData('polygon_2.started', polygon_2.tStartRefresh)
    L2.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    
    # ------Prepare to start Routine "Test_L"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_2.setPos((r*4/2.8*cos((pos-2)%6*(pi/3)),r*4/2.8*sin((pos-2)%6*(pi/3))))
    image_2.setSize((size*4/2.8,size*4/2.8))
    image_2.setImage(stim)
    key_resp_l.keys = []
    key_resp_l.rt = []
    _key_resp_l_allKeys = []
    # keep track of which components have finished
    Test_LComponents = [image_2, key_resp_l]
    for thisComponent in Test_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_L"-------
    while continueRoutine:
        # get current time
        t = Test_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *key_resp_l* updates
        waitOnFlip = False
        if key_resp_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_l.frameNStart = frameN  # exact frame index
            key_resp_l.tStart = t  # local t and not account for scr refresh
            key_resp_l.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_l, 'tStartRefresh')  # time at next scr refresh
            key_resp_l.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_l.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_l.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_l.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_l_allKeys.extend(theseKeys)
            if len(_key_resp_l_allKeys):
                key_resp_l.keys = _key_resp_l_allKeys[-1].name  # just the last key pressed
                key_resp_l.rt = _key_resp_l_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_L"-------
    for thisComponent in Test_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L2.addData('image_2.started', image_2.tStartRefresh)
    L2.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_l.keys in ['', [], None]:  # No response was made
        key_resp_l.keys = None
    L2.addData('key_resp_l.keys',key_resp_l.keys)
    if key_resp_l.keys != None:  # we had a response
        L2.addData('key_resp_l.rt', key_resp_l.rt)
    L2.addData('key_resp_l.started', key_resp_l.tStartRefresh)
    L2.addData('key_resp_l.stopped', key_resp_l.tStopRefresh)
    # the Routine "Test_L" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'L2'


# ------Prepare to start Routine "Ins_R"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_r.keys = []
key_ins_r.rt = []
_key_ins_r_allKeys = []
# keep track of which components have finished
Ins_RComponents = [ins_r, key_ins_r]
for thisComponent in Ins_RComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_R"-------
while continueRoutine:
    # get current time
    t = Ins_RClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_RClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_r* updates
    if ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_r.frameNStart = frameN  # exact frame index
        ins_r.tStart = t  # local t and not account for scr refresh
        ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_r, 'tStartRefresh')  # time at next scr refresh
        ins_r.setAutoDraw(True)
    
    # *key_ins_r* updates
    waitOnFlip = False
    if key_ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_r.frameNStart = frameN  # exact frame index
        key_ins_r.tStart = t  # local t and not account for scr refresh
        key_ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_r, 'tStartRefresh')  # time at next scr refresh
        key_ins_r.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_r.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_r.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_r.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_r_allKeys.extend(theseKeys)
        if len(_key_ins_r_allKeys):
            key_ins_r.keys = _key_ins_r_allKeys[-1].name  # just the last key pressed
            key_ins_r.rt = _key_ins_r_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_RComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_R"-------
for thisComponent in Ins_RComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_r.started', ins_r.tStartRefresh)
thisExp.addData('ins_r.stopped', ins_r.tStopRefresh)
# check responses
if key_ins_r.keys in ['', [], None]:  # No response was made
    key_ins_r.keys = None
thisExp.addData('key_ins_r.keys',key_ins_r.keys)
if key_ins_r.keys != None:  # we had a response
    thisExp.addData('key_ins_r.rt', key_ins_r.rt)
thisExp.addData('key_ins_r.started', key_ins_r.tStartRefresh)
thisExp.addData('key_ins_r.stopped', key_ins_r.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_R" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
R2 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='R2')
thisExp.addLoop(R2)  # add the loop to the experiment
thisR2 = R2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisR2.rgb)
if thisR2 != None:
    for paramName in thisR2:
        exec('{} = thisR2[paramName]'.format(paramName))

for thisR2 in R2:
    currentLoop = R2
    # abbreviate parameter names if possible (e.g. rgb = thisR2.rgb)
    if thisR2 != None:
        for paramName in thisR2:
            exec('{} = thisR2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_R"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_RComponents = [polygon]
    for thisComponent in fix_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_R"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_R"-------
    for thisComponent in fix_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R2.addData('polygon.started', polygon.tStartRefresh)
    R2.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "Test_R"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setPos((r*1.45*cos((pos-2)%6*(pi/3)),r*1.45*sin((pos-2)%6*(pi/3))))
    image.setSize((size*1.45,size*1.45))
    image.setImage(stim)
    key_resp_r.keys = []
    key_resp_r.rt = []
    _key_resp_r_allKeys = []
    # keep track of which components have finished
    Test_RComponents = [image, key_resp_r]
    for thisComponent in Test_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_R"-------
    while continueRoutine:
        # get current time
        t = Test_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_r* updates
        waitOnFlip = False
        if key_resp_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_r.frameNStart = frameN  # exact frame index
            key_resp_r.tStart = t  # local t and not account for scr refresh
            key_resp_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_r, 'tStartRefresh')  # time at next scr refresh
            key_resp_r.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_r.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_r.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_r.getKeys(keyList=['p','o'], waitRelease=False)
            _key_resp_r_allKeys.extend(theseKeys)
            if len(_key_resp_r_allKeys):
                key_resp_r.keys = _key_resp_r_allKeys[-1].name  # just the last key pressed
                key_resp_r.rt = _key_resp_r_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_R"-------
    for thisComponent in Test_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R2.addData('image.started', image.tStartRefresh)
    R2.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_r.keys in ['', [], None]:  # No response was made
        key_resp_r.keys = None
    R2.addData('key_resp_r.keys',key_resp_r.keys)
    if key_resp_r.keys != None:  # we had a response
        R2.addData('key_resp_r.rt', key_resp_r.rt)
    R2.addData('key_resp_r.started', key_resp_r.tStartRefresh)
    R2.addData('key_resp_r.stopped', key_resp_r.tStopRefresh)
    # the Routine "Test_R" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'R2'


# ------Prepare to start Routine "round3"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
round3Components = [text_3]
for thisComponent in round3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
round3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "round3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = round3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=round3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "round3"-------
for thisComponent in round3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# ------Prepare to start Routine "Ins_L"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_l.keys = []
key_ins_l.rt = []
_key_ins_l_allKeys = []
# keep track of which components have finished
Ins_LComponents = [ins_l, key_ins_l]
for thisComponent in Ins_LComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_L"-------
while continueRoutine:
    # get current time
    t = Ins_LClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_LClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_l* updates
    if ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_l.frameNStart = frameN  # exact frame index
        ins_l.tStart = t  # local t and not account for scr refresh
        ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_l, 'tStartRefresh')  # time at next scr refresh
        ins_l.setAutoDraw(True)
    
    # *key_ins_l* updates
    waitOnFlip = False
    if key_ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_l.frameNStart = frameN  # exact frame index
        key_ins_l.tStart = t  # local t and not account for scr refresh
        key_ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_l, 'tStartRefresh')  # time at next scr refresh
        key_ins_l.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_l.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_l.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_l.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_l_allKeys.extend(theseKeys)
        if len(_key_ins_l_allKeys):
            key_ins_l.keys = _key_ins_l_allKeys[-1].name  # just the last key pressed
            key_ins_l.rt = _key_ins_l_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_LComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_L"-------
for thisComponent in Ins_LComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_l.started', ins_l.tStartRefresh)
thisExp.addData('ins_l.stopped', ins_l.tStopRefresh)
# check responses
if key_ins_l.keys in ['', [], None]:  # No response was made
    key_ins_l.keys = None
thisExp.addData('key_ins_l.keys',key_ins_l.keys)
if key_ins_l.keys != None:  # we had a response
    thisExp.addData('key_ins_l.rt', key_ins_l.rt)
thisExp.addData('key_ins_l.started', key_ins_l.tStartRefresh)
thisExp.addData('key_ins_l.stopped', key_ins_l.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_L" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
L3 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='L3')
thisExp.addLoop(L3)  # add the loop to the experiment
thisL3 = L3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisL3.rgb)
if thisL3 != None:
    for paramName in thisL3:
        exec('{} = thisL3[paramName]'.format(paramName))

for thisL3 in L3:
    currentLoop = L3
    # abbreviate parameter names if possible (e.g. rgb = thisL3.rgb)
    if thisL3 != None:
        for paramName in thisL3:
            exec('{} = thisL3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_L"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_LComponents = [polygon_2]
    for thisComponent in fix_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_L"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_L"-------
    for thisComponent in fix_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L3.addData('polygon_2.started', polygon_2.tStartRefresh)
    L3.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    
    # ------Prepare to start Routine "Test_L"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_2.setPos((r*4/2.8*cos((pos-2)%6*(pi/3)),r*4/2.8*sin((pos-2)%6*(pi/3))))
    image_2.setSize((size*4/2.8,size*4/2.8))
    image_2.setImage(stim)
    key_resp_l.keys = []
    key_resp_l.rt = []
    _key_resp_l_allKeys = []
    # keep track of which components have finished
    Test_LComponents = [image_2, key_resp_l]
    for thisComponent in Test_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_L"-------
    while continueRoutine:
        # get current time
        t = Test_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *key_resp_l* updates
        waitOnFlip = False
        if key_resp_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_l.frameNStart = frameN  # exact frame index
            key_resp_l.tStart = t  # local t and not account for scr refresh
            key_resp_l.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_l, 'tStartRefresh')  # time at next scr refresh
            key_resp_l.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_l.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_l.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_l.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_l_allKeys.extend(theseKeys)
            if len(_key_resp_l_allKeys):
                key_resp_l.keys = _key_resp_l_allKeys[-1].name  # just the last key pressed
                key_resp_l.rt = _key_resp_l_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_L"-------
    for thisComponent in Test_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L3.addData('image_2.started', image_2.tStartRefresh)
    L3.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_l.keys in ['', [], None]:  # No response was made
        key_resp_l.keys = None
    L3.addData('key_resp_l.keys',key_resp_l.keys)
    if key_resp_l.keys != None:  # we had a response
        L3.addData('key_resp_l.rt', key_resp_l.rt)
    L3.addData('key_resp_l.started', key_resp_l.tStartRefresh)
    L3.addData('key_resp_l.stopped', key_resp_l.tStopRefresh)
    # the Routine "Test_L" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'L3'


# ------Prepare to start Routine "Ins_R"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_r.keys = []
key_ins_r.rt = []
_key_ins_r_allKeys = []
# keep track of which components have finished
Ins_RComponents = [ins_r, key_ins_r]
for thisComponent in Ins_RComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_R"-------
while continueRoutine:
    # get current time
    t = Ins_RClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_RClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_r* updates
    if ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_r.frameNStart = frameN  # exact frame index
        ins_r.tStart = t  # local t and not account for scr refresh
        ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_r, 'tStartRefresh')  # time at next scr refresh
        ins_r.setAutoDraw(True)
    
    # *key_ins_r* updates
    waitOnFlip = False
    if key_ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_r.frameNStart = frameN  # exact frame index
        key_ins_r.tStart = t  # local t and not account for scr refresh
        key_ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_r, 'tStartRefresh')  # time at next scr refresh
        key_ins_r.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_r.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_r.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_r.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_r_allKeys.extend(theseKeys)
        if len(_key_ins_r_allKeys):
            key_ins_r.keys = _key_ins_r_allKeys[-1].name  # just the last key pressed
            key_ins_r.rt = _key_ins_r_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_RComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_R"-------
for thisComponent in Ins_RComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_r.started', ins_r.tStartRefresh)
thisExp.addData('ins_r.stopped', ins_r.tStopRefresh)
# check responses
if key_ins_r.keys in ['', [], None]:  # No response was made
    key_ins_r.keys = None
thisExp.addData('key_ins_r.keys',key_ins_r.keys)
if key_ins_r.keys != None:  # we had a response
    thisExp.addData('key_ins_r.rt', key_ins_r.rt)
thisExp.addData('key_ins_r.started', key_ins_r.tStartRefresh)
thisExp.addData('key_ins_r.stopped', key_ins_r.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_R" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
R3 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='R3')
thisExp.addLoop(R3)  # add the loop to the experiment
thisR3 = R3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisR3.rgb)
if thisR3 != None:
    for paramName in thisR3:
        exec('{} = thisR3[paramName]'.format(paramName))

for thisR3 in R3:
    currentLoop = R3
    # abbreviate parameter names if possible (e.g. rgb = thisR3.rgb)
    if thisR3 != None:
        for paramName in thisR3:
            exec('{} = thisR3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_R"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_RComponents = [polygon]
    for thisComponent in fix_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_R"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_R"-------
    for thisComponent in fix_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R3.addData('polygon.started', polygon.tStartRefresh)
    R3.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "Test_R"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setPos((r*1.45*cos((pos-2)%6*(pi/3)),r*1.45*sin((pos-2)%6*(pi/3))))
    image.setSize((size*1.45,size*1.45))
    image.setImage(stim)
    key_resp_r.keys = []
    key_resp_r.rt = []
    _key_resp_r_allKeys = []
    # keep track of which components have finished
    Test_RComponents = [image, key_resp_r]
    for thisComponent in Test_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_R"-------
    while continueRoutine:
        # get current time
        t = Test_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_r* updates
        waitOnFlip = False
        if key_resp_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_r.frameNStart = frameN  # exact frame index
            key_resp_r.tStart = t  # local t and not account for scr refresh
            key_resp_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_r, 'tStartRefresh')  # time at next scr refresh
            key_resp_r.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_r.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_r.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_r.getKeys(keyList=['p','o'], waitRelease=False)
            _key_resp_r_allKeys.extend(theseKeys)
            if len(_key_resp_r_allKeys):
                key_resp_r.keys = _key_resp_r_allKeys[-1].name  # just the last key pressed
                key_resp_r.rt = _key_resp_r_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_R"-------
    for thisComponent in Test_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R3.addData('image.started', image.tStartRefresh)
    R3.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_r.keys in ['', [], None]:  # No response was made
        key_resp_r.keys = None
    R3.addData('key_resp_r.keys',key_resp_r.keys)
    if key_resp_r.keys != None:  # we had a response
        R3.addData('key_resp_r.rt', key_resp_r.rt)
    R3.addData('key_resp_r.started', key_resp_r.tStartRefresh)
    R3.addData('key_resp_r.stopped', key_resp_r.tStopRefresh)
    # the Routine "Test_R" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'R3'


# ------Prepare to start Routine "round4"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
round4Components = []
for thisComponent in round4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
round4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "round4"-------
while continueRoutine:
    # get current time
    t = round4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=round4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "round4"-------
for thisComponent in round4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "round4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Ins_R"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_r.keys = []
key_ins_r.rt = []
_key_ins_r_allKeys = []
# keep track of which components have finished
Ins_RComponents = [ins_r, key_ins_r]
for thisComponent in Ins_RComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_R"-------
while continueRoutine:
    # get current time
    t = Ins_RClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_RClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_r* updates
    if ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_r.frameNStart = frameN  # exact frame index
        ins_r.tStart = t  # local t and not account for scr refresh
        ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_r, 'tStartRefresh')  # time at next scr refresh
        ins_r.setAutoDraw(True)
    
    # *key_ins_r* updates
    waitOnFlip = False
    if key_ins_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_r.frameNStart = frameN  # exact frame index
        key_ins_r.tStart = t  # local t and not account for scr refresh
        key_ins_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_r, 'tStartRefresh')  # time at next scr refresh
        key_ins_r.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_r.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_r.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_r.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_r_allKeys.extend(theseKeys)
        if len(_key_ins_r_allKeys):
            key_ins_r.keys = _key_ins_r_allKeys[-1].name  # just the last key pressed
            key_ins_r.rt = _key_ins_r_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_RComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_R"-------
for thisComponent in Ins_RComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_r.started', ins_r.tStartRefresh)
thisExp.addData('ins_r.stopped', ins_r.tStopRefresh)
# check responses
if key_ins_r.keys in ['', [], None]:  # No response was made
    key_ins_r.keys = None
thisExp.addData('key_ins_r.keys',key_ins_r.keys)
if key_ins_r.keys != None:  # we had a response
    thisExp.addData('key_ins_r.rt', key_ins_r.rt)
thisExp.addData('key_ins_r.started', key_ins_r.tStartRefresh)
thisExp.addData('key_ins_r.stopped', key_ins_r.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_R" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
R4 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='R4')
thisExp.addLoop(R4)  # add the loop to the experiment
thisR4 = R4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisR4.rgb)
if thisR4 != None:
    for paramName in thisR4:
        exec('{} = thisR4[paramName]'.format(paramName))

for thisR4 in R4:
    currentLoop = R4
    # abbreviate parameter names if possible (e.g. rgb = thisR4.rgb)
    if thisR4 != None:
        for paramName in thisR4:
            exec('{} = thisR4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_R"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_RComponents = [polygon]
    for thisComponent in fix_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_R"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_R"-------
    for thisComponent in fix_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R4.addData('polygon.started', polygon.tStartRefresh)
    R4.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "Test_R"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setPos((r*1.45*cos((pos-2)%6*(pi/3)),r*1.45*sin((pos-2)%6*(pi/3))))
    image.setSize((size*1.45,size*1.45))
    image.setImage(stim)
    key_resp_r.keys = []
    key_resp_r.rt = []
    _key_resp_r_allKeys = []
    # keep track of which components have finished
    Test_RComponents = [image, key_resp_r]
    for thisComponent in Test_RComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_R"-------
    while continueRoutine:
        # get current time
        t = Test_RClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_RClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp_r* updates
        waitOnFlip = False
        if key_resp_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_r.frameNStart = frameN  # exact frame index
            key_resp_r.tStart = t  # local t and not account for scr refresh
            key_resp_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_r, 'tStartRefresh')  # time at next scr refresh
            key_resp_r.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_r.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_r.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_r.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_r.getKeys(keyList=['p','o'], waitRelease=False)
            _key_resp_r_allKeys.extend(theseKeys)
            if len(_key_resp_r_allKeys):
                key_resp_r.keys = _key_resp_r_allKeys[-1].name  # just the last key pressed
                key_resp_r.rt = _key_resp_r_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_RComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_R"-------
    for thisComponent in Test_RComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    R4.addData('image.started', image.tStartRefresh)
    R4.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_r.keys in ['', [], None]:  # No response was made
        key_resp_r.keys = None
    R4.addData('key_resp_r.keys',key_resp_r.keys)
    if key_resp_r.keys != None:  # we had a response
        R4.addData('key_resp_r.rt', key_resp_r.rt)
    R4.addData('key_resp_r.started', key_resp_r.tStartRefresh)
    R4.addData('key_resp_r.stopped', key_resp_r.tStopRefresh)
    # the Routine "Test_R" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'R4'


# ------Prepare to start Routine "Ins_L"-------
continueRoutine = True
# update component parameters for each repeat
key_ins_l.keys = []
key_ins_l.rt = []
_key_ins_l_allKeys = []
# keep track of which components have finished
Ins_LComponents = [ins_l, key_ins_l]
for thisComponent in Ins_LComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ins_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ins_L"-------
while continueRoutine:
    # get current time
    t = Ins_LClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ins_LClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins_l* updates
    if ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_l.frameNStart = frameN  # exact frame index
        ins_l.tStart = t  # local t and not account for scr refresh
        ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_l, 'tStartRefresh')  # time at next scr refresh
        ins_l.setAutoDraw(True)
    
    # *key_ins_l* updates
    waitOnFlip = False
    if key_ins_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ins_l.frameNStart = frameN  # exact frame index
        key_ins_l.tStart = t  # local t and not account for scr refresh
        key_ins_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ins_l, 'tStartRefresh')  # time at next scr refresh
        key_ins_l.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ins_l.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ins_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ins_l.status == STARTED and not waitOnFlip:
        theseKeys = key_ins_l.getKeys(keyList=['space'], waitRelease=False)
        _key_ins_l_allKeys.extend(theseKeys)
        if len(_key_ins_l_allKeys):
            key_ins_l.keys = _key_ins_l_allKeys[-1].name  # just the last key pressed
            key_ins_l.rt = _key_ins_l_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ins_LComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins_L"-------
for thisComponent in Ins_LComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins_l.started', ins_l.tStartRefresh)
thisExp.addData('ins_l.stopped', ins_l.tStopRefresh)
# check responses
if key_ins_l.keys in ['', [], None]:  # No response was made
    key_ins_l.keys = None
thisExp.addData('key_ins_l.keys',key_ins_l.keys)
if key_ins_l.keys != None:  # we had a response
    thisExp.addData('key_ins_l.rt', key_ins_l.rt)
thisExp.addData('key_ins_l.started', key_ins_l.tStartRefresh)
thisExp.addData('key_ins_l.stopped', key_ins_l.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ins_L" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
L4 = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='L4')
thisExp.addLoop(L4)  # add the loop to the experiment
thisL4 = L4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisL4.rgb)
if thisL4 != None:
    for paramName in thisL4:
        exec('{} = thisL4[paramName]'.format(paramName))

for thisL4 in L4:
    currentLoop = L4
    # abbreviate parameter names if possible (e.g. rgb = thisL4.rgb)
    if thisL4 != None:
        for paramName in thisL4:
            exec('{} = thisL4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix_L"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_LComponents = [polygon_2]
    for thisComponent in fix_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fix_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix_L"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fix_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix_L"-------
    for thisComponent in fix_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L4.addData('polygon_2.started', polygon_2.tStartRefresh)
    L4.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    
    # ------Prepare to start Routine "Test_L"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_2.setPos((r*4/2.8*cos((pos-2)%6*(pi/3)),r*4/2.8*sin((pos-2)%6*(pi/3))))
    image_2.setSize((size*4/2.8,size*4/2.8))
    image_2.setImage(stim)
    key_resp_l.keys = []
    key_resp_l.rt = []
    _key_resp_l_allKeys = []
    # keep track of which components have finished
    Test_LComponents = [image_2, key_resp_l]
    for thisComponent in Test_LComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_L"-------
    while continueRoutine:
        # get current time
        t = Test_LClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_LClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *key_resp_l* updates
        waitOnFlip = False
        if key_resp_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_l.frameNStart = frameN  # exact frame index
            key_resp_l.tStart = t  # local t and not account for scr refresh
            key_resp_l.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_l, 'tStartRefresh')  # time at next scr refresh
            key_resp_l.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_l.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_l.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_l.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_l.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_l_allKeys.extend(theseKeys)
            if len(_key_resp_l_allKeys):
                key_resp_l.keys = _key_resp_l_allKeys[-1].name  # just the last key pressed
                key_resp_l.rt = _key_resp_l_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_LComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_L"-------
    for thisComponent in Test_LComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    L4.addData('image_2.started', image_2.tStartRefresh)
    L4.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_l.keys in ['', [], None]:  # No response was made
        key_resp_l.keys = None
    L4.addData('key_resp_l.keys',key_resp_l.keys)
    if key_resp_l.keys != None:  # we had a response
        L4.addData('key_resp_l.rt', key_resp_l.rt)
    L4.addData('key_resp_l.started', key_resp_l.tStartRefresh)
    L4.addData('key_resp_l.stopped', key_resp_l.tStopRefresh)
    # the Routine "Test_L" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'L4'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
