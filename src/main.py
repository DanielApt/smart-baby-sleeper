#!/usr/bin/env python3

# From https://raspberrypi.stackexchange.com/a/7089/155012
import pygame
pygame.mixer.init()
pygame.mixer.music.load("audio/underwater-white-noise.mp3")
pygame.mixer.music.play(loops = -1) # Make it loop infinitely
while pygame.mixer.music.get_busy() == True:
    continue
