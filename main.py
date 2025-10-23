import win32gui
import win32api
import win32con
import keyboard
import random
import time
import sys

time.sleep(2)

MOVE_VARIATION = 1
COLOR_TOLERANCE = 70
coords_base = [(1120, 670), (1000, 670), (880, 670), (760, 670)]
target_rgb = (47, 47, 55)

def color_approx_equal(c1, c2, tolerance):
    return all(abs(a - b) <= tolerance for a, b in zip(c1, c2))

def get_pixel_color(x, y):
    hdc = win32gui.GetDC(0)
    color = win32gui.GetPixel(hdc, x, y)
    win32gui.ReleaseDC(0, hdc)
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    return (r, g, b)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def check_exit_key():
    exit_keys = ['home', 'insert']
    return any(keyboard.is_pressed(key) for key in exit_keys)

time.sleep(2)

try:
    while True:
        if check_exit_key():
            print("завершена нажатием клавиш Home или Insert")
            sys.exit(0)

        for x_base, y_base in coords_base:
            x_offset = random.randint(-MOVE_VARIATION, MOVE_VARIATION)
            y_offset = random.randint(-MOVE_VARIATION, MOVE_VARIATION)
            x = x_base + x_offset
            y = y_base + y_offset

            pixel_color = get_pixel_color(x, y)
            if color_approx_equal(pixel_color, target_rgb, COLOR_TOLERANCE):
                click(x, y)
except KeyboardInterrupt:
    print("\nзавершён")