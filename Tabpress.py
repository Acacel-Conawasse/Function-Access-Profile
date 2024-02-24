import pyautogui
import time

def execute_actions_with_mouse_clicks(coordinates, sequences):
    """
    Performs mouse clicks at specified coordinates, then executes a sequence of tab presses followed by an action (Enter or Down).

    :param coordinates: Tuple of (x, y) coordinates for the mouse click.
    :param sequences: A list of tuples, each representing a sequence of actions.
                      Each tuple is (number_of_tabs, action) where action is either 'enter', 'down', or 'tab'.
    """
    # Perform the initial mouse click at the specified coordinates
    pyautogui.click(coordinates[0], coordinates[1])

    # Execute each sequence of actions
    for tabs, action in sequences:
        pyautogui.click = (-1711, -175)
        # Press Tab the specified number of times
        for _ in range(tabs):
            pyautogui.press('tab')
            time.sleep(0.05)  # Short delay between presses

        # Perform the action after pressing Tab
        if action == 'enter':
            pyautogui.press(['enter'])
            time.sleep(1)
        elif action == 'up':
            pyautogui.hotkey(['up', 'down'])
            time.sleep(1)
        elif action == 'tab':  # Assuming 'tab' means an additional tab press
            pyautogui.press(['tab'])

        time.sleep(1)  # A short delay after the action before starting the next sequence

# Coordinates for the initial mouse click
mouse_click_coordinates = (-1281, -217)
            
# Define the sequences based on your instructions
sequences = [
    (20, 'enter'),  # Click 17 tabs and enter.
    (21, 'up'),   # Click 18 tabs and down.
    (23, 'enter'),  # Click 20 tabs and enter.
    (38, 'enter'),  # Click 35 tabs then enter.
    (41, 'tab'),    # Click 38 tabs (assuming an additional tab press).
]#

# Execute the actions with the initial mouse click
execute_actions_with_mouse_clicks(mouse_click_coordinates, sequences)
time.sleep(0.7)                         