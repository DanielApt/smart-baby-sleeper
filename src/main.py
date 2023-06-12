import pygame
import os

directory = os.path.dirname(__file__)
# audio_file = os.path.join(directory, './rain-2.mp3'
audio_file = os.path.join(directory, '..', 'audio', 'rain-2.mp3')

pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(loops = -1)
while pygame.mixer.music.get_busy() == True:
    continue


