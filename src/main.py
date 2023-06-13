import pygame
import os
import keyboard
# import RPi.GPIO as GPIO

index = 0
volumes = [0.25, 0.5, 0.75, 1, 0]

# GPIO.setmode(GPIO.BCM)
directory = os.path.dirname(__file__)
# audio_file = os.path.join(directory, './rain-2.mp3'
audio_file = os.path.join(directory, '..', 'audio', 'rain-2.mp3')
volume = 1

pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.set_volume(volumes[index])
pygame.mixer.music.play(loops = -1)

while pygame.mixer.music.get_busy() == True:
    while True:
        key = keyboard.read_key()

        if key == 'down':
            print(key)
            index -= 1

        elif key == 'up':
            index += 1

        pygame.mixer.music.set_volume(volumes[index % len(volumes)])

    continue
