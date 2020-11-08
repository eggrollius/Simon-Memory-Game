from unicorn_hat_sim import unicornhathd as hat
import keyboard
import time
import random
import sys
from playsound import playsound

rotation = 270  # This value can be modified if needed to change the orientation
hat.rotation(rotation)

global memory
memory = []

global level
level = 1

white = (100, 100, 100)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
clear = (0, 0, 0)


def flash_quadrant(quadrant):
    if quadrant == 1:
        for i in range(8):
            for j in range(8):
                hat.set_pixel(i, j, *green)
    elif quadrant == 2:
        for i in range(8):
            for j in range(8):
                hat.set_pixel(i, j + 8, *red)
    elif quadrant == 3:
        for i in range(8):
            for j in range(8):
                hat.set_pixel(i + 8, j, *yellow)
    elif quadrant == 4:
        for i in range(8):
            for j in range(8):
                hat.set_pixel(i + 8, j + 8, *blue)
    hat.show()
    playsound('short-beep.mp3')


def clear_all():
    for i in range(16):
        for j in range(16):
            hat.set_pixel(i, j, *white)
    hat.show()


def flash_screen():
    for i in range(0, level):
        flash_quadrant(memory[i])
        time.sleep(0.75)
        clear_all()


memory.append(random.randint(1, 4))


def check_answer(v, i):
    flash_quadrant(v)
    time.sleep(1)
    clear_all()
    if memory[i] != v:
        game_over()


def test_memory():
    counter = int(0)
    for i in range(len(memory)):
        while True:
            if keyboard.is_pressed('q'):
                check_answer(1, counter)
                counter += 1
                break
            if keyboard.is_pressed('w'):
                check_answer(2, counter)
                counter += 1
                break
            if keyboard.is_pressed('a'):
                check_answer(3, counter)
                counter += 1
                break
            if keyboard.is_pressed('s'):
                check_answer(4, counter)
                counter += 1
                break


def calculate():
    global level
    level += 1
    memory.append(random.randint(1, 4))


def game_over():
    for i in range(16):
        hat.set_pixel(i, i, *red)
        hat.set_pixel(15 - i, i, *red)
    hat.show()
    playsound('fail.mp3')
    sys.exit()
for i in range(1, 5):
    flash_quadrant(i)
time.sleep(10)

while 1 == 1:
    flash_screen()

    clear_all()

    test_memory()

    calculate()
