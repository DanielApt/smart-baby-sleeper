import pygame
import os
# import keyboard
from gpiozero import Button

# We use this HAT: https://thepihut.com/products/hi-fi-sound-card-hat-for-raspberry-pi-with-speakers?variant=37627825062083
# Which has GPIO 17 available for programming
# Change this if you use a different add-on or HAT
PROGRAMMABLE_PIN = 17
index = 0
volumes = [0.3, 0.5, 0.75, 1]

def cycle_volume():
    global index
    index += 1

directory = os.path.dirname(__file__)
audio_file = os.path.join(directory, '..', 'audio', 'rain-2.mp3')

button = Button(PROGRAMMABLE_PIN)

pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.set_volume(volumes[index])
pygame.mixer.music.play(loops = -1)


while pygame.mixer.music.get_busy() == True:
    button.when_released = cycle_volume
    pygame.mixer.music.set_volume(volumes[index % len(volumes)])
    continue
