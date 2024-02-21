import pyautogui
import time
import csv 


file_path = "settings.txt"
pyautogui.FAILSAFE = True  # Enable failsafe by moving the mouse to the upper left corner

#Functions 
def move_and_click(x, y, delay=0.7):
    """
    Moves the mouse to a specified position and clicks.
    Parameters:
    - x (int): The x-coordinate to move the mouse to.
    - y (int): The y-coordinate to move the mouse to.
    - delay (float): The time in seconds to wait after the click. Default is 0.7 seconds.
    """
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(delay)

# Function to press tab the required number of times and then either up+tab or down based on the setting
def press_tab_and_decide(setting, tabs_count):
    # Press tab the required number of times
    for _ in range(tabs_count):
        pyautogui.press('tab')
        time.sleep(0.9)  # Adding a small delay to ensure the UI can catch up

    # Decide whether to press 'up' and 'tab' or just 'down'
    if setting.lower() == 'allowed':
        pyautogui.hotkey('up')
        time.sleep(1.2)
        pyautogui.hotkey('tab')
    else:
        pyautogui.press('down')
    time.sleep(0.7)


#Everyone (Expand) Mouse Click (-1664,69)
#move_and_click(-1664, 69)
#time.sleep(1)
##Everyone (Mouse Click in front (-1631,66), Click on two tabs, and then click up + down (Disallow All))
#move_and_click(-1631, 66)
#time.sleep(1)
#pyautogui.press(['tab', 'tab'])
#time.sleep(2)
#pyautogui.hotkey('up', 'down')
#Home Page Personalization (click three tabs, if allowed click up arrow key + tab, else click down)
#pyautogui.press(['tab', 'tab', 'tab'])

# Read the settings from the file
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Assuming the first row is the header with setting names
        for setting, value in row.items():
            
            # Perform the action based on the setting value
            if setting == "Everyone":
                #Everyone (Expand) Mouse Click (-1664,69)
                move_and_click(-1664, 69)
                time.sleep(1)
                #Everyone (Mouse Click in front (-1631,66), Click on two tabs, and then click up + down (Disallow All))
                move_and_click(-1631, 66)
                time.sleep(1)
                pyautogui.press(['tab', 'tab'])
                time.sleep(2)
                pyautogui.hotkey('up', 'down')
                time.sleep(1)
                pyautogui.press(['tab'])

            if setting == "Open an online form":
                press_tab_and_decide(value,9)
            
            if setting == "Show Person Number":
                press_tab_and_decide(value,2)

            # You can add similar conditions for other settings here
            # ...
            time.sleep(1)  # Wait for 1 second before the next action