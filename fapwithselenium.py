import pyautogui
import csv
import time

# Function to perform mouse click at specified coordinates
def mouse_click(x, y):
    pyautogui.click(x, y)

# Function to automate settings based on a row from the settings.txt
def automate_settings(row, initial_x, initial_y):
    # Reset to the starting point for each setting
    mouse_click(initial_x, initial_y)
    
    # Process each setting based on its index
    for index, setting in enumerate(row):
        print(f"Processing setting at index {index}: {setting}")  # Print the current setting being processed

        # Manager - Department Manager
        if index == 0:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=20, interval=0.1)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position if needed
                pyautogui.press('tab', presses=21, interval=0.1)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        # Dataviews - Group Edits
        elif index == 1:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.1)
                pyautogui.press('enter')
                pass

        # Group approval of timecards
        elif index == 2:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=38, interval=0.1)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position if needed
                pyautogui.press('tab', presses=41, interval=0.1)
                pass
        # Add
        elif index == 3:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position if needed
                pyautogui.press('tab', presses=43, interval=0.1)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.1)
                pass
            
        # Remove
        elif index == 4:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position if needed
                pyautogui.press('tab', presses=45, interval=0.1)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.1)
                pass
        # Implement additional logic for other columns based on the pattern above
        
        # Delay to avoid sending inputs too quickly
        time.sleep(0.5)

# Read settings.txt and apply settings
def main():
    initial_x, initial_y = 3530, 145  # Update these values to the initial click position
    with open('settings.txt', mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        for row in reader:
            automate_settings(row, initial_x, initial_y)
            time.sleep(3)  # Delay between processing each row

if __name__ == "__main__":
    main()
