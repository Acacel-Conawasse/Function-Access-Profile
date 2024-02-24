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
                pyautogui.press('tab', presses=20, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=21, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        # Dataviews - Group Edits
        elif index == 1:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass
        # Group approval of timecards
        elif index == 2:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
        # Add
        elif index == 3:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=43, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass       
        # Remove
        elif index == 4:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=45, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
        #Remove All
        elif index == 5:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=47, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Edit data after non account approval by self
        elif index == 6:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=49, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Edit data after non account approval by others
        elif index == 7:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=51, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Comments in Dataviews
        elif index == 8:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Notes for comments in Dataviews
        elif index == 9:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=55, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Filter by Selected Job Seniority
        elif index == 10:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=59, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Pay code edits in Dataviews
        elif index == 11:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=61, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Mark Exceptions as Reviewed
        elif index == 12:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('enter')
                pass
        #Pay from Schedule in Dataviews
        elif index == 13:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=55, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=58, interval=0.07)
                pass    
		#Start Pay from Schedule
        elif index == 14:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=60, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass 
		#Stop Pay from Schedule
        elif index == 15:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=62, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass    
		#Punch edits in Dataviews#
        elif index == 16:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=55, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=55, interval=0.07)
                pyautogui.press('enter')
                pass 
        #Sign-off in Dataviews        
        elif index == 17:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=60, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pass
        #Add        
        elif index == 18:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=65, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Remove            
        elif index == 19:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=60, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=60, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Transfers in Dataviews
        elif index == 20:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pass    #Open
        #Perform labor category transfers
        elif index == 21:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=68, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform cost center transfers
        elif index == 22:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=70, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform work rule transfers
        elif index == 23:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=72, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform job transfers
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Start Time on pay code edits
        elif index == 25:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Scheduling
        elif index == 26:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=29, interval=0.07)
                pass    #Open
        #Open Shift Available Notification
        elif index == 27:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pass  
        #Schedule access
        elif index == 28:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=34, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass 
        #Filter Location by Employee Group
        elif index == 29:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pyautogui.press('enter')
                pass
        #Schedule Views
        elif index == 30:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=39, interval=0.07)
                pass    #Open   
		#	Employment Term View of Schedule
        elif index == 31:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass    
		#	Employee View of Schedule
        elif index == 32:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=43, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Group View of Schedule
        elif index == 33:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=45, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Job View of Schedule
        elif index == 34:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=47, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Display Location-based Add-on Data when Employee Group Filtering Enabled
        elif index == 35:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=49, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Run reports within Schedule Planner
        elif index == 36:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=51, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Pay Code Comments in Schedules
        elif index == 37:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Notes for Pay Code Comments in Schedules
        elif index == 38:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pyautogui.press('enter')
                pass   
        #Schedule Quick Actions 50 tabs 
        elif index == 39:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass    #Open    
        #Add segment tag
        elif index == 40:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=55, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Schedule pay code edits
        elif index == 41:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=61, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #View audit trails in Schedules
        elif index == 42:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Filter audit trails in Schedules
        elif index == 43:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                pass    #Close 
        #Transfers in Schedules
        elif index == 44:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pass    #Open
        #Perform labor category transfers
        elif index == 45:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=68, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Perform cost center transfers
        elif index == 46:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=70, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Perform work rule transfers
        elif index == 47:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=72, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Perform job transfers
        elif index == 48:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=74, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Schedule Shift Comments
        elif index == 49:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=76, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Notes for Schedule Shift Comments
        elif index == 50:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=78, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Mark Schedule Posted
        elif index == 51:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Mark Schedule Unposted
        elif index == 52:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=86, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Availability
        elif index == 53:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Workload Planner 76
        elif index == 54:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=79, interval=0.07)
                pass    #Open
        #Budget Pattern
        elif index == 55:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=82, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
        #Budget Calendar
        elif index == 56:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=85, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=88, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=88, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)       
        #Plan Pattern
        elif index == 57:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=90, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=92, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=92, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=4, interval=0.07)
        #Plan Calendar
        elif index == 58:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=93, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=98, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=95, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)  
        #Budget Volume
        elif index == 59:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=96, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=98, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=98, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)  
        #Plan Volume
        elif index == 60:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=99, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=101, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=101, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)  
        #Actual Volume
        elif index == 61:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=102, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=104, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=104, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)         
        #Actual Calendar
        elif index == 62:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=105, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=107, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=107, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)      
        #Generate Workload
        elif index == 63:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=109, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Lock Volume
        elif index == 64:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=111, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Run Priority Scheduling Engine
        elif index == 65:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=113, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Run Schedule Engine
        elif index == 66:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=117, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=4, interval=0.07)
                pass  #Regular
        #Schedule Day Lock
        elif index == 66:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=122, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=5, interval=0.07)
                pass  #Regular 
        #Shift Profile Sets
        elif index == 67:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=123, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=127, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=127, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
        #Shift Profiles
        elif index == 67:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=128, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=132, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=132, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=4, interval=0.07)
            #4 Tabs to Enter Time Off     
        #Enter Time Off
        elif index == 68:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=138, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular
            #6 Tabs to Pay Code Edits using Pattern Day
        #Pay Code Edits using Pattern Day
        elif index == 69:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=146, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=8, interval=0.07)
                pass  #Regular
            #8 Tabs to Add to schedule Group 
        #Add to Schedule Group
        elif index == 70:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=148, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Remove from Schedule Group
        elif index == 71:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=150, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Edit Group Schedules
        elif index == 72:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=152, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Lock Shifts
        elif index == 73:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=154, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular     
        #Assign Breaks
        elif index == 74:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=156, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular 
        #Team Definition Setup
        elif index == 76:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=158, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular 
        #Team Definition Setup Extended Access
        elif index == 78:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=162, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular 
        #Replace shift
        elif index == 79:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=164, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular     
        #Append shift
        elif index == 80:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=166, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Insert transfer <Two Tabs to Employee visibility period and enter> Not closing any Drops 
        elif index == 81:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Employee Visibility Periods
        elif index == 82:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=136, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=139, interval=0.07)
                pass    #Open    
        #Request Submission Control
        elif index == 83:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=141, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Request Period Extended Access
        elif index == 84:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=143, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Recurrent / Rolling periods
        elif index == 85:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=145, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Multi-Group options
        elif index == 86:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=147, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Employee Priority option
        elif index == 87:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=149, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Personal Hyperfinds for Employee Query
        elif index == 88:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=151, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Visibility Period Actions
        elif index == 89:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=153, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Call Log
        elif index == 90:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=155, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Call List
        elif index == 91:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=157, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Group Edit Results
        elif index == 92:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=159, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Calendar views for Managers <Closing Scheduling with initial click and 26 Tabs> 
        elif index == 93:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Timecard Editor for Managers
        #Timecard access
        #Allow negatives in Timecard Editor
        #Approval in Timecard Editor
        #Add
        #Remove
        #Remove All
        #Edit data after non account approval by self
        #Edit data after non account approval by others
        #Cancel meal deductions in Timecard Editor
        #Comments in Timecard Editor
            


        #Manager - Common Setup
        elif index == 93:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=24, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Hyperfind
        elif index == 94:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass
        #Query conditions
        elif index == 95:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')        
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Display Business Structure & Job Information in Hyperfind
        elif index == 96:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=34, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #General Information category
        elif index == 97:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Timekeeper category
        elif index == 98:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=38, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Time Management category
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=42, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Scheduler category
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=44, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Advanced Scheduler category
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=50, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #User Information category
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=52, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Role - Timekeeper category
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=60, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Attendance Category
        elif index == 25:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Query tabs
        elif index == 95:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('enter')        
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=35, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Assemble Query tab
        elif index == 25:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Query visibility
        elif index == 95:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=35, interval=0.07)
                pyautogui.press('enter')        
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Ad hoc queries
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=40, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Personal queries
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position
                pyautogui.press('tab', presses=46, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular
        #Query Manager
        elif index == 25:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #People Editor
        elif index == 20:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pass    #Open    
        #Person
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=33, interval=0.07)
                pyautogui.write('All')
                pyautogui.press('tab', presses=38, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular    
        #License view
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=39, interval=0.07)
                pyautogui.press('up')
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
            elif setting == 'disallowed':
                pass  #Regular    
        #Employee Group
        elif index == 20:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=41, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=44, interval=0.07)
                pass    #Open
        #Information view
        elif index == 20:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pass    #Open

        #Person name
        #Person ID
        #Hire date
        #Employment status
        #Access user account
        #User name
        #Primary Labor Category
        #Primary Job
        #Time Zone
        #Reports To
        #Reports To Field
        #Manager ID Column
        #Seniority Date
        #Contact Information view
        #E-mail
        #Telephone
        #Additional Information view
        #Person's Dates View
        #Devices Group
        # Timekeeping Group
        #Timekeeper view
        #Percent Allocation Assignment
        #Employment Terms view
        #Scheduling Group
        #Scheduler view
        #Skills & Certifications view
        #Skills on a person
        #Certifications on a person
        #Accruals Group
        #Leave Group
        #Attendance Group
        #Assignments group
        #Jobs and Business Structure
        #Event Manager
        #Individual events
        #Table Import
        #Biometrics
        #Schedule Configuration
        #Skills & Certifications
        #Certifications
        #Skills
        #Workload Setup
        #Shift Template Configuration
        #Schedule Groups Configuration
        #Schedule Score Setup
        #Scheduler Profiles
        #Process Management setup
        #Activities Configuration
        #Integrations
        #Workforce Attendance Setup
        #Schedule Group Edit
        #Developer Portal
        #Hours of Operation
        #Forecast Configuration
        #Universal Device Manager
        #Batch Processing
        #Statutory Reporting
        #Average Pay Rates
        #Event/Notification
        #Data Hub


        # Delay to avoid sending inputs too quickly
        time.sleep(0.5)

# Read settings.txt and apply settings
def main():
    initial_x, initial_y = -1166, -215  # Update these values to the initial click position
    with open('settings.txt', mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        for row in reader:
            automate_settings(row, initial_x, initial_y)
            time.sleep(3)  # Delay between processing each row

if __name__ == "__main__":
    main()
