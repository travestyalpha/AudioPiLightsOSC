from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import time
import types
import os
#import RPi.GPIO as GPIO
import binascii
import pygame
import pyfirmata

from pyfirmata import Arduino, util
board = Arduino('\\.\COM3')

pygame.mixer.init()

server = OSCServer( ("192.168.1.70", 8080) )#This has to be the IP of the RaspberryPi on the network
#client = OSCClient()

def handle_timeout(self):
    print ("waiting")
server.handle_timeout = types.MethodType(handle_timeout, server)
 
def C(path, tags, args, source):
    print "C"
    numnuts = pygame.mixer.Sound("numnuts.wav")
    numnuts.play()
    numnuts.set_volume(1.0)

    board.digital[13].write(1) #Set the LED pin to 1 (High)
    board.pass_time(1)
    board.digital[13].write(0) # Set the LED pin to 0 (Low)
    board.pass_time(1)
    

def Csharp(path, tags, args, source):
    print "C#"
    #winsound.Beep(277,250)

def D(path, tags, args, source):
    print "D"
    horse = pygame.mixer.Sound("0859.ogg")
    horse.play()
    horse.set_volume(1.0)

    board.digital[12].write(1) #Set the LED pin to 1 (High)
    board.pass_time(1)
    board.digital[12].write(0) # Set the LED pin to 0 (Low)
    board.pass_time(1)
    

def Dsharp(path, tags, args, source):
    print "D#"
    #winsound.Beep(311,250)

def E(path, tags, args, source):
    print "E"
    wilhelm = pygame.mixer.Sound("0477.ogg")
    wilhelm.play()

    board.digital[11].write(1) #Set the LED pin to 1 (High)
    board.pass_time(1)
    board.digital[11].write(0) # Set the LED pin to 0 (Low)
    board.pass_time(1)
    

def F(path, tags, args, source):
    print "F"
    #winsound.Beep(349,250)

    board.digital[10].write(1) #Set the LED pin to 1 (High)
    board.pass_time(1)
    board.digital[10].write(0) # Set the LED pin to 0 (Low)
    board.pass_time(1)    

def Fsharp(path, tags, args, source):
    print "F#"
    #winsound.Beep(370,250)

def G(path, tags, args, source):
    print "G"
    #winsound.Beep(392,250)

    board.digital[9].write(1) #Set the LED pin to 1 (High)
    board.pass_time(1)
    board.digital[9].write(0) # Set the LED pin to 0 (Low)
    board.pass_time(1)
    

def Gsharp(path, tags, args, source):
    print "G#"
    #winsound.Beep(415,250)

def A(path, tags, args, source):
    print "A"
    #winsound.Beep(440,250)

def Asharp(path, tags, args, source):
    print "A#"
    #winsound.Beep(466,250)

def B(path, tags, args, source):
    print "B"
    #winsound.Beep(494,250)

def CC(path, tags, args, source):
    print "CC"
    #winsound.Beep(523,250)

#These are all the add-ons that you can name in the TouchOSC layout designer (you can set the values and directories)

server.addMsgHandler("/C", C)
server.addMsgHandler("/Csharp", Csharp)
server.addMsgHandler("/D", D)
server.addMsgHandler("/Dsharp", Dsharp)
server.addMsgHandler("/E", E)
server.addMsgHandler("/F", F)
server.addMsgHandler("/Fsharp", Fsharp)
server.addMsgHandler("/G", G)
server.addMsgHandler("/Gsharp", Gsharp)
server.addMsgHandler("/A", A)
server.addMsgHandler("/Asharp", Asharp)
server.addMsgHandler("/B", B)
server.addMsgHandler("/CC", CC)

#The way that the MSG Handlers work is by taking the values from set accessory, then it puts them into a function
#The function then takes the values and separates them according to their class (args, source, path, and tags)

while True:
    server.handle_request()

server.close()
#This will kill the server when the program ends
