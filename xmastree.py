from sense_hat import SenseHat, ACTION_RELEASED
import time
import os
from signal import pause

sense = SenseHat()
sense.clear()

sense.low_light = True
sense.set_rotation(180)
sense.show_message("ready")

X = [0, 100, 0] # Green
O = [0, 0, 0] # Black
W = [255, 255, 255]  # White
B = [139, 69, 19] # Brown
U = [0, 0, 128] # Blue
R = [255, 0, 0] # Red
P = [125, 125, 64] #PINK
Y = [255, 255, 0] #YELLOW
A = [255, 165, 0] # orange
G = [123, 123, 123] #grey
L = [75, 0, 130] # INDIGO

xmas_tree_1 = [
O, O, O, X, X, O, O, O,
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
X, X, X, X, X, X, X, X,
O, O, O, B, B, O, O, O,
O, O, O, B, B, O, O, O
]
xmas_tree_2 = [
O, O, O, Y, Y, O, O, O,
O, O, X, X, X, X, O, O,
O, Y, X, X, X, X, Y, O,
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
Y, X, X, X, X, X, X, Y,
O, O, O, B, B, O, O, O,
O, R, O, B, B, O, R, O
]

def treelights_on(event):
    sense.set_pixels(xmas_tree_2)

def treelights_off(event):
    sense.set_pixels(xmas_tree_1)

def pi_shutdown(event):
   sense.show_message("bye bye")
   os.system("sudo shutdown -h now")

def low_light_on(event):
    sense.low_light=True

def low_light_off(event):
    sense.low_light=False

sense.stick.direction_down = treelights_on
sense.stick.direction_up = treelights_off
sense.stick.direction_middle = pi_shutdown
sense.stick.direction_left = low_light_off
sense.stick.direction_right = low_light_on

while True:
    pass
