import pyautogui
import time
import csv 


file_path = "C:/Users/kwiggin7/Documents/Automation/Function_Access_Profiles/Function-Access-Profile/settings.txt"
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
    
def mouse_click(x, y):
    pyautogui.click(x, y)    


def tabto(count,initial_x=1291, initial_y=100):
    mouse_click(initial_x, initial_y)
    pyautogui.press('tab', presses=count, interval=0.07)
        
        
# Function to press tab the required number of times and then either up+tab or down based on the setting
def press_tab_and_decide(setting, tabs_count):
    # Press tab the required number of times
    tabto(tabs_count)
    # Decide whether to press 'up' and 'tab' or just 'down'
    if setting == 'allowed' or setting == "All But Self":
        pyautogui.press('up')
        time.sleep(2)
    #elif setting == 'All':
    #    pyautogui.press('a')
    #    time.sleep(2)
    else:
        pyautogui.press('down')
    time.sleep(0.7)



def tab_and_open(count):
    tabto(count)
    pyautogui.press('enter')
    time.sleep(1)
        

    
def automate_settings(row, initial_x, initial_y):
    mouse_click(initial_x, initial_y)
    
    # Assuming the first row is the header with setting names
    for index, setting in enumerate(row):
        print(f"Processing setting at index {index}: {setting}")  # Print the current setting being processed
        
        
        # Employee
        
        
        ## Employee    
        #if  index == 0:
        #    #Employee (Expand) Mouse Click (-1664,69)
        #     tab_and_open(17)
        #     time.sleep(1)
        #     tabto(18)
        #     pyautogui.press('d')
        #     time.sleep(2)
        #
        ## Time Stamp for Employees
        #elif  index == 1:
        #    #Time Stamp for Employees (Expand) 
        #     tab_and_open(20)
        #     time.sleep(1)
        #
        ##Cancel meal deductions in Time Stamp     
        #elif  index == 2:
        #    press_tab_and_decide(setting,23)
        #    # end of Time Stamp for Employees. Closing group    
        #    tab_and_open(20)
        #    time.sleep(1)
        #
        ## "Calendar"
        #elif  index == 3:
        #    # Calendar (Expand) 
        #     tab_and_open(23)
        #     time.sleep(1)
        #
        ## Calendar views for employees     
        #elif  index == 4:
        #    press_tab_and_decide(setting,26)
        #
        ## Print Schedule    
        #elif  index == 5:
        #    press_tab_and_decide(setting,28)
        #
        ## Employee Visibility Periods    
        #elif  index == 6:
        #    press_tab_and_decide(setting,30)
        #    # end of Calendar. Closing group    
        #    tab_and_open(23)
        #    time.sleep(1)
        #
        ## Timecard Editor for Employees (My Timecard)    
        #elif  index == 7:
        #    #Timecard Editor for Employees (My Timecard) (Expand) 
        #     tab_and_open(30)
        #     time.sleep(1)
        #
        ## Comments in My Timecard - Add     
        #elif  index == 8:
        #    press_tab_and_decide(setting,40)
        #
        ## Comments in My Timecard - Delete    
        #elif  index == 9:
        #    press_tab_and_decide(setting,41)
        #
        ## Notes for Comments in My Timecard    
        #elif  index == 10:
        #    press_tab_and_decide(setting,43)
        #
        ## Hours Worked amount in My Timecard    
        #elif  index == 11:
        #    press_tab_and_decide(setting,45)
        #    
        ## "Pay Codes in My Timecard - Edit"    
        #elif  index == 12:
        #    #Pay Codes in My TImecard (Expand)
        #    tab_and_open(47)
        #    time.sleep(1)
        #    
        #    #Check pay code - edit field 
        #    press_tab_and_decide(setting,50)
        #    
        ## Pay Codes in My Timecard - View    
        #elif  index == 13:
        #    press_tab_and_decide(setting,52)
        #
        ## Move Amounts in My Timecard    
        #elif  index == 14:
        #    press_tab_and_decide(setting,54)
        #    # End of group. Pay Codes in My TImecard (Close)
        #    tab_and_open(47)
        #    time.sleep(1)
        #
        ## Punch edits in My Timecard    
        #elif  index == 15:
        #    press_tab_and_decide(setting,50)
        #
        ## Calculate totals in My Timecard    
        #elif  index == 16:
        #    press_tab_and_decide(setting,55)
        #
        ## Totals breakdown in My Timecard    
        #elif  index == 17:
        #    press_tab_and_decide(setting,57)
        #
        ## View schedules in My timecard    
        #elif  index == 18:
        #    press_tab_and_decide(setting,61)
        #
        ## View the Audit Trail Tab in My Timecard    
        #elif  index == 19:
        #    press_tab_and_decide(setting,73)
        #    #Timecard Editor for Employees (My Timecard) (close) 
        #    tab_and_open(30)
        #    time.sleep(1)
        #
        ## Transfers - View transfers    
        #elif  index == 20:
        #    #Transfers (Expand)
        #    tab_and_open(36)
        #    time.sleep(1)
        #    press_tab_and_decide(setting,39)  
        #
        ## Perform cost center transfers    
        #elif  index == 21:
        #    press_tab_and_decide(setting,41)
        #
        ## Perform labor category transfers    
        #elif  index == 22:
        #    press_tab_and_decide(setting,43)
        #
        ## Perform work rule transfers    
        #elif  index == 23:
        #    press_tab_and_decide(setting,45)
        #
        ## Perform job transfers    
        #elif  index == 24:
        #    press_tab_and_decide(setting,47)
        #    #Transfers (close)
        #    tab_and_open(36)
        #    time.sleep(1)
        #
        ## Access to Employee Home Page    
        #elif  index == 25:
        #    press_tab_and_decide(setting,49)
        #
        ## Employee access to My Actions list    
        #elif  index == 26:
        #    press_tab_and_decide(setting,51)
        #
        ## Location Data
        #elif  index == 27:
        #    #Location Data (expand)
        #    tab_and_open(53)
        #    time.sleep(1)
        #
        ## View location data    
        #elif  index == 28:
        #    press_tab_and_decide(setting,58)
        #    #Location Data (close)
        #    tab_and_open(53)
        #    time.sleep(1)
        #
        ## Enable location schedule    
        #elif  index == 29:
        #    press_tab_and_decide(setting,58)
        #
        ## Access unposted schedule    
        #elif  index == 30:
        #    press_tab_and_decide(setting,67)
        #
        ## My Requests    
        #elif  index == 31:
        #    press_tab_and_decide(setting,69)
        #
        ## Comments & Notes in my request    
        #elif  index == 32:
        #    press_tab_and_decide(setting,74)
        #
        ## Impersonation Access    
        #elif  index == 33:
        #    press_tab_and_decide(setting,76)
        #
        ## Offline    
        #elif  index == 34:
        #    #Offline (expand)
        #    tab_and_open(78)
        #    time.sleep(1)
        #
        ## Mobile App Punch    
        #elif  index == 35:
        #    press_tab_and_decide(setting,81) 
        #    #end of Employee (close)
        #    tab_and_open(17)
        #    time.sleep(1)
            
            
        #### Dept Manager ####
        
        
        
        
        # Timi 
        
        
        
        
        
        # Timecard Editor for Managers (expand)
        if  index == 0:
             tab_and_open(33)
             time.sleep(1)
             
        # Timecard access
        elif  index == 1:    
            press_tab_and_decide(setting,36)
        
        # Allow negatives in Timecard Editor
        elif  index == 2:
            press_tab_and_decide(setting,38)
        
        
        # Approval in Timecard Editor (expand)
        elif  index == 3:
            tab_and_open(40)
            time.sleep(1)
        
        # Add
        elif  index == 4:
            press_tab_and_decide(setting,43)
            
        # Remove
        elif  index == 5:
            press_tab_and_decide(setting,45)
            
        # Remove All
        elif  index == 6:
            press_tab_and_decide(setting,47)
            
        # Edit data after non account approval by self
        elif  index == 7:
            press_tab_and_decide(setting,49)
            
        # Edit data after non account approval by others
        elif  index == 8:
            press_tab_and_decide(setting,51) 
            # End of Approval in Timecard Editor (close)
            tab_and_open(40)
            time.sleep(1)
        
        
        # Cancel meal deductions in Timecard Editor
        elif  index == 9:
            press_tab_and_decide(setting,43)
            
        # Comments in Timecard Editor
        elif  index == 10:
            press_tab_and_decide(setting,45)
            press_tab_and_decide(setting,46)
            
            
        # Notes for Comments in Timecard Editor (expand)
        elif  index == 11:
            tab_and_open(48)
            time.sleep(1)
            
        # Add or Remove
        elif  index == 12:
            press_tab_and_decide(setting,51)
         
        # Remove Notes added by Others
        elif  index == 13:
            press_tab_and_decide(setting,53)
            # end of Notes for Comments in Timecard Editor (close)
            tab_and_open(48)
            time.sleep(1)
            
        # Hours Worked amount in Timecard Editor
        elif  index == 14:
            press_tab_and_decide(setting,51)
            
            
        # Pay codes in Timecard Editor (expand)
        elif  index == 15:    
            tab_and_open(53)
            time.sleep(1)
            
        # Edit
        elif  index == 16:
            press_tab_and_decide(setting,56)
        
        # View
        elif  index == 17:
            press_tab_and_decide(setting,58)
        
        # Move Amount
        elif  index == 18:
            press_tab_and_decide(setting,60)
        
        # Start Time on pay code edits
        elif  index == 19:
            press_tab_and_decide(setting,64)
        
        # Justify Missed Time Exceptions
        elif  index == 20:
            press_tab_and_decide(setting,66)
        
        # Mark Exceptions Reviewed in Timecard Editor
        elif  index == 21:
            press_tab_and_decide(setting,68)
            # End of Pay codes in Timecard Editor (close)
            tab_and_open(53)
            time.sleep(1)
            
        # Punch edits in Timecard Editor
        elif  index == 22:
            press_tab_and_decide(setting,56)
        
        
        # Sign-off in Timecard Editor (expand)
        elif  index == 23:    
            tab_and_open(58)
            time.sleep(1)
        
        # Add
        elif  index == 24:
            press_tab_and_decide(setting,61)
        
        # Remove
        elif  index == 25:
            press_tab_and_decide(setting,63)
            # End of Sign-off in Timecard Editor (close)
            tab_and_open(58)
            time.sleep(1)
            
        # Calculate totals in Timecard Editor
        elif  index == 26:
            press_tab_and_decide(setting,61)
        
        # Totals breakdown in Timecard Editor
        elif  index == 27:
            press_tab_and_decide(setting,63)
        
        
        
        # Transfers in Timecard Editor (expand)
        elif  index == 28:    
            tab_and_open(67)
            time.sleep(1)
        
        # View transfers
        elif  index == 29:
            press_tab_and_decide(setting,70)
        
        # Perform cost center transfers
        elif  index == 30:
            press_tab_and_decide(setting,72)
        
        # Perform labor category transfers
        elif  index == 31:
            press_tab_and_decide(setting,74)
        
        # Perform work rule transfers
        elif  index == 32:
            press_tab_and_decide(setting,76)
        
        # Perform job transfers
        elif  index == 33:
            press_tab_and_decide(setting,78)
            # End of Transfers in Timecard Editor (close)
            tab_and_open(67)
            time.sleep(1)
            
            
        # View schedules in Timecard Editor
        elif  index == 34:
            press_tab_and_decide(setting,70)
        
       ## Accruals in Timecard Editor (expand)
       #elif  index == 35:    
       #    tab_and_open(74)
       #    time.sleep(1)
        
        # Reports in Timecard Editor (expand)
        elif  index == 35:    
            tab_and_open(79)
            time.sleep(1)
        
        # Rule Analysis Tool Report in Timecard editor
        elif  index == 36:
            press_tab_and_decide(setting,82)
            # End of Reports in Timecard Editor (close)
            tab_and_open(79)
            time.sleep(1)
        
        # View the Audit Trail Tab in Timecard Editor
        elif  index == 37:
            press_tab_and_decide(setting,82)
            
        # Enable Job Transfer Validation
        elif  index == 38:
            press_tab_and_decide(setting,86)
            # End of Timecard Editor for Managers (close)
            tab_and_open(33)
            time.sleep(1)
        
        
        # Multiple Assignments (Skip)
        # Activities in Timecard Editor (Skip)
        # Notes For Comments in Activities (Skip)
        # Accept Activities in Timecard Editor (Skip)
        
        
        # Reports (expand)
        elif  index == 39:    
            tab_and_open(42)
            time.sleep(1)
        
        # Run reports
        elif  index == 40:
            press_tab_and_decide(setting,45)
        
        # Report scheduling
        elif  index == 41:
            press_tab_and_decide(setting,47)
        
        # Report setup (skip)
        
        # Schedule reports for others
        elif  index == 42:
            press_tab_and_decide(setting,52)
        
        # Report Scheduling: All Access
        elif  index == 43:
            press_tab_and_decide(setting,54)
        
        # Report Page
        elif  index == 44:
            press_tab_and_decide(setting,56)
        
        # Schedule report delivery to email as attachment
        elif  index == 45:
            press_tab_and_decide(setting,58)
            # Reports (close) 
            tab_and_open(42)
            time.sleep(1)
        
            
        # E-mail Notifications to Managers (expand)
        elif  index == 46:    
            tab_and_open(45)
            time.sleep(1)
        
        # E-mail a completed group edit
        elif  index == 47:
            press_tab_and_decide(setting,48)
        
        # E-mail when a group edit was not completed
        elif  index == 48:
            press_tab_and_decide(setting,50)
        
        # E-mail when event status has changed
        elif  index == 49:
            press_tab_and_decide(setting,52)
            # E-mail Notifications to Managers (close)
            tab_and_open(45)
            time.sleep(1)
            
        # Manager access to Actions list
        elif  index == 50:
            press_tab_and_decide(setting,48)
        
        # Forecasting (skip)
        # Forecast Planner (skip)
        # Operational Dashboard (skip)
        
        
        # Attendance for Managers (expand)
        elif  index == 51:    
            tab_and_open(55)
            time.sleep(1)
        
        # View Audit Data
        elif  index == 52:
            press_tab_and_decide(setting,58)
        
        # Perfect attendance definitions
        elif  index == 53:
            press_tab_and_decide(setting,60)
        
        # Source policy
        elif  index == 54:
            press_tab_and_decide(setting,62)
        
        # Attendance Actions
        elif  index == 55:
            tabto(64)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
                
        # Apply Rules
        elif  index == 56:
            tabto(66)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
                
        # Attendance Balance Resets and Adjustments
        elif  index == 57:
            # two fields that change together
            # Change field one
            tabto(68)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # Change field two    
            tabto(69)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
                
        # Attendance Events
        elif  index == 58:
            # three fields that change together
            # Change field one
            tabto(71)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # Change field two    
            tabto(72)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # Change field three    
            tabto(73)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
         
        # Refine Filters (skip)
        
        # Access to Attendance Detail Page and Calendar
        elif  index == 59:
            press_tab_and_decide(setting,80)
        
        # Forward Attendance Documents
        elif  index == 60:
            press_tab_and_decide(setting,82)
        
        # View Attendance Documents
        elif  index == 61:
            press_tab_and_decide(setting,84)
            # End of Attendance for Managers (close)
            tab_and_open(55)
            time.sleep(1)
            
            
        # Location Data (expand)
        elif  index == 62:    
            tab_and_open(58)
            time.sleep(1)
        
        # View location data
        elif  index == 63:
            press_tab_and_decide(setting,61)
            # Location Data (close)
            tab_and_open(58)
            time.sleep(1)
            
        # Leave Cases For Managers (expand)
        elif  index == 64:    
            tab_and_open(61)
            time.sleep(1)
        
        # Access to Leave Landing Page
        elif  index == 65:
            press_tab_and_decide(setting,64)
        
        # Access to Leave Case Editor, Leave Calendar and Takings List
        elif  index == 66:
            press_tab_and_decide(setting,66)
        
        # Access to Leave Audit
        elif  index == 67:
            press_tab_and_decide(setting,68)
        
        # Manage Leave Case (expand)
        elif  index == 68:    
            tab_and_open(70)
            time.sleep(1)
        
        # Leave Case Details (skip)
        # Leave Case Eligibility and Rules (skip)
        
        # Leave Case Documents (expand)
        elif  index == 69:    
            tab_and_open(85)
            time.sleep(1)
        
        # Forward documents
        elif  index == 70:
            tabto(88)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
                
        # View documents
        elif  index == 71:
            tabto(92)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # End of Leave Case Documents (close)
            tab_and_open(85)
            time.sleep(1)
            
        # Leave Case Additional Information
        elif  index == 72:
            tabto(88)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
        
        # Leave Case Notes
        elif  index == 73:
            if setting == 'VIEW-Allowed':
                tabto(93)
                pyautogui.press('a')
                time.sleep(2)
            # Manage Leave Case (close)
            tab_and_open(70)
            time.sleep(1)
            # Leave Cases For Managers (close)
            tab_and_open(61)
            time.sleep(1)
            
        # Leave Case Notifications (skip)
        # Leave of Absence Time (skip)
        # Leave time in Timecard Editor (skip)
        # Leave time in Scheduling (skip)
        # Leave time actions (skip)
        # Commit to Timecard (skip)
        # Commit to Schedule (skip)
        
        # Edit signed off time (expand)
        elif  index == 74:    
            tab_and_open(66)
            time.sleep(1)
        # Allow enable edits for employees
        elif  index == 75:
            press_tab_and_decide(setting,73)
            # End of Edit signed off time (close)
            tab_and_open(66)
            time.sleep(1)
            
        # Dataview Personalization
        elif  index == 76:
            press_tab_and_decide(setting,69)
            
        # Include inactive and terminated employees into search result
        elif  index == 77:
            press_tab_and_decide(setting,71)
        
        # Employee Search
        elif  index == 78:
            press_tab_and_decide(setting,73)
        
            
            
def main():
    initial_x, initial_y = 2289, 134  # Update these values to the initial click position
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        for row in reader:
            automate_settings(row, initial_x, initial_y)
            time.sleep(3)  # Delay between processing each row



if __name__ == "__main__":
    main()
    
