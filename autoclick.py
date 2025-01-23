import pyautogui
import time

# Optional: a small sleep to give you time to switch to the correct window
time.sleep(3)

# Path to your screenshot of the "Generate" button
button_image_path = 'generate_button.png'

# Locate the button on the screen
# 'confidence' can be lowered if it's having trouble matching the image.
# PyAutoGUI may require the pillow library or an updated version if it complains about confidence.
location = pyautogui.locateOnScreen(button_image_path, confidence=0.8)

if location is not None:
    # Get the center of the location
    center_x, center_y = pyautogui.center(location)
    # Move the mouse to the center
    pyautogui.moveTo(center_x, center_y, duration=0.5)  # 0.5 seconds to move
    # Click
    pyautogui.click()
    print("Generate button clicked!")
else:
    print("Generate button not found on screen.")
