import pygame
import os
import keyboard
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
directory = os.path.dirname(__file__)
# audio_file = os.path.join(directory, './rain-2.mp3'
audio_file = os.path.join(directory, '..', 'audio', 'rain-2.mp3')
volume = 1

pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(loops = -1)
while pygame.mixer.music.get_busy() == True:
    while True:
        key = keyboard.read_key()

        if key == 'down':
            print(key)
            volume -= 0.5

        elif key == 'up':
            volume += 0.5

        pygame.mixer.music.set_volume(volume)

    continue
