import pyautogui
import time
import csv 


file_path = "C:/Users/kwiggin7/Documents/Automation/Function_Access_Profiles/Function-Access-Profile/settings.txt"
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

            elif  setting == "Open an online form":
                press_tab_and_decide(value,9)
            
            elif  setting == "Show Person Number":
                press_tab_and_decide(value,2)
                
            elif  setting == "Employee":
                #Employee (Expand) Mouse Click (-1664,69)
                 move_and_click(1015, 765)
                 time.sleep(1)
                 #Employee (Mouse Click in front (-1631,66), Click on two tabs, and then click up + down (Disallow All))
                 move_and_click(1050, 185)
                 time.sleep(1)
                 pyautogui.press(['tab', 'tab'])
                 time.sleep(2)
                 pyautogui.hotkey('up', 'down')
                 time.sleep(1)
                 pyautogui.press(['tab'])
                 
            elif  setting == "Time Stamp for Employees":
                #Time Stamp for Employees (Expand) 
                 move_and_click(1078,213)
                 time.sleep(1)
                 #Time Stamp for Employees
                 move_and_click(1165,181)
                 time.sleep(1)
                 pyautogui.press(['tab', 'tab'])
                 time.sleep(2)

            elif  setting == "Cancel meal deductions in Time Stamp":
                press_tab_and_decide(value,2)
                
            elif  setting == "Calendar":
                #Time Stamp for Employees (Expand) 
                 move_and_click(1033, 304)
                 time.sleep(1)
                 #Time Stamp for Employees
                 move_and_click(1079, 182)
                 time.sleep(1)
                 pyautogui.press(['tab', 'tab'])
                 time.sleep(2)
                 
            elif  setting == "Calendar views for employees":
                press_tab_and_decide(value,2)
                
            elif  setting == "Print Schedule":
                press_tab_and_decide(value,2)
                
            elif  setting == "Employee Visibility Periods":
                press_tab_and_decide(value,2)
                
            elif  setting == "Timecard Editor for Employees (My Timecard)":
                #Time Stamp for Employees (Expand) 
                 move_and_click(1100, 303)
                 time.sleep(1)
                 #Time Stamp for Employees
                 move_and_click(1265,175)
                 time.sleep(1)
                 pyautogui.press(['tab', 'tab'])
                 time.sleep(2)
                 
            elif  setting == "Comments in My Timecard - Add":
                press_tab_and_decide(value,9)
                
            elif  setting == "Comments in My Timecard - Delete":
                press_tab_and_decide(value,1)
                
            elif  setting == "Notes for Comments in My Timecard":
                press_tab_and_decide(value,2)
                
            elif  setting == "Hours Worked amount in My Timecard":
                press_tab_and_decide(value,2)
                
                
            elif  setting == "Pay Codes in My Timecard - Edit":
                #Pay Codes in My TImecard (Expand)
                move_and_click(1091, 354)
                time.sleep(1)
                #Time Stamp for Employees
                move_and_click(1180,180)
                time.sleep(1)
                pyautogui.press(['tab', 'tab'])
                time.sleep(2)
                
                press_tab_and_decide(value,2)
                
            elif  setting == "Pay Codes in My Timecard - View":
                press_tab_and_decide(value,2)
                
            elif  setting == "Move Amounts in My Timecard":
                press_tab_and_decide(value,2)
                
            elif  setting == "Punch edits in My Timecard":
                press_tab_and_decide(value,4)
                
            elif  setting == "Calculate totals in My Timecard":
                press_tab_and_decide(value,5)
                
            elif  setting == "Totals breakdown in My Timecard":
                press_tab_and_decide(value,2)
                
            elif  setting == "View schedules in My timecard":
                press_tab_and_decide(value,4)
                
            elif  setting == "View the Audit Trail Tab in My Timecard":
                press_tab_and_decide(value,12)
                
            elif  setting == "Activities in My Timecard":
                #Pay Codes in My TImecard (Expand)
                move_and_click(1067, 702)
                time.sleep(1)
                #Time Stamp for Employees
                move_and_click(1157,179)
                time.sleep(1)
                pyautogui.press(['tab', 'tab'])
                time.sleep(2)
            
            elif  setting == "Transfers - View transfers":
                #Transfers (Expand)
                move_and_click(1041, 390)
                time.sleep(1)
                #Time Stamp for Employees
                move_and_click(1072,210)
                time.sleep(1)
                pyautogui.press(['tab', 'tab'])
                time.sleep(2)
                
                press_tab_and_decide(value,2)  
                
            elif  setting == "Perform cost center transfers":
                press_tab_and_decide(value,2)
                
            elif  setting == "Perform labor category transfers":
                press_tab_and_decide(value,2)
                
            elif  setting == "Perform work rule transfers":
                press_tab_and_decide(value,2)
                
            elif  setting == "Perform job transfers":
                press_tab_and_decide(value,2)
                
            elif  setting == "Access to Employee Home Page":
                press_tab_and_decide(value,12)
                
            elif  setting == "Employee access to My Actions list":
                press_tab_and_decide(value,2)
            
            elif  setting == "Location Data":
                #Location Data (Expand)
                move_and_click(1049, 512)
                time.sleep(1)
                #Time Stamp for Employees
                move_and_click(1105,361)
                time.sleep(1)
                pyautogui.press(['tab', 'tab'])
                time.sleep(2) 
                
            elif  setting == "View location data":
                press_tab_and_decide(value,4)
                
            elif  setting == "Enable location schedule":
                press_tab_and_decide(value,12)
                
            elif  setting == "Access unposted schedule":
                press_tab_and_decide(value,9)
                
            elif  setting == "My Requests":
                press_tab_and_decide(value,2)
                
            elif  setting == "Comments & Notes in my request":
                press_tab_and_decide(value,5)
                
            elif  setting == "Impersonation Access":
                press_tab_and_decide(value,2)
                
            elif  setting == "Offline":
                #Location Data (Expand)
                move_and_click(1032, 788)
                time.sleep(1)
                #Time Stamp for Employees
                move_and_click(1057,760)
                time.sleep(1)
                pyautogui.press(['tab', 'tab'])
                time.sleep(2) 
                
            elif  setting == "Mobile App Punch":
                press_tab_and_decide(value,2) 