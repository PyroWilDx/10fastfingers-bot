from PIL import Image
from pytesseract import image_to_string
import keyboard
import time

image_path = "Capture.PNG"
text = image_to_string(Image.open(image_path), lang="fra")

time.sleep(1)

wait_duration = 0.035

for c in text:
    keyboard.write(c)
    time.sleep(wait_duration)
