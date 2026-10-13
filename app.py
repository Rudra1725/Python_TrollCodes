import random
import time
import pyautogui

pyautogui.FAILSAFE = True

print("Ghost Mouse running... Move mouse to any corner to abort.")

try:
    while True:
        time.sleep(random.uniform(4, 10))

        dx = random.choice([-2, -1, 1, 2])
        dy = random.choice([-2, -1, 1, 2])

        x, y = pyautogui.position()
        pyautogui.moveTo(x + dx, y + dy, duration=0.1)
except KeyboardInterrupt:
    print("Prank stopped.")