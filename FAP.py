import pyautogui
import time
import csv 


file_path = "settings.txt"
#"(1291, 105)" = (1291, 105)
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


def tabto(count):
    move_and_click(1291, 105)
    for _ in range(count):
        pyautogui.press('tab')
        time.sleep(0.1)
        
        
# Function to press tab the required number of times and then either up+tab or down based on the setting
def press_tab_and_decide(setting, tabs_count):
    # Press tab the required number of times
    tabto(tabs_count)
    
    # Decide whether to press 'up' and 'tab' or just 'down'
    if setting.lower() == 'allowed':
        pyautogui.hotkey('up')
        time.sleep(1.2)
    else:
        pyautogui.press('down')
    time.sleep(0.7)



def tab_and_open(count):
    tabto(count)
    pyautogui.press('enter')
    time.sleep(1)
        

    

# Read the settings from the file
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Assuming the first row is the header with setting names
        for setting, value in row.items():
            
            # Perform the action based on the setting value
            if setting == "Everyone":
                #Everyone (Expand) Mouse Click (-1664,69)
                
               #time.sleep(1)
               ##Everyone (Mouse Click in front (-1631,66), Click on two tabs, and then click up + down (Disallow All))
               #move_and_click(-1631, 66)
               #time.sleep(1)
               #pyautogui.press(['tab', 'tab'])
               #time.sleep(2)
               #pyautogui.hotkey('up', 'down')
                time.sleep(1)
               # pyautogui.press(['tab'])

            elif  setting == "Open an online form":
                press_tab_and_decide(value,9)
            
            elif  setting == "Show Person Number":
                press_tab_and_decide(value,2)
                
            elif  setting == "Employee":
                #Employee (Expand) Mouse Click (-1664,69)
                 tab_and_open(17)
                 time.sleep(1)
                 tabto(18)
                 pyautogui.hotkey('up', 'down')
                 time.sleep(1)
                 tabto(18)
                 #pyautogui.press(['tab'])
                 #
            elif  setting == "Time Stamp for Employees":
                #Time Stamp for Employees (Expand) 
                 tab_and_open(20)
                 time.sleep(2)

            elif  setting == "Cancel meal deductions in Time Stamp":
                press_tab_and_decide(value,23)
                # end of Time Stamp for Employees. Closing group    
                tab_and_open(20)
                time.sleep(2)
            
            elif  setting == "Calendar":
                #Time Stamp for Employees (Expand) 
                 tab_and_open(23)
                 time.sleep(2)
                 
            elif  setting == "Calendar views for employees":
                press_tab_and_decide(value,26)
                
            elif  setting == "Print Schedule":
                press_tab_and_decide(value,28)
                
            elif  setting == "Employee Visibility Periods":
                press_tab_and_decide(value,30)
                # end of Calendar. Closing group    
                tab_and_open(23)
                time.sleep(2)
                
            elif  setting == "Timecard Editor for Employees (My Timecard)":
                #Timecard Editor for Employees (My Timecard) (Expand) 
                 tab_and_open(30)
                 time.sleep(2)
                 
            elif  setting == "Comments in My Timecard - Add":
                press_tab_and_decide(value,40)
                
            elif  setting == "Comments in My Timecard - Delete":
                press_tab_and_decide(value,41)
                
            elif  setting == "Notes for Comments in My Timecard":
                press_tab_and_decide(value,43)
                
            elif  setting == "Hours Worked amount in My Timecard":
                press_tab_and_decide(value,45)
                
                
            elif  setting == "Pay Codes in My Timecard - Edit":
                #Pay Codes in My TImecard (Expand)
                tab_and_open(47)
                time.sleep(2)
                
                #Check pay code - edit field 
                press_tab_and_decide(value,50)
                
            elif  setting == "Pay Codes in My Timecard - View":
                press_tab_and_decide(value,52)
                
            elif  setting == "Move Amounts in My Timecard":
                press_tab_and_decide(value,54)
                # End of group. Pay Codes in My TImecard (Close)
                tab_and_open(47)
                time.sleep(2)
                
            elif  setting == "Punch edits in My Timecard":
                press_tab_and_decide(value,50)
                
            elif  setting == "Calculate totals in My Timecard":
                press_tab_and_decide(value,55)
                
            elif  setting == "Totals breakdown in My Timecard":
                press_tab_and_decide(value,57)
                
            elif  setting == "View schedules in My timecard":
                press_tab_and_decide(value,61)
                
            elif  setting == "View the Audit Trail Tab in My Timecard":
                press_tab_and_decide(value,73)
                #Timecard Editor for Employees (My Timecard) (close) 
                tab_and_open(30)
                time.sleep(2)
                
            #elif  setting == "Activities in My Timecard":
            #    tab_and_open(33)
            #    time.sleep(2)
            
            elif  setting == "Transfers - View transfers":
                #Transfers (Expand)
                tab_and_open(36)
                time.sleep(2)
                press_tab_and_decide(value,39)  
                
            elif  setting == "Perform cost center transfers":
                press_tab_and_decide(value,41)
                
            elif  setting == "Perform labor category transfers":
                press_tab_and_decide(value,43)
                
            elif  setting == "Perform work rule transfers":
                press_tab_and_decide(value,45)
                
            elif  setting == "Perform job transfers":
                press_tab_and_decide(value,47)
                #Transfers (close)
                tab_and_open(36)
                time.sleep(2)
                
            elif  setting == "Access to Employee Home Page":
                press_tab_and_decide(value,49)
                
            elif  setting == "Employee access to My Actions list":
                press_tab_and_decide(value,51)
            
            elif  setting == "Location Data":
                #Location Data (expand)
                tab_and_open(53)
                time.sleep(2)
                
            elif  setting == "View location data":
                press_tab_and_decide(value,58)
                #Location Data (close)
                tab_and_open(53)
                time.sleep(2)
                
            elif  setting == "Enable location schedule":
                press_tab_and_decide(value,58)
                
            elif  setting == "Access unposted schedule":
                press_tab_and_decide(value,67)
                
            elif  setting == "My Requests":
                press_tab_and_decide(value,69)
                
            elif  setting == "Comments & Notes in my request":
                press_tab_and_decide(value,74)
                
            elif  setting == "Impersonation Access":
                press_tab_and_decide(value,76)
                
            elif  setting == "Offline":
                #Offline (expand)
                tab_and_open(78)
                time.sleep(2)
                
            elif  setting == "Mobile App Punch":
                press_tab_and_decide(value,81) 
                
                
                
                
            #### Dept Manager ####
                
            # if setting is Timecard Editor for Managers click and open()
            
            # if Timecard access
                # tab and decide() but add conditions for 'All' and 'All but self'
                # press up for all but self
                # press a for all
                
            # if Allow negatives in Timecard Editor tab and decide
            
            # if Approval in Timecard Editor open and select
            
            # 